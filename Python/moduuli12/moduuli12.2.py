import requests

hakusana = input('Syötä paikkakunta: ')

pyynto = 'https://api.openweathermap.org/data/2.5/weather?q='+hakusana+'&appid=610be67330b23a33f27eb44fdab2443b'
vastaus = requests.get(pyynto).json()
print(vastaus['weather'][0]['main'])
print(str(round(int(vastaus['main']['temp'])-273.15,2)) + ' Celcius-astetta.')