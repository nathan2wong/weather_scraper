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


if __name__ == "__main__":
    a = weatherman("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
    b = prediction(a)
    c = weather_analysis(b)
    print("Pandas table: {0}".format(b))
    print("Mean temperature: {0}".format(c))
