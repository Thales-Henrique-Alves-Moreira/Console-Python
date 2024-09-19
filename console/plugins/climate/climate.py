from .utils.location import location
from .utils.request import request

def temperature(commandLine):
    temp, feelsLike, tempMin, tempMax = climate().getTemp()

    print(f"The temperature for today is {temp} °C and the feels like is {feelsLike} °C. The max temperature for today is {tempMax} °C and the minimum temperature for today is {tempMin} °C")

def weather(commandLine):
    weather, weatherDescription = climate().getWeather()

    print(f"Today's weather is {weather.lower()}, but a better description would be: {weatherDescription}")


class climate(location, request):
    def __init__(self):
        super().__init__()
        self.TOKEN = "token"
        self.location = self.getGeoLocation().split(',')

        self.getInfo()

    def getInfo(self):
        info = self.getRequest(f'https://api.openweathermap.org/data/2.5/weather?lat={self.location[0]}&lon={self.location[1]}&units=metric&lang=pt-BR&appid={self.TOKEN}', 'json')

        self.temp = info["main"]["temp"]
        self.feelsLike = info["main"]["feels_like"]
        self.tempMin = info["main"]["temp_min"]
        self.tempMax = info["main"]["temp_max"]

        self.weather = info["weather"][0]["main"]
        self.weatherDescription = info["weather"][0]["description"]


    def getTemp(self):
        return self.temp, self.feelsLike, self.tempMin, self.tempMax

    def getWeather(self):
        return self.weather, self.weatherDescription
