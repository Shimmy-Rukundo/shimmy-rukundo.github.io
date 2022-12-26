from PIL import Image

# Open the image
im = Image.open('profile.jpg')

# Get the width and height of the image
width, height = im.size

# Convert the image to a mutable image (this is necessary to modify the pixel values)
im = im.convert('RGBA')

# Define the RGB color that you want to change to transparency
color = (255, 255, 255)  # red

# Iterate over all the pixels in the image
for x in range(width):
    for y in range(height):
        # Get the pixel at position (x, y)
        pixel = im.getpixel((x, y))

        # Check if the pixel has the same color as the color that you want to change
        if pixel[:3] == color:
            # Set the alpha value of the pixel to 0 (fully transparent)
            pixel = pixel[:3] + (0,)

            # Set the modified pixel back in the image
            im.putpixel((x, y), pixel)

# Save the modified image
im.save('modified_image.png', format='PNG')