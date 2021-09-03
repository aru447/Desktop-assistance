import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
from wikipedia.wikipedia import page
import wolframalpha
import json
import requests
import pywhatkit as kit
from  requests import get
import pyautogui
#import PyPDF2
import pyjokes
import cv2,time
import psutil,json
import re


#print("system confrigation!, please wait! , system confrigation complete!systemready!sir")
#set engine--------------------------------------------------------------------------------------------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)




#-------functions1(computer speak)-------------------------------------------------------------------------------------------------------------

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#==========================================================================================================
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
battery = psutil.sensors_battery()
bp = battery.percent
bcp = battery.power_plugged
bt = secs2hours(battery.secsleft)


def bevents():
    print(f"charge = {bp}, time left = {bt}, Charger Plugged-in = {bcp}")
    if bp <= 20:
        speak(
            f'Battery level is, {bp}  percent! System status: Critical! Time remaining: {bt}. We are now running on backup power! Charger Plugged-in: {bcp}')
    elif bp > 20 and bp <= 59:
        speak(
            f'Battery level is, {bp} percent! System status: Average!  Time remaining: {bt}. Charger Plugged-in: {bcp}')
    elif bp <= 10:
        speak('Battery level critical!  Time remaining: {bt}. Plugin power supply!')
    elif bp >= 60 and bp <= 99:
        speak(f'Battery level is, {bp} percent! System status: Good!  Time remaining: {bt}. Charger Plugged-in: {bcp}')
    elif bp == 100:
        speak(f'Battery is fully charged! Charger Plugged-in: {bcp}')
#------------------------------------------------------------------------------------------------------------        
def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
 #==================================-----------------------------------=============================---------       
def camera():
    speak("Press space to take image and escape to stop Camera")
    Camera = cv2.VideoCapture(0)
    cv2.namedWindow("Camera")
    img_counter = 0
    while True:
        ret, frame = Camera.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Camera", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            speak("closing camera")
            break
        elif k%256 == 32:
            img_name = "camera{}.png".format(img_counter)
            #Replace CameraPath with the path of the folder where you want to save your photos taken by camera
            path="CameraPath"
            cv2.imwrite(os.path.join(path , img_name), frame)
            cv2.imwrite(img_name, frame)
            speak("{} image taken".format(img_name))
            img_counter += 1
    Camera.release()
    cv2.destroyAllWindows()
#____________________________________________________________________________________________________
#____________________________________________________________________________________________________ ===
def help():
   
    speak ("SCREENSHOT to get screenshot")
 

#-----------------------(computer wish me)----------------------------------------------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good moring  sir!')

    elif hour>=12 and hour<=18:
         speak('good after noon  sir!')
         
    else:
        speak ('good evening  aru sir!')

        #speak("How can I help you?")
    speak("according to my data !  today is your birthday! so wish you very happy birthday sir! i booked your birthday cake !it will come 9pm")
    speak('! ok sir now !let me check  sir! where will be go today ! sir i have feched the data where we go! i will send u details in your email! check your email')


    #speak('i am phoenix ! what can i do for you')
    #-----------------------(computer take ur voice)------------------------------------------------------------------------------------

def takeCommand():
# its take micro phone input from the user and returen the string out put---------------------------------------------

    r = sr.Recognizer()
    with sr .Microphone() as source:
        print('Listening..')
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print('recognizing...!!')
        query= r.recognize_google(audio, language='en-in')
        print(F"User said:  {query}\n")
        

    except Exception as e:
       #speak("sir do u have any work")
        return "None"
    return query
#speak("system confrigation  please wait! , system confrigation complete!now i am online sir")
#wishMe()   
    
if __name__ == "__main__":
   wishMe()#first it will wish u then take ur voice--------------------------------------------------------------------
   while True:
    query = takeCommand().lower()
    
    if query==0:
            continue

    if "go to sleep" in query or "ok bye" in query or "stop" in query:
            speak('your personal assistant phoenix! is shutting down,!')
            #print('your personal assistant G-one is shutting down,!')
            break



