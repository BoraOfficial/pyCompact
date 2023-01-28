from PIL import Image
import numpy as np
from math import ceil

# Open the file and read the bytes
with open("filename.extension", "rb") as f:
    bytes = f.read()

# Create an empty image with a size of (width, height)
width = 100
height = ceil(len(bytes) / width)



# Convert the bytes to a list of integers
pixels = list(bytes)

# Create a new image with the same size as the original image
image = Image.new("L", (width, height))

# Set the pixels of the image
image.putdata(pixels)

# Save the image
image.save("_temp.png")

