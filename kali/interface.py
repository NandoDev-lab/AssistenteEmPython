import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
import time 
import os
from kali import AI



class Tela_Animada(QWidget):
   
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 400)
        self.setWindowFlags(Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)
        self.movie = QMovie('tela.gif')
        self.label_animation.setMovie(self.movie)
        timer = QTimer(self)

        self.startAnimation()
        timer.singleShot(1000000, self.stopAnimation)
        
        
    def startAnimation(self):
        self.movie.start()
       
    
    def stopAnimation(self):
        self.movie.stop()
        self.close()




class iniciar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 225)
        self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)
        self.movie = QMovie('/jarvis_ini.gif')
        self.label_animation.setMovie(self.movie)
        timer = QTimer(self)

        self.startAnimation()
        timer.singleShot(5000, self.stopAnimation)
        


    def startAnimation(self):
        self.movie.start()
        

    
    def stopAnimation(self):
        self.movie.stop()
        self.close()
   

class principal(QWidget):
    def __init__(self):
        super().__init__()
        
       

      
          
                
        

app = QApplication(sys.argv)
demo = principal()

sys.exit(app.exec_())




