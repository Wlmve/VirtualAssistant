import datetime
from email.message import EmailMessage
from Emailseceret import senderemail, password
import smtplib
import requests
from newsapi import NewsApiClient
import webbrowser as we
import pyjokes
import psutil
import pyttsx3
import pyaudio
import speech_recognition as sr



def inputCommand():
    r = sr.Recognizer()
    walk= ""
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            walk = r.recognize_google(r.listen(source), language="en-IN")
        except Exception as e:
            output("Say that again Please...")
    return walk

def output(audio):
    engine.say(audio)
    engine.runAndWait()

user = "Joshua"
assistant = "Aqualad"
engine = pyttsx3.init()
voices = engine.getProperty("voices")

# For Mail voice AKA Jarvis
engine.setProperty("voice", voices[1].id)

def greet():
    hour=datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        output(f"Top of the morning  {user}")
    elif (hour >= 12) and (hour < 18):
        output(f"I can only wish you all the best all day long {user}")
    elif (hour >= 18) and (hour < 21):
        output(f"Salutations upon this fine eve of the blazing Sun {user}")
    output("How may I assist you?")

def sendEmail():
    email_list={
        "test":"jibeyi2086@vinopub.com"# used a temporary mail
    }
    try: 
      email=EmailMessage()
      output("Who should i send this too? ")  
      name = inputCommand().lower() 
      email["To"] = email_list[name]
      output("What should i set your subject to? ") 
      email["Subject"] = inputCommand().lower()
      email["From"] = senderemail
      output("What should send? ")
      email.set_content(inputCommand())
      s=smtplib.SMTP("smtp.gmail.com", 587)
      s.starttls()
      s.login(senderemail,password)
      s.send_message(email)
      s.close()
      output("Email was sent ")
    except Exception as e:
        print(e)
        output("Email was not able to send")
    
def weather():
    city="Baltimore"
    res= requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp2 = res["main"]["temp"]
    feels=  res["main"]["feels_like"]
    output(
        f"Temperature in {city} is {format(temp2)} degree Celsius /n but it feels like {format(feels)} Celsius")
def news():
    newsapi = NewsApiClient(api_key='9e8a650e75374140ab3a3d7f56483fa7')
    output("What topic you need the news about")
    topic = inputCommand()
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        output(y["description"])
def StockX():
    import webbrowser as wb
    we.open_new_tab('http://www.https://stockx.com/')

greet()
while True:
    walk= inputCommand().lower()
    if("time" in walk):
         output("Current time is " + datetime.datetime.now().strftime("%I:%M"))

    elif ('date' in walk):
        output("Current date is " + str(datetime.datetime.now().day) + " " + str(datetime.datetime.now().month)+ " " + str(datetime.datetime.now().year))

    elif ('email' in walk):
        sendEmail()

    elif ("search" in walk):
        output("what should I search on google?")
        we.open("https://www.google.com/search?q="+inputCommand())    

    elif ('weather' in walk):
        weather()

    elif ("news" in walk):
        news()

    elif ("joke" in walk):
        output(pyjokes.get_joke())  

    elif "cpu" in walk:
        output(f"Cpu is at {str(psutil.cpu_percent())}") 

    elif "end" in walk:
        hour = datetime.datetime.now().hour
        if (hour >= 21) and (hour < 6):
            output(f"Good Night {user}!  Sleep tight")
        else:
            output(f"Bye {user}")
        quit()