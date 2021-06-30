import pyttsx3


import pyttsx3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from interpretador import interpretar
# texto para voz
speaker =  pyttsx3.init()



def navegar(ordens):
    ordens="navegar"
    if ordens == "navegar":
            speaker.say(f"você disse para {ordens}, executando...")
            speaker.runAndWait()
            speaker.say('Qual site gostaria de navegar?')
            speaker.runAndWait()      
            fala2 = interpretar()
            navegar = (fala2)
            print(fala2)
            while True:
                if navegar != "youtube" or "facebook" or "google":
                    speaker.say("não consegui entender suas ordens")
                    speaker.say("Por favor, repita o que você disse")
                    speaker.runAndWait() 
                    navegar = interpretar()
                break
                
                   

            navegar = interpretar()

            if navegar == "youtube":                
                youtube()               
            elif navegar == "facebook":
                facebook()                    
            elif navegar == "google":
               google()


def youtube():
    speaker.say(f"Entendi, o senhor deseja navegar no Youtube, executando...")
    speaker.runAndWait()
    youtube = "https://www.youtube.com"
    driver = webdriver.Chrome(executable_path="C:/Users/user/kali/chromedriver.exe")    
    speaker.say(f"abrindo o site youtube,conforme o solicitado, Senhor...")
    speaker.runAndWait()
    driver.get(youtube)
    speaker.say(f"Ativei área de pesquisas, diga o titulo do video que deseja asistir...")
    speaker.runAndWait()
    pesquisar= interpretar()
    selecionar = driver.find_element_by_xpath('//*[@id="search"]')    
    selecionar.click()
    selecionar.send_keys(f'{pesquisar}')
    

   


def facebook():
    facebook = "https://www.facebook.com"
    speaker.say(f"Entendi, o senhor deseja navegar no {navegar}, executando...")
    speaker.runAndWait()
    driver = webdriver.Chrome(executable_path="C:/Users/user/kali/chromedriver.exe")
    driver.get(facebook)

def google():
    google = "https://www.google.com"
    speaker.say(f"Entendi, o senhor deseja navegar no {navegar}, executando...")
    driver = webdriver.Chrome(executable_path="C:/Users/user/kali/chromedriver.exe")
    driver.get(google)



