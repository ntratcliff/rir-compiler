import sys
import re
from PIL import Image

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
