import sys
import os
import re
import argparse
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
parser = argparse.ArgumentParser(description='Compiler for the Rainbow Intermediate Representation.')
parser.add_argument('rirpath', type=str, help='rir file to be compiled')
parser.add_argument('--output', '-o', help='destination file for compiled Rainbow script')

args = parser.parse_args()

# open ir file and get instructions
with open(args.rirpath) as f:
    instructions = f.readlines()

# remove whitespace, newline, and comments
for i in range(len(instructions)):
    instructions[i] = instructions[i].strip("\n")
    instructions[i] = re.sub(ur'( )|(;.*$)', '', instructions[i])

instructions = [x for x in instructions if x != ""]

# create Rainbow image
image = Image.new("RGB", get_image_size(instructions), "black")
pix = image.load()
pix = set_image_data(instructions, pix)

# write image file
if args.output is not None:
    impath = args.output
else:
    impath = os.path.splitext(args.rirpath)[0]+'.bmp'

image.save(impath)
