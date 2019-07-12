
helloIntent = ["hello","hi","hey","hey there","hi there","hello there"]

# Membership Operator - in , not in

chat = True
while chat:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
