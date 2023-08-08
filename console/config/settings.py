from .config import config

def readAllConfigs(commandLine):
    config().readAllConfigs()

def readModuleConfig(commandLine):
    module = commandLine.split()[1]

    config().readModuleConfig(module)

def delConfig(commandLine):
    name, attr, module = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]

    config().delConfig(module, name, attr)

def setConfig(commandLine):
    name, attr, value = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]

    config().setConfig(name, attr, value)

def updateConfig(commandLine):
    name, attr, value = commandLine.split()[1], commandLine.split()[2], commandLine.split()[3]
    
    config().updateConfig(name, attr, value)

def showConfig(commandLine):
    name, attr = commandLine.split()[0], commandLine.split()[1]

    config().showConfig(name, attr)