from PIL import Image

# Images need to be converted from 'RGB' to 'RGBA', for Image.blend() to work
with Image.open("racing-helmet-unsplash.jpg").convert("RGBA") as image_a, Image.open(
    "red-bull-car-unsplash.jpg"
).convert("RGBA") as image_b:
    image_a_copy = image_a.copy()
    image_b_copy = image_b.copy()
    # need to resize image_b to match image_a, for blend() to work
    image_b_copy = image_b.resize((2265, 2831))
    # image_b needs to be the same size as image_a, for Image.blend() to work
    # thumbnail() modifies the size and maintains the aspect ratio
    image_a_copy.thumbnail((300, 300))
    image_b_copy.thumbnail((300, 300))

    for number in range(11):
        merged = Image.blend(image_a_copy, image_b_copy, number / 10)
        merged.save(f"merged_{number}.png")
        # merged.show()
