# -*- coding: utf-8 -*-

### MODULES

import sys
import os
sys.path.insert(0, os.getcwd() + "/lib")

# Importing GTL libraries
from txt_reader import *
from draw_bits import draw_bit_fnt
from shape_functions import *

from random import choice






### VARIABLES

# Absolute path of folder containing glyphs'txts
txt_path = os.getcwd() + "/assets/italic"

# Set glyphs'baseline row (counting from bottom of txt)
gly_baseline = 2

# Set the ratio between width of "pixelone" and its height:
# width_ratio = 2 means the module width will be twice its height
width_ratio = 1

# Set number of "pixelone" sub-units
box_col = 1
box_row = 1

# Set name of set (".alt1", ".alt2", ...)
set_suffix = ""






### SHAPE PROPERTIES

p_rectangle = {
    "scale": (1,1),
    "rotation": 0,
    "clockwise": True
    }

p_ellipse = {
    "squaring": .56,
    "scale": (1,1),
    "rotation": 0,
    "clockwise": True
    }

p_ellipse_t = {
    "squaring": 0,
    "scale": (1,1),
    "rotation": 0,
    "clockwise": True
    }

p_el_quarter = {
    "squaring": .56,
    "scale": (1,1),
    "rotation": 0,
    "clockwise": True
}

p_el_quarter_t = {
    "squaring": 0,
    "scale": (1,1),
    "rotation": 0,
    "clockwise": True
}

p_el_half = {
    "squaring": .56,
    "scale": (1, 1),
    "rotation": 0,
    "clockwise": True
}

p_el_half_t = {
    "squaring": 0,
    "scale": (1, 1),
    "rotation": 0,
    "clockwise": True
}

p_random = [
    (rectangle         , p_rectangle),
    (ellipse           , p_ellipse),
    #(ellipse           , p_ellipse_t),
    (ellipse_quarter_ro, p_el_quarter),
    #(ellipse_quarter_ro, p_el_quarter_t),
    (ellipse_half_ro   , p_el_half),
    (ellipse_half_ro   , p_el_half_t)
]



### SINTASSI

sintassi = {
    ".": (do_nothing, {"null": "null"}),
    "@": (rectangle, p_rectangle),
    "#": (rectangle, p_rectangle),
    "%": (do_nothing, {"null": "null"}),
    "&": (do_nothing, {"null": "null"}),
    "$": (do_nothing, {"null": "null"}),
    "+": (do_nothing, {"null": "null"})
}






### INSTRUCTIONS

# Selecting font in robofont
fnt = CurrentFont()

# Creating the dictionary with all the instructions
fnt_dict = get_font_from_folder(txt_path)

# Getting number of lines
first_key = next(iter(fnt_dict))
first_val = fnt_dict[first_key]
line_num = len(first_val)

# Calculating box height
box_hgt = 1000/line_num

# Calculating box width
box_wdt = box_hgt * width_ratio

# Calculating descender line
dsc_hgt = -box_hgt * gly_baseline






### DRAWING FONT

draw_bit_fnt(fnt = fnt,
             fnt_dict = fnt_dict,
             suffix = set_suffix,
             dsc_hgt = dsc_hgt,
             box_size = (box_wdt, box_hgt),
             box_layout = (box_row, box_col),
             syntax = sintassi)
