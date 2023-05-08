
from genericpath import isfile
import os

from math import fabs
import png;
import json;

# Path to the folder holding the handdrawing data
SOURCE_PATH = "./Anonimized_data/all_data/useful"

# Path to the folder to which images are rendered
GOAL_PATH = "./CNN_Transfer_Learning/image_rendered"

"""
REX Python file for reading json data and redering it into drawings.

The data is given as JSON objects storing coordinates of x and y the mouse covered, 
combined with the time at which the mouse covered it.
The class looks at x and y coordinates, and given the default size of the drawing picture,
renders it into a PNG.

"""

WIDTH, HEIGHT = 600, 475  #determined initially from website

class RenderDrawing():

    """
    Render drawing from data by:
    1) Reading the JSON data into an array of pixels which has been covered 
       (each pixel is an array of 3 values, R, G, B)
    2) Render a whole image out of the JSON object's dimension and 
       determining color values to each pixel based on whether the pixel has been covered
       (the whole image is an array of int, obtained by flattening rows of the image, 
       which in turn are array of pixels that is flattened, where each pixel is the 3 value [R, G, B];
       so a black image of 2 * 3 pixels with the bottom right pixel being red is shown as:
       [0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 255, 0, 0])
    2) Render the pixels by giving it to the png module.
    """

    def readJSON(self, filePath : str):
        """
        Reads the array of pixels from the given json file.

        :param str filePath: Path to json file to be read.
        """
        with open(filePath, 'r') as file:
            fileContent = file.read()
            readJsonArray = json.loads(fileContent)

        self.drawingName = str(readJsonArray["time-uploaded"])

        self.wb_arrayDrawing = [0, 0, 0]*WIDTH*HEIGHT
        self.red_on_white_arrayDrawing = [255,255,255]*WIDTH*HEIGHT

        red_pixel = [255, 0, 0]
        white_pixel = [255, 255, 255]

        for pixel in readJsonArray["coordinates"]:
            x = int(pixel["x"])
            y = int(pixel["y"])
            p_red   = y * WIDTH * 3 + x * 3 + 0
            p_green = y * WIDTH * 3 + x * 3 + 1
            p_blue  = y * WIDTH * 3 + x * 3 + 2

            self.wb_arrayDrawing[p_red] = white_pixel[0]
            self.wb_arrayDrawing[p_green] = white_pixel[1]
            self.wb_arrayDrawing[p_blue] = white_pixel[2]

            self.red_on_white_arrayDrawing[p_red] = red_pixel[0]
            self.red_on_white_arrayDrawing[p_green] = red_pixel[1]
            self.red_on_white_arrayDrawing[p_blue] = red_pixel[2]
        
        #print("readJSON SUCCESSFUL!")


    def render(self, render_mode : str):
        """
        Renders picture currently read with name taken from the file name,
        either red_on_white or white_on_black; or raise exception if no picture 
        has been read so far.

        :param str render_mode: Designates the picture to be rendered:
        red on white if "red_on_white", otherwise white on black.
        :raises Exception: Indicates render was called without json drawing read by the 
        class yet. 
        """
        if render_mode == "red_on_white":
            written_arr = self.red_on_white_arrayDrawing
            r_mode_name = "_rw"

        else:
            written_arr = self.wb_arrayDrawing
            r_mode_name = "_wb"

        if (written_arr != None):
            writer = png.Writer(width=WIDTH, height=HEIGHT, greyscale=False)
            with open(GOAL_PATH + "/" + self.drawingName + r_mode_name + ".png", 'bw') as goalFile: 
                writer.write_array(goalFile, written_arr)
            #print("RENDER SUCCESSFUL!")
        else:
            raise Exception("render has been called without json drawing read by the class") 


def renderAllInFolder(folder : str, render_mode : str):
    rd = RenderDrawing()

    allInDir = os.listdir(folder)
    for p in allInDir:
        fullPath = folder + "/" + p
        if os.path.isfile(fullPath):
            rd.readJSON(fullPath)
            rd.render(render_mode=render_mode)
    
    print("RENDER ALL SUCCESSFUL!")

if __name__ == "__main__":
    renderAllInFolder(SOURCE_PATH, "white_on_black")

