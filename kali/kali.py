from navegar import navegar
import pyttsx3
from interpretador import interpretar
from identificar import identificador
import time
from prontidao import atender
from cumprimentos import dispensas
from encerrar import encerrar

# texto para voz
speaker = pyttsx3.init()

nome = interpretar()


identificador(nome)
while True:
       fala = interpretar()
       while fala == "oi":
              atender()        
              ordens = interpretar()
              print(f"{ordens}")

              if ordens == "navegue" or ordens == "navegar" or ordens == "navega":
                     navegar(ordens)
              elif fala == dispensas:
                     encerrar()

       


