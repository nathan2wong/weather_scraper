def generate_url():
    lat, lng = 37,-122
    while lat < 100:
        while lng < 100:
            yield lat, lng
            lng += 0.05
        lat += 0.05
        lng = -122

def create_url(loc_generator):
    sample_url = "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
    first_url = "http://forecast.weather.gov/MapClick.php?lat=37&lon=-122"
    while True:
        try:
            lat, lng = next(loc_generator)
            mod_url = "http://forecast.weather.gov/MapClick.php?lat={0}&lon={1}".format(lat, lng)
            yield mod_url
        except StopIteration:
            print("Finished all lat and longs")
