
from genericpath import isfile
import os

from math import fabs
import png;
import json;

"""
Two things to do first and then run this scipt:
1) Change the folderPath to the path in which the handrawing data is held
2) Change the GOAL_FILE_PATH in RenderDrawing to the path that you are aiming to render the images into
"""
#Put the path to the folder that holds the handdrawing data
folderPath = "C:\\Users\\mashi\\Downloads\\REX\\Hand drawing data\\data"

#Change this path to the folder that you are aiming to render the images into
GOAL_FILE_PATH = "C:\\Users\\mashi\\Desktop\\VisualStudioCode\\python\\DominantHandDrawing\\renderedDrawings"

"""
REX Python file for reading json data and redering it into drawings.

The data is given as JSON objects storing coordinates of x and y the mouse covered, 
combined with the time at which the mouse covered it.
The class looks at x and y coordinates, and given the default size of the drawing picture,
renders it into a PNG.

"""


WIDTH = 600  #determined initially from website
HEIGHT = 475 #determined initially from website
NON_DRAWING_PIXEL = [255,255,255]
DRAWING_PIXEL = [255,0,0]

class RenderDrawing():
    arrayDrawing = None
    drawingName = ""

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

    #Reads the array of pixels from the json file given
    def readJSON(self, filePath):
        with open(filePath, 'r') as file:
            fileContent = file.read()
            readJsonArray = json.loads(fileContent)

        self.drawingName = str(readJsonArray["time-uploaded"])

        self.arrayDrawing = NON_DRAWING_PIXEL *WIDTH *HEIGHT

        for pixel in readJsonArray["coordinates"]:
            x = int(pixel["x"])
            y = int(pixel["y"])
            self.arrayDrawing[y * WIDTH * 3 + x * 3 + 0] = DRAWING_PIXEL[0]
            self.arrayDrawing[y * WIDTH * 3 + x * 3 + 1] = DRAWING_PIXEL[1]
            self.arrayDrawing[y * WIDTH * 3 + x * 3 + 2] = DRAWING_PIXEL[2]
        
        #print("readJSON SUCCESSFUL!")


    #Renders picture currently read with its given name, or raise exception if no picture read 
    def render(self):
        if (self.arrayDrawing != None):
            writer = png.Writer(width=WIDTH, height=HEIGHT, greyscale=False)
            with open(GOAL_FILE_PATH + "\\" + self.drawingName + ".png", 'bw') as goalFile: 
                writer.write_array(goalFile, self.arrayDrawing)
            #print("RENDER SUCCESSFUL!")
        else:
            raise Exception("render has been called without json drawing read by the class") 




def main(p):
    rd = RenderDrawing()
    print("INSTANTIATION SUCCESSFUL!")
    rd.readJSON(p)
    print("readJSON SUCCESSFUL!")
    rd.render()
    print("RENDER SUCCESSFUL!")

def renderAllInFolder(folder):
    rd = RenderDrawing()

    allInDir = os.listdir(folder)
    for p in allInDir:
        fullPath = folder + "\\" + p
        if os.path.isfile(fullPath):
            rd.readJSON(fullPath)
            rd.render()
    
    print("RENDER ALL SUCCESSFUL!")

#main(filePath)
renderAllInFolder(folderPath)

