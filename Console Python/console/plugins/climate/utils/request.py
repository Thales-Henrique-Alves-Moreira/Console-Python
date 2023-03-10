import requests

def getReq(commandLine):
    link, type = commandLine.split(' ')[1], commandLine.split(' ')[2]

    print(request().getRequest(link, type))

class request():
    def getRequest(self, link, type):
        res = requests.get(link)

        if type == "json":
            return res.json()
        elif type == "text":
            return res.text
        else:
            print("Error! You must choose a valid type of request response.")
