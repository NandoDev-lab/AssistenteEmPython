from pyaudio import paStreamIsStopped
import pyttsx3
from random import choice
from interpretador import interpretar
from cumprimentos import cumprimentos

# texto para voz
speaker =  pyttsx3.init()
nome=""

def identificador(nome):
    
    speaker.say('Qual é o seu nome?')
    speaker.runAndWait()
    resposta1 = interpretar()
    while resposta1 == "" or resposta1 == cumprimentos:
        speaker.say('Repita seu nome')
        speaker.runAndWait()
        print("Ainda estou aguardando o seu nome...")
        resposta1 = interpretar()
    else:
        nome = str(resposta1)


    Nome=nome
    if Nome != "sair":
        speaker.say(f'você disse que seu nome é {Nome}')
        speaker.runAndWait()
        speaker.say(f'Estou a sua disposição senhor,{Nome}')
        speaker.runAndWait()
    return nome

usuario = []

if usuario == "":
    usuario.append(nome)
elif len(usuario)!= 0:
    if nome in usuario:
        pass
    else:
        usuario.append(nome)