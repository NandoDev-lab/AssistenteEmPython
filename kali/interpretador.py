from vosk import Model, KaldiRecognizer
import json
import pyttsx3
from random import choice
from selenium import webdriver
import os
import pyaudio
import time

# Verificando modelo pre-treinado
if not os.path.exists("C:/Users/user/kali/vosk-model-small-pt-0.3"):
    print ("Favor verificar existencia do modelo treinado em model-br.")
    exit (1)

# texto para voz
speaker =  pyttsx3.init()

# Ativando microfone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Atribuindo modelo de reconhecimento
model = Model("C:/Users/user/kali/vosk-model-small-pt-0.3")
rec = KaldiRecognizer(model,16000)


def interpretar():
    # Loop continuo
    while True:
        
        # Lendo audio do microfone
        data = stream.read(8000)
    
        # Convertendo em texto    
        if rec.AcceptWaveform(data):
        # Fazendo a leitura do JSON para extrair apenas o texto capturado
            finalResult = json.loads(rec.Result())
            texto = finalResult.get("text")
            return f"{texto}"
