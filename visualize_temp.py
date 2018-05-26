import pandas as pd

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
