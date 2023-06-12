from PIL import Image
import os

PATH = "./static/"
PATH_NEW = "./static/compressed/"
IMAGE_DIMENSIONS = (13, 13)

filenames = os.listdir(PATH)


for file in filenames:
    if os.path.isdir(PATH + file):
        continue

    image = Image.open(PATH + file)

    original_size = image.size
    print("The original size of " + file + " is ", original_size)
    new_dimensions = IMAGE_DIMENSIONS

    if original_size[0] != original_size[1]:
        new_dimensions = (
            IMAGE_DIMENSIONS[0],
            int(original_size[1] / (original_size[0] / IMAGE_DIMENSIONS[0])),
        )

    image = image.resize(new_dimensions, Image.LANCZOS)

    image.save(PATH_NEW + file.split(".")
               [0] + ".webp", optimize=True, quality=85)
