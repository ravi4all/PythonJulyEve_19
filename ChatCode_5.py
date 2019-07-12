from datetime import datetime as dt

helloIntent = ["hello","hi","hey","hey there","hi there","hello there"]
dateIntent = ["date today","today's date","date please","tell me date","date"]
timeIntent = ["tell me time","current time","please tell me time","time"]

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
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
