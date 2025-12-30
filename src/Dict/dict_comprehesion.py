cities_in_F={'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_c={key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}

print(cities_in_c)


# using if condition

weather={'New York': "snowing",'Boston':"sunny",'Los Angeles':"sunny",'Chicago':"cloudy"}

sunny_weather={key: value for (key, value) in weather.items() if value=="sunny"}

print(sunny_weather)

cities={'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

desc_cities={key: ("WARM" if value>=40 else "COLD") for (key, value) in cities.items()}

print(desc_cities)