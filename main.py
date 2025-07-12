import imageio.v3 as iio
filenames = ['chicklet1.png', 'chicklet2.png', 'chicklet3.png','chicklet4.png',]
images = [ ]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('team.gif', images, duration = 500, loop = 0)
print("Script started")

import imageio.v3 as iio
from PIL import Image
import numpy as np

print("Script started")

filenames = ['chicklet1.png', 'chicklet2.png', 'chicklet3.png', 'chicklet4.png']
images = []

# Load and check image shapes
for filename in filenames:
    img = Image.open(filename).convert("RGB")
    print(f"{filename} size: {img.size}")
    images.append(np.array(img.resize((256, 256))))  # Force resize to same shape

# Write to GIF
try:
    iio.imwrite('team.gif', images, duration=500, loop=0)
    print("GIF created successfully.")
except Exception as e:
    print("Error creating GIF:", e)
