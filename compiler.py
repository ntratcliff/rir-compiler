import sys
import os
import re
import math
import argparse
from PIL import Image

def get_image_size(instructions):
    size = (len(instructions), 1)
    if args.width is not None and args.height is not None:
        # check if dimensions are valid
        if args.width * args.height < len(instructions):
            raise ValueError('The provided dimensions are too small')
        size = (args.width, args.height)
    elif args.width is not None:
        # calculate minimum height
        height = int(math.ceil(len(instructions) / float(args.width)))
        size = (args.width, height)
    elif args.height is not None:
        # calculate minimum width
        width = int(math.ceil(len(instructions) / float(args.height)))
        size = (width, args.height)
    return size

def hex2rgb(strhex):
    r = int(strhex[:2], 16)
    g = int(strhex[2:4], 16)
    b = int(strhex[4:], 16)
    return (r, g, b)

def set_image_data(instructions, pix, size):
    rgb = []
    for ins in instructions:
        rgb.append(hex2rgb(ins))
    return image_data_as_dim(rgb, pix, size)

def image_data_as_dim(imdata, pix, size):
    # pad blank areas of the image
    for _ in range(len(imdata), size[0] * size[1]):
        imdata.append((0,0,0))
    imdata = [[imdata[size[0] * y + x] for x in range(size[0])] for y in range(size[1])]
    for y in range(size[1]):
        for x in range(size[0]):
            pix[x, y] = imdata[y][x]
    return pix

# get ir filename and additional arguments
parser = argparse.ArgumentParser(description='Compiler for the Rainbow Intermediate Representation.')
parser.add_argument('rirpath', type=str, help='rir file to be compiled')
parser.add_argument('--output', '-o', help='destination file for compiled Rainbow script')
parser.add_argument('--dim-x', '-x', dest='width', type=int, help='output image width, in pixels')
parser.add_argument('--dim-y', '-y', dest='height', type=int, help='output image height, in pixels')
# TODO: Verbose

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
size = get_image_size(instructions)
image = Image.new("RGB", size, "black")
pix = image.load()
pix = set_image_data(instructions, pix, size)

# write image file
if args.output is not None:
    impath = args.output
else:
    impath = os.path.splitext(args.rirpath)[0]+'.bmp'

image.save(impath)
