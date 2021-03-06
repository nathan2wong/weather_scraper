from weatherman import *
from url_generator import *
from visualize_temp import *
import datetime

NUMBER_OF_SCRAPES = 1000
CURRENT_TIME = datetime.datetime.now()

def scrape_weather():
    print("\n\n\n\n")
    i = 0
    url_gen = create_url(generate_url())
    aggregate_temp = []
    while i < NUMBER_OF_SCRAPES:
        try:
            url = next(url_gen)
            construct = weatherman(url)
            weeklong = prediction(construct)
            analysis = mean_temperature(weeklong[2])
            #print("url: {0}\nweeklong: {1}\n\nmean: {2}".format(url, weeklong, analysis))
            aggregate_temp.append(weeklong[2])
            if i % 5 == 0:
                mean_total_temp = mean_temperature(aggregate_temp[i])
                #print("\n\n\n Mean tempeature so far: {0}".format(mean_total_temp))
            print("Iterations so far: {0}".format(i))
            i += 1
        except AttributeError as e:
            print(e)
            print("\n\n\n Page not found probably")
            i+=1
        except:
            print("Unknown error at {0}".format(i))
            i+= 1
    return aggregate_temp

if __name__ == "__main__":
    aggregate_temp = scrape_weather()
    for place in aggregate_temp:
        for i in range(len(place)):
            place[i] = extract_digits(place[i])
    daily_mean_temps = format_data(aggregate_temp)
    save_csv(daily_mean_temps, "./data/{0}-scrape_weather-{1}.csv".format(NUMBER_OF_SCRAPES, CURRENT_TIME))
    visualize_data(daily_mean_temps, "./data/visualizations/{0}-temp_visualization-{1}.html".format(NUMBER_OF_SCRAPES, CURRENT_TIME))
