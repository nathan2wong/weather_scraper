import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def weatherman(url):
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    seven_day = soup.find("ul", id="seven-day-forecast-list")
    forecast_items = seven_day.find_all("div", class_="tombstone-container")
    return forecast_items

def prediction(forecast_week):
    periods, short_descs, temp, img, desc = [],[],[],[],[]
    for day in forecast_week:
        try:
            periods.append(day.find(class_="period-name").get_text())
            short_descs.append(day.find(class_="short-desc").get_text())
            temp.append(day.find(class_="temp").get_text())
            img = day.find("img")
            desc.append(img['alt'])
        except AttributeError:
            print("error")

    weather = pd.DataFrame({
        "period": periods,
        "short-desc": short_descs,
        "temperature": temp,
        "description": desc
    })

    return weather

def weather_analysis(weather):
    temp_nums = weather["temperature"].str.extract("(?P<temp_num>\d+)", expand=False)
    weather["temp_num"] = temp_nums.astype('int')
    return weather["temp_num"].mean()

def generate_url():
    lat, lng = 37,-122
    while lat < 100:
        while lng < 100:
            yield lat, lng
            lng += .1
        lat += .1
        lng = -122

def create_url(loc_generator):
    sample_url = "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
    while True:
        try:
            lat, lng = next(loc_generator)
            mod_url = "http://forecast.weather.gov/MapClick.php?lat={0}&lon={1}".format(lat, lng)
            yield mod_url
        except StopIteration:
            print("Finished all lat and longs")
            return

if __name__ == "__main__":

    trial_condition = False
    if trial_condition:
        a = weatherman("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
        b = prediction(a)
        c = weather_analysis(b)
        print("Pandas table: {0}".format(b))
        print("Mean temperature: {0}".format(c))

    i = 0
    url_gen = create_url(generate_url())
    while i < 100:
        try:
            url = next(url_gen)
            construct = weatherman(url)
            weeklong = prediction(construct)
            analysis = weather_analysis(weeklong)
            print("url: {0}\nweeklong: {1}\n\n\nmean: {2}".format(url, weeklong, analysis))
            i += 1
        except StopIteration as e:
            print(e)
        except ValueError as e:
            print(e)
        except:
            print("Unknown error at {0}".format(i))
