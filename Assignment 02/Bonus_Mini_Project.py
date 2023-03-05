#GROUP QUESTION IN COLLABORATION WTIH:- YASH SINGH, YOGESH KUMAR, NISHCHAL GAUR
import pyttsx3
import requests


def K2C(K):
    c = K-273.15
    return int(c)


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 170)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    return


def temperature():
    key = "26a8a6650dfddcf1000379ecafefcd8d"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter The city name:")
    c_url = url + "appid=" + key + "&q=" + city_name
    response = requests.get(c_url)
    x = response.json()
    c = x["name"]
    temp = K2C(x['main']['temp'])
    print(f"The temperature of {c} is {temp} degree celsius")
    speak(f"The temperature of {c} is {temp} degree celsius")
    return


def tellip():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    x = response.json()
    city = x['city']
    ip = x['query']
    country = x['country']
    print(
        f"The Ip Address of the device is:{ip}  and the city is:{city}   and the country is:{country}")
    d = f"The Ip Address of the device is:{ip}  and the city is:{city}   and the country is:{country}"
    speak(d)
    return


speak("Hello , I am Program to tell ip information and weather using Public api")
choice = int(
    input(""" Enter 1 to know IP ADDRESS\n Enter 2 to Get Weather information:"""))
if choice == 1:
    tellip()
elif choice == 2:
    temperature()
