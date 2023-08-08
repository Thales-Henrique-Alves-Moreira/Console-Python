import json
from prettytable import PrettyTable
import glob
import os
from pathlib import Path

def readAllConfigs(commandLine):
    config().readAllConfigs()

def readModuleConfig(commandLine):
    module = commandLine.split()[1]

    config().readModuleConfig(module)

def delConfig(commandLine):
    name, attr, module = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]

    config().delConfig(name, attr)

def setConfig(commandLine):
    name, attr, value = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]

    config().setConfig(name, attr, value)

def updateConfig(commandLine):
    name, attr, value = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]
    
    config().updateConfig(name, attr, value)

def showConfig(commandLine):
    name, attr = commandLine.split()[0], commandLine.split()[1]

    config().showConfig(name, attr)

class config():
    def readAllConfigs():
        config = []

        with open(os.path.dirname(os.path.realpath(__file__)) + "/main-config.json", 'r') as cjson:
            config.append(json.load(cjson))

        plugins = glob.glob(str(Path(os.path.dirname(__file__)).parent.absolute()) + "\\plugins\\*\\", recursive=True)

        del plugins[len(plugins) - 1]

        for plugin in plugins:
            with open(f"{plugin}/config.json", 'r') as cjson:
                config.append(json.load(cjson))

        for i in range(len(config)):
            print("\n" + config[i]["name"] + "\n")

            table = PrettyTable(["setting", "value"])

            for key, value in config[i]["config"].items():
                table.add_row([key, value])
            
            print(table)

    def readModuleConfig(module):
        config = ""

        if module == "main":
            with open(os.path.dirname(os.path.realpath(__file__)) + "/main-config.json", 'r') as cjson:
                config = json.load(cjson)

        else:
            with open((str(Path(os.path.dirname(__file__)).parent.absolute())) + f"\\plugins\\{module}\\config.json", 'r') as cjson:
                config = json.load(cjson)

        print(f"\n{module}\n")
        table = PrettyTable(["setting", "value"])

        for key, value in config["config"].items():
            table.add_row([key, value])

        print(table)
        return

        print("Choose a valid setting name")

    def delConfig(module, name, attr):
        config = ""

        if module == "main":
            with open(os.path.dirname(os.path.realpath(__file__)) + "/main-config.json", 'r') as cjson:
                config = json.load(cjson)

        else:
            with open((str(Path(os.path.dirname(__file__)).parent.absolute())) + f"\\plugins\\{module}\\config.json", 'r') as cjson:
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