import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import time


#set engine--------------------------------------------------------------------------------------------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)




#-------functions1(computer speak)-------------------------------------------------------------------------------------------------------------

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#-----------------------(computer wish me)-------------------------------------------------------------------------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good moring aru sir!')

    elif hour>=12 and hour<=18:
         speak('good after noon aru sir!')
         
    else:
        speak ('good evening  sir!')

    speak('i am phoenix ! what can i do for you')
    #-----------------------(computer take ur voice)------------------------------------------------------------------------------------

def takeCommand():
# its take micro phone input from the user and returen the string out put---------------------------------------------

    r = sr.Recognizer()
    with sr .Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing...!!')
        query= r.recognize_google(audio, language='en-in')
        print(F"User said:  {query}\n")

    except Exception as e:
        print("say again please...")
        return "None"
    return query
    
if __name__ == "__main__":
   wishMe()#first it will wish u then take ur voice--------------------------------------------------------------------
   while True:
    query = takeCommand().lower()


#logic tasks--
# wikipedia work----------------------------------------------------------------------------------------------------------
    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


    elif "who made you" in query: 
        speak ("I have been created by programmer XONE ARU.")
        query = query.replace("who made you","")
        

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")      


    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

    elif 'which college i study from' in query:
           speak(f"sir, U are study in Rajshree Institute of managment of technology") 
           query = query.replace("which college i study from","")      
           

   