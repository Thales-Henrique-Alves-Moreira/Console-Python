import pyttsx3

engine = pyttsx3.init('sapi5')

def speak(text, volume):
    engine.say(text)
    engine.setProperty("volume", volume)
    engine.runAndWait()
    return