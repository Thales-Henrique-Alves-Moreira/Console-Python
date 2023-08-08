# ao invés de fazer a comunicação no próprio console,
# poderia abrir uma outra aplicação na qual faria isso
#   ^
#   |
#   |
# chorão

import socket
from threading import Thread

listening = False
hosting = False

threadListening = Thread()
threadHosting = Thread()

name = ""

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hoster = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

amHost = False

clients = {}

def startHost(commandLine):
    commandLine = commandLine.split(" ")
    del commandLine[0]

    global name
    ipPort, name = commandLine

    threadHosting.target = host
    threadHosting.args = [ipPort, name]
    threadHosting.start()
    
    threadListening.target = listen
    threadListening.args = [ipPort, name]

def host(host, name):
    ip, port = host.split(":")

    global hoster

    hoster.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    hoster.bind((ip, port))
    hoster.listen()

    while True:
        clientsocket, address = hoster.accept()

def listen(host, name):
    ip, port = host.split(":")

    global listener

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.connect((ip, port))

def msg(commandLine):
    global hoster
    global listener
    
    if amHost:
        hoster.send()
    else:
        listener.send()

def endHost(commandLine):
    pass

def stopListening(commandLine):
    pass