#logic tasks--
# wikipedia work----------------------------------------------------------------------------------------------------------
    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
#-----------------------------------------------------------------------------------------------------
    elif 'power status' in query:
            bevents()
#--------------------------------------------------------------------------------------------------------
    elif "who made you" in query: 
        speak ("I have been created by programmer ,professor ARU.")
        query = query.replace("who made you","")
 #----------------------------------------------------------------------------------------------------------       
    elif"open camera" in query:
            camera()
#=========================================================================================================
    elif 'open youtube' in query:
     webbrowser.open("youtube.com")   
     speak("Here is youtube")   
    


    elif "close youtube" in query:
            speak("closing youtube")
            os.system("taskkill /f /im iexplore.exe")    

    
    elif "tell me ip address"in query:
            ip= get ('https://api.ipify.org').text
            speak(f"sir! your ip address is {ip}")

#---------------------------------------------------------------------------------------------------
    #elif "read my pdf" in query:
           #pdf_reader()
#-------------------------------------------------------------------------------------------------
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


    elif "take a screenshot" in query:
       speak("sir! tell me  the name for this screenshot file")
       name =takeCommand().lower()
       speak("hold sir! i take screenshot")
       time.sleep(3)
       img =pyautogui.screenshot()
       img.save(f"{name}.png")
       speak("i m done sir! the screenshot is saved in our main folder! now i am ready for next command")    


    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

    elif 'which college i study from' in query:
           speak(f"sir, U are study in Rajshree Institute of managment of technology") 
           query = query.replace("which college i study from","")      
           
    elif "mum" in query:
          speak("your mom is , preeti sharma")
          query = query.replace("mum","")

    elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


    elif 'who are you' in query or 'what can you do' in query:
     speak('I am phoenix !version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

    elif "open stack overflow" in query:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
    elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)              
    elif  "take a photo" in query:
            speak('picture!,click')
            ec.capture(0,"robo camera","img.jpg")
           # speak('camera!,open')

    elif 'show'  in query:
            speak("searching sir! please wait!")
            query= query.replace("show", "")
            webbrowser.open_new_tab(query)

    elif "ok close" in query:
          speak("ok sir! wait for next command") 
          os.system("taskkill /f /im msedge.exe")     
    
    elif "open notepad" in query:
            speak("opening notepad")
            npath= "C:\\Windows\\System32\\Notepad.exe"
            os.startfile(npath)

    

    elif "open command prompt" in query:
            speak(" opening command prompt") 
            os.system("start cmd")

    elif "close command prompt" in query:
            speak(" closing cmd sir")
            os.system("taskkill /f /im cmd.exe")     
         
    elif "close notepad" in query:
            speak("ok sir! closing notepad") 
            os.system("taskkill /f /im notepad.exe")

    elif "tell me a joke" in query:
            joke= pyjokes.get_joke(language="en", category="neutral")
            speak(joke) 

    elif "system shutdown" in query:
            speak("sir !all functions are close !now i m going to ofline !goodnight ")
            os.system("shutdown /s /t 1")
    
    elif "system restart" in query:
            speak(" system going to restart! please wait")
            os.system("shutdown /r /t 1")

    elif "you can go" in query or "no " in query:
            speak("ok sir! Thanks for useing me !have a good day " )
            query = query.replace("no you can go","")
            break

   



    elif 'hello'  in query:
        speak("hello sir")


    elif'how are you' in query:
        speak("i am good sir ! what about u")

    elif'good'in query:
            speak('ok sir ! if u want access somthing, please  call me sir')

    elif'thank you' in query or "thanks" in query:
            speak("my pleaser ! injoy your day sir")

    elif "day" in query:
          tellDay()

    elif "sorry" in query:
         speak("sir! dont worry i will manage your coding and study schedule! go with your family sir")      
            
    elif "are you sure" in query:
        speak("yes sir! i am sure")
   