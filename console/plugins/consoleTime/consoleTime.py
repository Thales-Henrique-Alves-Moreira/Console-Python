import time

def curtime(commandLine):
    print(consoleTime().curtime())

def curdate(commandLine):
    print(consoleTime().curdate())

def curdatetime(commandLine):
    print(consoleTime().curdatetime())

class consoleTime:
    def __init__(self):
        self.curHour = time.localtime().tm_hour
        self.curMin = time.localtime().tm_min
        self.curSec = time.localtime().tm_sec
        self.curWeekDay = time.localtime().tm_wday
        self.curDay = time.localtime().tm_mday
        self.curMon = time.localtime().tm_mon
        self.curYear = time.localtime().tm_year

        self.daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octuber", "November", "December"]

    def curtime(self):
        return f"{self.curHour}:{self.curMin}:{self.curSec}"

    def curdate(self):
        return f"{self.curDay}/{self.curMon}/{self.curYear}"

    def curdatetime(self):
        return f"{self.daysOfWeek[self.curWeekDay]}, {self.months[self.curMon]} {self.curDay}, {self.curYear}. {self.curHour}:{self.curMin}"