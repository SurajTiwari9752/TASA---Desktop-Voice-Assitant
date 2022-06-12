import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
 


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 100)

voices = engine.getProperty('voices')
for voice in voices:
  #  print "Using voice:", repr(voice)
    engine.setProperty('voice', voice.id)

def speak(audio): 
 engine.say(audio)
 engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i am TASA how may i help you")

def takeCommand():
    #it take microphone input from the user and returns string output

    r = sr.Recognizer()
    #r.energy_threshold = 400  
    with sr.Microphone() as source:
     #print("Please wait. Calibrating microphone...")   
        print("Litening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please.....") 
        return "None"
    return query    


def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    
    server.ehlo()
    server.starttls()
    server.login('surajtiwari8433@gmail.com', 'Suraj@2000')
    server.sendmail('surajtiwari8433@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query= takeCommand().lower()

    # logic for executing tasks based on query
    if "wikipedia" in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)


    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com") 


    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")


    elif 'play music' in query:
        music_dir = 'D:\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))


    elif ' the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir ,the time is {strTime} ")


    elif 'open code' in query:
        codePath ="C:\\Users\\suraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)


    elif 'email to suraj' in query:
        try:
            speak("what should i say")
            content = takeCommand()
            to = "surajtiwari8433@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("sorry my friend suraj. I am not able to send email")

    elif 'exit' in query:
        exit