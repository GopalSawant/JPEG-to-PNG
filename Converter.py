import sys
import os
from PIL import Image

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

for images in os.listdir(source_folder):
    img = Image.open(f"{source_folder}{images}")
    name = os.path.splitext(images)[0]
    if not os.path.isfile(f'{destination_folder}{name}.png'):
        img.save(f"{destination_folder}{name}.png", "png")
