import sys
import os
import re
from PIL import Image

def get_image_size(instructions):
    return (len(instructions), 1) # TODO: output dimension parameters

def hex2rgb(strhex):
    r = int(strhex[:2], 16)
    g = int(strhex[2:4], 16)
    b = int(strhex[4:], 16)
    return (r, g, b)

def set_image_data(instructions, image):
    for i in range(len(instructions)):
        image[i, 0] = hex2rgb(instructions[i]) # TODO: output dimension param
    return image

# get ir filename and additional arguments
flags = []
for arg in sys.argv:
    if arg[0] == "-":
        flags.append(arg) # TODO: handle flags
    else:
        irpath = arg

# open ir file and get instructions
with open(irpath) as f:
    instructions = f.readlines()

# remove whitespace, newline, and comments
for i in range(len(instructions)):
    instructions[i] = instructions[i].strip("\n")
    instructions[i] = re.sub(ur'( )|(;.*$)', '', instructions[i])

instructions = [x for x in instructions if x != ""]
print instructions

# create Rainbow image
image = Image.new("RGB", get_image_size(instructions), "black")
pix = image.load()
pix = set_image_data(instructions, pix)

# write image file
# TODO: output name param
impath = os.path.splitext(irpath)[0]+'.bmp'
print impath
#image.save(impath)
