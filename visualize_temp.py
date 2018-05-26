import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show, save
import random

HEXCODE = "ABCDEF"
NUM = [1,2,3,4]

def avg(*args):
    total_val, i = 0,0
    for arg in args:
        total_val += float(arg)
        i+=1
    return total_val/i

def format_data(input_array):
    arr = input_array[:][:]
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]) - 1:
            if arr[i][j] > arr[i][j+1]:
                arr[i][j] = avg(arr[i][j], arr[i].pop(j+1))
            j += 1
        arr[i] = list(filter(lambda x : isinstance(x, float),arr[i]))
        i += 1
    arr = list(filter(lambda x: len(x) > 0, arr))
    return arr


def save_csv(input_array, filename="weather_scraper.csv"):
    download_file = pd.DataFrame(input_array)
    download_file.to_csv("{0}".format(filename))
    print("Saved as csv as {0}".format(filename))

def visualize_data(input_array, filename="weather.html"):
    TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select,save"
    p = figure(tools=TOOLS, x_axis_label = 'day from today', x_range=(-0.5, 3.5), y_axis_label = 'temperature in F', y_range=(40, 90))
    for arr in input_array:
        x = []
        for i in range(len(arr)):
            x += [i]
        y = np.array(arr)
        x = np.array(x)
        color = "#{0}{1}{2}{3}".format(random.choice(HEXCODE),int(arr[1]),int(arr[2]), random.choice(HEXCODE))
        p.scatter(x, y, radius=0.1, fill_color=color, fill_alpha=0.6, line_color=color)
    output_file(filename, title="color-scatter-temperature")
    save(p)
