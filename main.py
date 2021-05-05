import json
import os
import web
import requests
from dotenv import load_dotenv

urls = (
    '/zipcode=(.*),country=(.*)', 'WeahterByZipcode',
    '/(.*)', 'WeahterByCityname',
)

app = web.application(urls, globals())

class WeahterByZipcode:
    def GET(self, zipcode, countrycode):
        load_dotenv()
        apiKey = os.getenv('appkey')

        if isinstance(zipcode, int):
            r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip={zip},{country}&appid={appkey}&lang=fr&units=metric".format(zip=zipcode, country=countrycode, appkey=apiKey))
            weatherInfo = r.json()
            weatherDisplay = []
            weatherDisplay.append([weatherInfo["weather"]])
            weatherDisplay.append([weatherInfo["main"]])
            weatherDisplay.append([weatherInfo["sys"]])

            return weatherDisplay
        else:
            return "zipcode is not a number"


        return weatherDisplay

class WeahterByCityname:
    def GET(self, cityname):
        load_dotenv()  # On charge le fichier .env pour récupérer l'appkey qui est stocké dedans
        apiKey = os.getenv('appkey') # On attribut à la variable apiKey la value qu'il y a dans appkey dans le .env

        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appkey}&lang=fr&units=metric".format(appkey=apiKey, city=cityname))
        weatherInfo = r.json() # On attribut à la variable data le JSON de la request
        print(json.dumps(weatherInfo, indent=2)) # Dans la console ca affiche le JSON proprement
        # print(data)
        weatherDisplay = []
        weatherDisplay.append([weatherInfo["weather"]])
        weatherDisplay.append([weatherInfo["main"]])
        weatherDisplay.append([weatherInfo["sys"]])

        return weatherDisplay



if __name__ == "__main__":
    app.run()
