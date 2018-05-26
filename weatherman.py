import requests
from bs4 import BeautifulSoup as bs

def extract_digits(str_input):
    return [int(s) for s in str_input.split() if s.isdigit()][0]

def weatherman(url):
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    if soup.find("span", class_="big") is not None:
        return None
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

    weather = [periods, short_descs, temp, desc]
    return weather

def mean_temperature(temps):
    mean_temp = 0.0
    for daily_temp in temps:
        mean_temp += float(extract_digits(daily_temp))
    mean_temp = mean_temp/len(temps)
    return mean_temp
