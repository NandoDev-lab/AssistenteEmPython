
import pyttsx3
from interpretador import interpretar

# texto para voz
speaker =  pyttsx3.init()


def encerrar():
   
    speaker.say("Obrigado senhor, desativando o sistema neste momento.")
    speaker.runAndWait()
    speaker.say("até breve...")
    speaker.runAndWait()
    exit()
