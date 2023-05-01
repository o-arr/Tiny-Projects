from PIL import Image, ImageFilter

# Images need to be converted from 'RGB' to 'RGBA', for Image.blend() to work
with Image.open("racing-helmet-unsplash.jpg").convert('RGBA') as image_a, Image.open("red-bull-car-unsplash.jpg").convert('RGBA') as image_b:
	image_b_copy = image_b.copy()
	# image_b needs to be the same size as image_a, for Image.blend() to work
	image_b_copy = image_b_copy.resize(image_a.size)
	for number in range(11):
		merged = Image.blend(image_a, image_b_copy, number / 10)
		merged.save(f'merged_{number}.png')
		#merged.show()