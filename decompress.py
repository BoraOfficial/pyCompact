from PIL import Image

# Open the image
image = Image.open("_temp.png")

# Get the red channel of the image
image = image.split()[0]

# Get the pixel values
pixels = image.getdata()

# Convert the pixel values to bytes
bytes = bytes(pixels)

# Write the bytes to a new file
with open("compressed.jpg", "wb") as f:
    f.write(bytes)
