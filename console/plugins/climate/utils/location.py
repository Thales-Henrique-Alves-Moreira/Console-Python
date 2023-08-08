from .request import request

def geoLoc(commandLine):
    print(location().getGeoLocation())

def ip(commandLine):
    print(location().getIp())

def city(commandLine):
    print(location().getCity())

def address(commandLine):
    print(location().getAddress())


class location(request):
    def __init__(self):
        self.getLocInfo()

    def getLocInfo(self):
        info = self.getRequest("https://ipinfo.io/json", "json")

        self.geoLocation = info["loc"]
        self.city = info["city"]
        self.region = info["region"]
        self.country = info["country"]
        self.ip = info["ip"]
        self.address = "{}, {}, {}".format(info["city"], info["region"], info["country"])

    def getGeoLocation(self):
        return self.geoLocation

    def getIp(self):
        return self.ip

    def getCity(self):
        return self.city

    def getAddress(self):
        return self.address

    def getRegion(self):
        return self.region

    def getCountry(self):
        return self.country