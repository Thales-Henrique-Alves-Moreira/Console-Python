import json
from prettytable import PrettyTable

def readConfigs(commandLine):
    config.readConfigs()

def readOneConfig(commandLine):
    name = commandLine.split()[1]

    config.readOneConfig(name)

def delConfig(commandLine):
    name, attr = commandLine.split()[1], commandLine.split()[2]

    config.delConfig(name, attr)

def setConfig(commandLine):
    name, attr, value = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]

    config.setConfig(name, attr, value)

def updateConfig(commandLine):
    name, attr, value = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]
    
    config.updateConfig(name, attr, value)

def showConfig(commandLine):
    name, attr = commandLine.split()[0], commandLine.split()[1]

    config().showConfig(name, attr)

class config():
    def readConfigs():
        with open("console/config.json", 'r') as cjson:
            config = json.load(cjson)

        for i in range(len(config)):
            print("\n" + config[i]["name"] + "\n")

            table = PrettyTable(["setting", "value"])

            for key, value in config[i]["config"].items():
                table.add_row([key, value])
            
            print(table)

    def readOneConfig(name):
        with open("console/config.json", 'r') as cjson:
            config = json.load(cjson)

        for i in range(len(config)):
            if config[i]["name"] == name:
                print(f"\n{name}\n")
                table = PrettyTable(["setting", "value"])

                for key, value in config[i]["config"].items():
                    table.add_row([key, value])

                print(table)
                return

        print("Choose a valid setting name")

    def delConfig(name, attr):
        with open("console/config.json") as cjson:
            config = json.load(cjson)

        index = 0

        for i in range(len(config)):
            if config[i]["name"] == name:
                index = i
                break

        del config[index]["config"][attr]
        
        with open("console/config.json", "w") as cjson:
            json.dump(config, cjson, indent=2)

    def setConfig(name, attr, value):
        with open("console/config.json", 'r') as cjson:
            config = json.load(cjson)

        index = 0

        for i in range(len(config)):
            if config[i]["name"] == name:
                index = i
                break

        config[index]["config"].update({attr: value})

        with open("console/config.json", "w") as cjson:
            json.dump(config, cjson, indent=2)


    def updateConfig(name, attr, value):
        with open("console/config.json") as cjson:
            config = json.load(cjson)

        index = 0

        for i in range(len(config)):
            if config[i]["name"] == name:
                index = i
                break

        config[index]["config"][attr] = value

        with open("console/config.json", "w") as cjson:
            json.dump(config, cjson, indent=2)

    def getConfig(self, name, attr):
        with open("console/config.json", 'r') as cjson:
            config = json.load(cjson)

        for i in range(len(config)):
            if config[i]["name"] == name:
                for keys in config[i]["config"].keys():
                    if keys == attr:
                        attrValue = config[i]["config"][attr]
                        return attr, attrValue

    def showConfig(self, name, attr):
        attribute, attrValue = self.getConfig(name, attr)
        
        table = PrettyTable(["Setting", "Value"])
        table.add_row([attribute, attrValue])

        print(table)