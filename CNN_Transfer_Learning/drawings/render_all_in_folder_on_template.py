"""
Code that renders every drawing JSON existing in a given folder onto a template spiral
with set colors. Useful to compare how dominant hand drawings look compared to 
non-dominant hands. 
"""

import os
from typing import List

from drawing import Drawing
TEMPLATE_JSON_PATH = "CNN_Transfer_Learning/drawings/templateSpiralJSON.json"

def render_all_in_folder_on_template(
        src_dir : str, 
        save_dir : str = ".",
        drawing_color : List[int] = [0, 0, 0],
        template_color : List[int] = [255, 0, 0],
        background_color : List[int] = [255, 255, 255],
        render_dominant : bool = None,
        template_on_top : bool = False
        ):
    """
    Renders all drawings stored as json data under the given directory with the color
    indicated as drawing_color, onto a template with color template_color.
    drawing_color & template_color are in RGB values.
    The rendered images are saved as png into save_dir.

    :param str src_dir: The directory in which all image data we render reside.
    :param str save_dir: The directory to which we save the obtained image.
    Defaults to the current directory.
    :param List[int] drawing_color: The color of the drawings we render, in RGB. 
    Defaults to [0, 0, 0].
    :param List[int] template_color: The color of the template we render, in RGB.
    Defaults to [255, 0, 0].
    :param List[int] background_color: The color of the background, in RGB.
    Defaults to [255, 255, 255].
    :param bool render_dominant: Whether to render only dominant hand images or not.
    If False, render only non-dominant images. If None, render all ignoring handedness.
    :param bool template_on_top: Whether to render the template on top of all images.
    If True, the template is rendered on top of all images. If False, the template is 
    rendered below all images.
    """
    # get the template and turn it into an array of pixel such that we can merge them 
    # using _merge_array_on_background from Drawing.
    template = Drawing(TEMPLATE_JSON_PATH)
    
    # render the template either as background or at the end
    if template_on_top:
        image_array = background_color*Drawing.WIDTH*Drawing.HEIGHT 
    else: 
        image_array = template.get_array_of_pixels(
            drawing_r=template_color[0], drawing_g=template_color[1], drawing_b=template_color[2],
             back_r=background_color[0],  back_g=background_color[1],  back_b=background_color[2]
            )
    
    # for every drawing
    for file in os.listdir(src_dir):
        # if file is not a json one, ignore
        # that is, if there exists an extension that is not json
        if not file.endswith("json") and "." in file : continue 
        
        full_path = src_dir + "/" + file
        drawing = Drawing(full_path)
        # skip or not depending on render_dominant
        if render_dominant: #then only render dominants
            if drawing.dominant_hand_is_right != drawing.drawn_hand_is_right: continue
        elif render_dominant == None: #then render all
            pass
        else: # otherwise, only render non-dominants
            if drawing.dominant_hand_is_right == drawing.drawn_hand_is_right: continue

        image_array = Drawing._merge_array_on_background(
            arr=drawing.drawing, 
            r=drawing_color[0], g=drawing_color[1], b=drawing_color[2], 
            background_array=image_array
            )

    # render the template at the top if template_on_top is True
    if template_on_top:
        image_array = Drawing._merge_array_on_background(
            arr=template.drawing, 
            r=template_color[0], g=template_color[1], b=template_color[2], 
            background_array=image_array
            )
        
    # finally, render obtained array into png
    handedness = "dom" if render_dominant else ("all" if render_dominant == None else "nondom")
    file_name = f"render_all_from_{src_dir.replace('/', '')}_" + handedness + ".png"
    Drawing._render_array_to_png(
        pixelArr=image_array, 
        out_path=save_dir + "/" + file_name
        )
    
    return image_array

if __name__ == "__main__":
    render_all_in_folder_on_template(
        src_dir="CNN_Transfer_Learning/drawings/top_21_shaky_dominant", 
        save_dir="CNN_Transfer_Learning/image_rendered", 
        drawing_color=[0,0,0], template_color=[255,0,255], background_color=[255,255,255],
        render_dominant=True,
        template_on_top=True
        )