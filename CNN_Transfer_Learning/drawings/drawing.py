"""
Converts json of drawing data into drawing object which are easier to use.
"""

import copy
import json
from typing import List
import png

WIDTH, HEIGHT = 600, 475 #determined initially from website
NON_DRAWING_PIXEL = [255,255,255]
DRAWING_PIXEL = [255,0,0]
START_POINT_X = 282
START_POINT_Y = 197 #197.39999961853027
END_POINT_X = 282 + (355 - 282) * 3
END_POINT_Y = 197 #197.39999961853027

BACKGROUND = NON_DRAWING_PIXEL * WIDTH * HEIGHT

TEMPLATE_PATH = "./image_rendered/reference_spiral.png"

class Drawing:

    def __init__(self, file_path : str = None):
        """
        Initializes a drawing object, reading the given file path if any.
        The json data is read and the following are set:
        - time of upload
        - user id
        - the drawing, as array of pixels
        - a boolean indicating if the dominant hand is right
        - a boolean indicating if the drawing hand is right
        - a boolean indicating if the drawer is diagonsed with Parkinson's disease

        :param str file_path: The file path from which we read the drawing, initialized
        to nothing if not given.
        """
        self.time_uploaded = ""
        self.user_id = " "
        self.drawing = {}
        self.dominant_hand_is_right = False
        self.drawn_hand_is_right = False
        self.is_parkinson_patient = False

        if file_path:
            self.read_json(file_path)

    def read_json(self, file_path : str):
        """
        Reads the array of pixels from the given json file path to update 
        the attributes of this drawing.

        :param str file_path: The file path from which we read the drawing.
        """
        with open(file_path, 'r') as file:
            file_content = file.read()
            read_json_array = json.loads(file_content)

        self.time_uploaded = str(read_json_array["time-uploaded"])
        self.user_id = read_json_array["userId"]
        self.drawing = read_json_array["coordinates"]
        self.dominant_hand_is_right = (read_json_array["dominantHand"] == "right")
        self.drawn_hand_is_right = (read_json_array["drawnHand"] == "right")
        self.is_parkinson_patient = (read_json_array["isParkinsonPatient"])

        #print("readJSON SUCCESSFUL!")

    def write_json(self, file_path : str):
        """
        Writes the current drawing array of pixels into the given file path as json,
        creating a file of the given name if it is not there.

        :param str file_path: The file path to which we write the drawing.
        """

        dict_to_convert = {
            "time-uploaded" : self.time_uploaded,
            "userId" : self.user_id,
            "coordinates" : self.drawing,
            "dominantHand" : "right" if self.dominant_hand_is_right else "left",
            "drawnHand" : "right" if self.drawn_hand_is_right else "left",
            "isParkinsonPatient" : self.is_parkinson_patient
        }

        with open(file_path, 'w') as file:
            json_dict = json.dumps(dict_to_convert)
            file.write(json_dict)
        
        #print("writeJSON SUCCESSFUL!")

    def round_coordinates(self):
        """
        Rounds the coordinates for every pixel that is part of the current 
        drawing using the built-in python round() function.
        Potentially used to normalize drawing data collected to nearest integer
        first before doing calculation (although it might not be truly needed)
        """
        for pixel in self.drawing:
            pixel["x"] = pixel["x"].round()
            pixel["y"] = pixel["y"].round()

    @staticmethod
    def _change_pixel_color_at(
        drawing : List[int], 
        x : int, y : int, 
        r : int = None, g : int = None, b : int = None, 
        pixel : List[int] = None
        ):
        """
        Change pixel color of given (x, y) coordinate to one of the given r, g and b colors
        or given pixel color. Does nothing if coordinate is off the array's index.

        :param List[int] drawing: An array of RGB pixels as array of three integers.
        :param int x: The x coordinate of the pixel to change.
        :param int y: The y coordinate of the pixel to change.
        :param int r: The pixel's new red value.
        :param int g: The pixel's new green value.
        :param int b: The pixel's new blue value.
        :param List[int] pixel: A pixel with three integers for RGB.
        """

        if (len(drawing) >= (y * WIDTH * 3 + x * 3 + 2)):
            if ((r==None or g==None or b==None) and pixel==None):
                return
            elif (r==None or g==None or b==None):
                drawing[y * WIDTH * 3 + x * 3 + 0] = pixel[0]
                drawing[y * WIDTH * 3 + x * 3 + 1] = pixel[1]
                drawing[y * WIDTH * 3 + x * 3 + 2] = pixel[2]
            else: # pixel==None
                drawing[y * WIDTH * 3 + x * 3 + 0] = r
                drawing[y * WIDTH * 3 + x * 3 + 1] = g
                drawing[y * WIDTH * 3 + x * 3 + 2] = b

    # Merges given array with background array and returns it 
    @staticmethod
    def _merge_array_on_background(arr, 
        r=DRAWING_PIXEL[0], g=DRAWING_PIXEL[1], b=DRAWING_PIXEL[2],
        background_path=None, background_array=None):

        # print("_merge_array_on_background_1: ", arr)
        
        if background_path: #if given with path to background PNG
            _, _, rgb_iter, _ = png.Reader(TEMPLATE_PATH).asRGB()
            background = []
            for rgb_row in rgb_iter:
                background += rgb_row
        elif background_array: #if given background PNG as RGB arrays
            background = background_array
        else:
            background = copy.deepcopy(BACKGROUND)
        
        # print("_merge_array_on_background_2: ", background)

        if arr: # executes if array is not empty list of dict
            for pixel in arr:
                x = int(pixel["x"])
                y = int(pixel["y"])
                Drawing._change_pixel_color_at(background, x, y, pixel=[r,g,b])    

        # print("_merge_array_on_background_3: ", background)    
        
        return background

    @staticmethod
    def _render_array_to_png(pixelArr, out_path):
        if pixelArr: # executes if array is not empty list of dict
            
            # print("_render_array_to_png: ", pixelArr)
            
            writer = png.Writer(width=WIDTH, height=HEIGHT, greyscale=False)
            with open(out_path, 'bw') as goal_file: 
                writer.write_array(goal_file, pixelArr)
            #print("RENDER SUCCESSFUL!")
        else:
            raise Exception("render has been called without json drawing read by the class")

    @staticmethod
    def render_array_as_png(arr, out_path, 
        r=DRAWING_PIXEL[0], g=DRAWING_PIXEL[1], b=DRAWING_PIXEL[2], 
        on_template=False):
        if arr: # executes if array is not empty list of dict
            
            # print("renderArrayAsPNG_1: ", arr)

            if on_template: # render image on template image found at TEMPLATE_PATH
                png_array = Drawing._merge_array_on_background(arr, background_path=TEMPLATE_PATH)
            else:
                png_array = Drawing._merge_array_on_background(arr)
            
            # print("renderArrayAsPNG_2: ", png_array)

            Drawing._render_array_to_png(png_array, out_path)
        else:
            raise Exception("render has been called without json drawing read by the class")


    def render_as_png(self, png_path, r=DRAWING_PIXEL[0], g=DRAWING_PIXEL[1], 
        b=DRAWING_PIXEL[2], on_template=False):
        
        # print("renderAsPNG: ", self.drawing)
        Drawing.render_array_as_png(self.drawing, png_path, r, g, b, on_template)



    def render_as_png_with_distinct_cycle_color(self, png_path, 
        colors=[[255,0,0],[0,255,0],[0,0,255]], on_template=False):
        
        cycles = Drawing.divide_to_cycles(self)
        png_array = copy.deepcopy(BACKGROUND)

        if on_template: # render image on template image found at TEMPLATE_PATH
            png_array = Drawing._merge_array_on_background([], background_path=TEMPLATE_PATH)

        for i in range(len(cycles)):
            cycle = list(cycles.values())[i]
            cl = len(colors)
            png_array = Drawing._merge_array_on_background(cycle, 
                r=colors[i%cl][0], g=colors[i%cl][1], b=colors[i%cl][2], 
                background_array=png_array)
        
        Drawing._render_array_to_png(png_array, png_path)
        
    def get_array_of_pixels(self, 
                            drawing_r : int, drawing_g : int, drawing_b : int,
                            back_r    : int, back_g    : int, back_b    : int):
        """
        Returns an array representing the current drawing with the given RGB values
        for the drawing pixels and background pixels.

        :param int drawing_r: R value of drawing pixels.
        :param int drawing_g: G value of drawing pixels.
        :param int drawing_b: B value of drawing pixels.
        :param int back_r: R value of background pixels.
        :param int back_g: G value of background pixels.
        :param int back_b: B value of background pixels.
        :return List[List[List[int]]]: The array representing the current drawing with
        given colors.
        """
        def check_if_valid_rgb_val(val):
            try: val = int(val) 
            except: raise Exception(f"The entry {str(val)} has to be an integer!")
            if 0 > val or 255 < val: 
                raise Exception(f"The entry {str(val)} has to be between 0 and 255!")
        
        # first check that the entries are within the valid ranges.
        for inp in [drawing_r, drawing_g, drawing_b, back_r, back_g, back_b]:
            check_if_valid_rgb_val(inp)
        # make the background
        back = [back_r, back_g, back_b] * WIDTH * HEIGHT
        # change colors of that background for the drawing pixels in self.drawing
        for pixel in self.drawing:
            x, y = int(pixel["x"]), int(pixel["y"])
            Drawing._change_pixel_color_at(drawing=back, x=x, y=y, 
                                                  r=drawing_r, g=drawing_g, b=drawing_b)
        
        return back

    # Divide drawing into individual cycles and return a dict after division
    # Function assumes drawing as drawn from center to outside, but can deal with 
    # situation where it is written in the exact opposite manner too (from outside to center)
    # GOTTA WORK ON CREATING A METHOD WHICH RELIABLY DIVIDES ANY DRAWING INTO ITS CYCLES
    # CURRENTLY NOT ROBUST ENOUGH FOR VERY SHAKY HAND DRAWINGS
    @staticmethod
    def divide_to_cycles(drawing_obj=None):
        to_be_returned = {"innermost" : [], "middle" : [], "outermost" : []}
        d = drawing_obj.drawing
        #if last pixel to the right of first pixel, written inside out; if not, the otherway around
        if (d[0]["x"] > d[-1]["x"]):
            d.reverse()

        firstPixelX = d[0]["x"]
        firstPixelY = d[0]["y"]
        previousPixel = d[0]
        previousBoundaryPixelPos = 0
        # counts times we cross boundary at y = firstPixelY in drawing in time order
        # and when at the right of firstPixelX
        count = 0
         
        current_cycle = "innermost" #tracks key for which part of drawing we currently are in

        for i in range(len(d)):
            pixel = d[i]
            # If boundary is crossed from below to above, and to the right of starting point of drawing
            if ( (previousPixel["y"] > firstPixelY and pixel["y"] <= firstPixelY)
                and (pixel["x"] > firstPixelX)
                and (previousBoundaryPixelPos <= i - 30) ): # two boundaries are reasonably distanced (30 pixels for now)
                    count += 1
                    previousBoundaryPixelPos = i
            
            if (count == 1):
                current_cycle = "middle"
            elif (count == 2):
                current_cycle = "outermost"
            # otherwise count is 0

            to_be_returned[current_cycle].append(pixel)
            previousPixel = pixel

        return to_be_returned
    
if __name__ == "__main__":
    d = Drawing("model/templateSpiralJSON.json")
    d.render_as_png_with_distinct_cycle_color("model/template_tricolor.png")