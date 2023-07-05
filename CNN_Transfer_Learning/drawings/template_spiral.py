"""
Code which creates the spiral used as template for drawing by people.
COULD be changed so that it generates the csv version, a png, and a drawing object.
"""

import json
from math import pi, cos, sin

import drawing

PATH = drawing.TEMPLATE_PATH
TEMPLATE_JSON_PATH = "./templateSpiralJSON.json"
STEP = 1000 #num steps when producing spiral (how detailed it is)
CYCLE_RADIUS = 73 #radius of the 3 individual cycles
# Set up if each entry in the drawing is rounded to the nearest integer
ROUND_ENTRY_TO_NEAREST_INT = True

template_spiral = {"innermost": [], "middle": [], "outermost": []}

prev_x_in, prev_y_in, prev_x_mid, prev_y_mid, prev_x_out, prev_y_out = -1, -1, -1, -1, -1, -1

for i in range(STEP): #100 steps within each of the 3 cycles
    distance = i * (CYCLE_RADIUS / STEP) #73 pixels per cycle in radius
    angle = i * (2 * pi / STEP) #2pi per cycle in angle
    # used to check if previous pixels are already in the drawing
    
    #innermost cycle
    new_pixel_x_in = drawing.START_POINT_X + distance * cos(angle)
    new_pixel_y_in = drawing.START_POINT_Y - distance * sin(angle)
    #middle cycle
    new_pixel_x_mid = drawing.START_POINT_X + (distance + CYCLE_RADIUS) * cos(angle)
    new_pixel_y_mid = drawing.START_POINT_Y - (distance + CYCLE_RADIUS) * sin(angle)
    #outermost cycle
    new_pixel_x_out = drawing.START_POINT_X + (distance + CYCLE_RADIUS*2) * cos(angle)
    new_pixel_y_out = drawing.START_POINT_Y - (distance + CYCLE_RADIUS*2) * sin(angle)

    if ROUND_ENTRY_TO_NEAREST_INT:
        new_pixel_x_in,  new_pixel_y_in  = round(new_pixel_x_in) , round(new_pixel_y_in)
        new_pixel_x_mid, new_pixel_y_mid = round(new_pixel_x_mid), round(new_pixel_y_mid)
        new_pixel_x_out, new_pixel_y_out = round(new_pixel_x_out), round(new_pixel_y_out)

    # add only pixels not already in the drawing, to test for offset calculation in main.py
    if not (prev_x_in == new_pixel_x_in and prev_y_in == new_pixel_y_in):
        template_spiral["innermost"].append({"x": new_pixel_x_in,  "y": new_pixel_y_in,  "timestamp":          i})
        prev_x_in, prev_y_in = new_pixel_x_in, new_pixel_y_in
    if not (prev_x_mid == new_pixel_x_mid and prev_y_mid == new_pixel_y_mid):
        template_spiral["middle"].append({   "x": new_pixel_x_mid, "y": new_pixel_y_mid, "timestamp":   STEP + i})
        prev_x_mid, prev_y_mid = new_pixel_x_mid, new_pixel_y_mid
    if not (prev_x_out == new_pixel_x_out and prev_y_out == new_pixel_y_out):
        template_spiral["outermost"].append({"x": new_pixel_x_out, "y": new_pixel_y_out, "timestamp": STEP*2 + i})
        prev_x_out, prev_y_out = new_pixel_x_out, new_pixel_y_out

full_spiral = template_spiral["innermost"] + template_spiral["middle"] + template_spiral["outermost"]

def render_spiral_as_png():
    drawing.Drawing.render_array_as_png(full_spiral, PATH, r=0, g=0, b=255, on_template=False)

# Write out template spiral as JSON file in style of drawing objects
def write_template_as_json():
    template_in_dict = {
        "time-uploaded":0,
        "coordinates": full_spiral,
        "userId":"Template",
        "dominantHand":"right",
        "drawnHand":"right",
        "isParkinsonPatient": False
    }
    template_in_json = json.dumps(template_in_dict)
    
    with open(TEMPLATE_JSON_PATH, "w") as file:
        file.write(template_in_json)

# render_spiral_as_png()
if __name__ == "__main__":
    write_template_as_json()