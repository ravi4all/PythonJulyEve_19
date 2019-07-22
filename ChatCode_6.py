from datetime import datetime as dt
import os
import glob, random
import webbrowser

helloIntent = ["hello","hi","hey","hey there","hi there","hello there"]
dateIntent = ["date today","today's date","date please","tell me date","date"]
timeIntent = ["tell me time","current time","please tell me time","time"]
musicIntent = ["play music","play song","start song"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hello User")
    elif msg in timeIntent:
        c_time = dt.now().time()
        print(c_time.strftime("%H:%M:%S,%p"))
    elif msg in dateIntent:
        date = dt.now().date()
        print(date.strftime("%d/%m/%y,%a"))
    elif msg in musicIntent:
        path = "C:/Users/asus/Music"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        s = random.choice(songs)
        os.startfile(s)
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
