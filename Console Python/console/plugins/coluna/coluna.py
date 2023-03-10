#under development

#from functions.speak.speak import speak
from threading import Thread
from time import sleep

import pyttsx3

engine = pyttsx3.init('sapi5')
class coluna:
    def __init__(self) -> None:
        self.tempo = 0
        self.ativado = False
        self.volume = 0

    def falarLembrete(self):
        engine.setProperty("volume", self.volume)

        engine.startLoop(False)

        while self.ativado:
            sleep(tempo)
            engine.say("a")

        engine.endLoop()

        print("thread finalizada com sucesso")

    def lembrarColuna(self, commandLine):
        if "lc" in commandLine: #lembrar coluna. "-t" é o tempo que demora para ficar avisando
            global ativado
            global tempo
            
            parameters = commandLine.split(' ')

            if "-off" in commandLine:
                ativado = False
                return

            if "-t" in commandLine:
                for i in range(len(parameters) - 1):
                    if "-t" in parameters[i]:
                        if i + 1 < len(parameters):
                            iTempo = parameters.index("-t") + 1
                            try: 
                                tempo = int(parameters[iTempo])
                            except ValueError:
                                print('Please use a number in the -t parameter. Usage " -t 5000 ".')
                                return
                        else:
                            print('Please inform the number in the -t parameter. Usage " -t 5000 ".')
                            return
            else:
                print("Please inform the -t parameter.")
                return
                
            if "-msgbx" in commandLine:
                pass

            if "-v" in commandLine:
                iVolume = parameters.index('-v') + 1

                try:
                    parametro = parameters[iVolume]
                except:
                    print('Please use something valid in the -v parameter ("mute", "low", "medium" and "high"). Usage " -v "high" ".')
                    return

                if parametro == "low":
                    volume = 0.3
                elif parametro == "medium": 
                    volume = 0.5
                elif parametro == "high":
                    volume = 0.8  
                else:
                    print('Please use something valid in the -v parameter ("mute", "low", "medium" and "high"). Usage " -v "high" ".')
                    return

            ativado = True

            t = Thread(target=self.falarLembrete, args=[volume]).start()