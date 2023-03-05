import pyjokes
import pyttsx3
from sys import exit
import datetime
import random
from pywikihow import search_wikihow
from PIL import Image
import subprocess
from bs4 import BeautifulSoup
import requests, os, string
import speech_recognition as sr
from pipwin import pipwin
import wikipedia
import os
import pywhatkit as kit 
import time
import requests
import webbrowser
import googlesearch
import cv2
import pyaudio
from requests import get
import sys
from time import sleep 
import pyautogui
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime, QDate ,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Siya import Ui_MainWindow
from PyQt5.uic import loadUiType
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[-1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning")
        elif hour>=12 and hour<18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        speak("hello  I am Siya an virtual assisstant in beta stage ")
        speak("I can do various works and be your assisstant here ")
        speak("now I am ready for your order")
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.taskexecution()
    def takecom(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            audio = r.listen(source,timeout=2,phrase_time_limit=4)

        try:
            print("Recognizing............")
            text = r.recognize_google(audio,language='en-in')
            #print(f"user said:{statement}\n")
            print(text)
        except Exception:
            speak("Network connection error!....")
            speak("Say that again please")
            print("Network Connection Error!............")
            print("Say that again please")
            return "None"
        return text
    print("Loading Your AI Personal Assisstant Siya")
    speak("Loading Your AI Personal Assisstant Siya")
    speak("I need active internet connection to work")
    def taskexecution(self):
        wishme()
        while True:
            self.query = self.takecom().lower()
            if "open notepad" in self.query:
                apath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(apath)
                speak("opening notepad ")
            if "close notepad" in self.query:
                speak("okay closing notepad..")
                os.system("taskkill /f /im notepad.exe")
            if "open game" in self.query:
                npath ="C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
                os.startfile(npath)
                speak("opening Epic Games Launcher")
            if "open command prompt" in self.query:
                os.system("start  cmd")
                speak("opening command prompt")
            if "close command prompt" in self.query:
                speak("okay closing command prompt..")
                os.system("taskkill /f /im cmd.exe")
            if "how are" in self.query:
                speak("I am fine what about you")
            if "i am good" in self.query:
                speak("okay lets start any commands for me")
            if "play music" in self.query:
                speak("which song you want to listen")
                sss = self.takecom()
                url = "https://www.youtube.com/results?search_query="+sss
                webbrowser.open_new_tab(url)
            if "wikipedia" in self.query:
                speak("Searching Wikipedia......")
                query = self.query.replace("wikipedia"," ")
                results=wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)        
            if "open youtube" in self.query:
                webbrowser.open_new_tab("www.youtube.com")
                speak("youtube is open now")
            if "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"user IP address is :{ip}")
                print("User IP Address is ",ip)
            if "open google" in self.query:
                webbrowser.open_new_tab("www.google.com")
                speak("google is opening now")
            if "open twitter" in self.query:
                webbrowser.open_new_tab("www.twitter.com")
                speak("twitter is opening now")
            if "open instagram" in self.query:
                webbrowser.open_new_tab("www.instagram.com")
                speak("instagram is opening now")
            if "temperature" in self.query:
                speak("tell me the name of place to find temperature")
                st = self.takecom()
                search = "temperature in"+st
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")
                print("temperature in ",st,"is",temp)
            if "activate how to do" in self.query:
                speak("how to do mod is activated ,tell me what you want to know ")
                how = self.takecom()
                max_results = 1
                how_to = search_wikihow(how,max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)
            if "open whatsapp" in self.query:
                webbrowser.open_new_tab("www.whatsapp.com")
                speak("whatsapp is opening  now")
            if "open school website" in self.query:
                webbrowser.open_new_tab("https://www.parentsalarm.com/")
                speak("parentsalarm is opening now")
            #zoom ka function add karna he 
            if "take a screenshot" in self.query:
                speak("please tell  me the name for this screenshot file")
                name = self.takecom()
                speak("please wait for few seconds ,i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done now file is  saved ")
            if "do calculations" in self.query:
                speak("okay i am opening calculator wait for a second ")
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            if "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            if "shutdown system" in self.query:
                os.system("shutdown /s /t 5")
            if "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            if "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            if "time" in self.query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S ")
                speak(f"The time is {strTime}")
                print(strTime)
            if "do paint" in self.query:
                jpath="C:\\Windows\\system32\\mspaint.exe"
                os.startfile(jpath)
                speak("opening MS paint .....")
            if "news" in self.query:
                news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak("here are some headlines form the Times of India ")
            if "send message" in self.query:
                print("YOU Have to login to web.whatsapp.com already to send message")
                speak("YOU Have to login to web.whatsapp.com already to send message")
                number=input("Enter number here:")
                name=input("Enter message  here:")
                print("Remember to enter time in 24 hour clock")
                time=int(input("enter hour here:"))
                minn=int(input("enter minute here:"))
                kit.sendwhatmsg("+91"+number,name,time,minn)
                speak("message sent")
            if "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img =cap.read()
                    cv2.imshow("webcam",img)
                    k = cv2.waitKey(20)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            if "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = "C:\\Users\\YASH\\Desktop\\S.I.Y.A\\music dir"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[1]))
            if "search on google" in self.query:
                speak("what should i search on google")
                cm = self.takecom()
                webbrowser.open_new_tab("https://www.google.com/results?search_query="+cm)
                speak("results shown to you on screen ")
            if "search on youtube" in self.query:
                speak("what should i search on youtube")
                c = self.takecom()
                webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+c)
                speak("opening youtube")
            if "who are you" in self.query:
                speak('I am Siya  version 1 point O ,,, your personal assistant made by my  ,,, developer ,,,,,,,,,,,Yash Singh,,,,,, i am first version and i will be improved in future. I am programmed to do  minor tasks like'
                    'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                    'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
            if "goodbye" in self.query:
                speak("thanks for using me ,personal assisstaant siya is shutting down have a good day")
                break
            #if "wait" in self.query:
                speak("ok i am going to sleep")
                sleep(4)
            #google search add karna he
            #speak(" do you have any other work  ")
            #if __name__ == "__main__":
                #
startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\YASH\\Desktop\\setup\\BigheartedVagueFoal-size_restricted.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:\\Users\\YASH\\Desktop\\setup\\b709477ff0a3f94d94ace66c49c63e23.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:\\Users\\YASH\\Desktop\\setup\\dribbb.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
siya = Main()
siya.show()
exit(app.exec_())
exit()