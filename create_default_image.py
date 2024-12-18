from PIL import Image, ImageDraw

# Create a new image with a white background
img = Image.new('RGB', (300, 300), color='#f0f0f0')

# Create a drawing object
draw = ImageDraw.Draw(img)

# Draw a circle for the avatar
draw.ellipse([50, 50, 250, 250], fill='#cccccc')

# Save the image
img.save('media/default.jpg')