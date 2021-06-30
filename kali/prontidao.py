from interpretador import interpretar
from random import choice
from cumprimentos import respostas
import pyttsx3

# texto para voz
speaker =  pyttsx3.init()

def atender():        
            resposta_aleatoria=choice(respostas)
            speaker.say(resposta_aleatoria)
            speaker.runAndWait()


           
          
            
           
        
    



