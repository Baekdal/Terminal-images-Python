from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# set source and image file
image = 'image.jpg'
windowwidth = 160

# open the image
with Image.open(image) as image:

	# Convert to RGB (Usually not nessesary, but just prevents problems for happening)
	image = image.convert('RGB')

	# get the image size
	width, height = image.size

	# set image size to terminal window width (usually 80, but mine screen is bigger)
	newheight = newheight = int((height / width)*windowwidth)

	# resize the image
	image = image.resize((windowwidth,newheight), Image.LANCZOS)

	# get the pixel data
	pixellist = list(image.getdata())
	# convert pixel data into image rows
	pixelrows = [pixellist[x:x+windowwidth] for x in range(0, len(pixellist), windowwidth)]

	termimg = ''

	# loop trough the every second row
	for row in range(0,len(pixelrows),2):
		pixels = pixelrows[row]
		for pixel in range(windowwidth):

			# set the color from the first row + the one directly underneath
			fr,fg,fb = pixelrows[row][pixel]
			br,bg,bb = pixelrows[row+1][pixel]

			# Write it to the terminal using ▀ as a special character
			# the front color is set as the character color,
			# and the back color is set as the background, doubling
			# the resolution
			termimg += f'\x1b[38;2;{fr};{fg};{fb}m\x1b[48;2;{br};{bg};{bb}m▀\033[0m'

		termimg += '\n'
# write the character image to the terminal
print(termimg)
