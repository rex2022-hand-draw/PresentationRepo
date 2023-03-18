from cmath import sqrt
import readjson

"""
Takes a json file holding drawing dataOld in pixels of 
[x, y, timestamp]
and returns a time series of the drawing speed between 
each pairs of pixel in the drawing.
"""


def draw_speed(x1, x2, y1, y2, t1, t2):
    if t2 - t1 != 0:
        return (sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) / (t2 - t1)
    else:
        return 0

def return_time_series(json_path):
    drawing_pixels = readjson.readJSON(json_path)
    time_series = []
    if len(drawing_pixels) == 0:
        return []
    prev_p = drawing_pixels[0]

    for pixel in drawing_pixels[1:]:
        x = pixel["x"]
        y = pixel["y"]
        ts = pixel["timestamp"]

        prev_x = prev_p["x"]
        prev_y = prev_p["y"]
        prev_ts = prev_p["timestamp"]

        time_series.append(
            draw_speed(prev_x, x, prev_y, y, prev_ts, ts)
        )

        prev_p = pixel
    return time_series