
# Logical Operators - and, or, not

chat = True
while chat:
    msg = input("Enter your message : ")
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
