Python app for showing images directly in the terminal.

Define the image and size to show at the top of the file:
image = 'image.jpg'
windowwidth = 160

Yes, there are a million ways to make this better, but it was just a fun experiment. However, the key difference here is that it's not trying to use ASCII art. Instead, it creates the pixels using the a sub-divided box character (to create square pixels in the terminal), and then outputs using the full color space. This creates the most realistic terminal image possible within the limitations of the pixel sizes. You can make it better by reducing the terminal font-size. 
