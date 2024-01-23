import random
greetingIntent = ["hello","hi","hey","hy","hello there","hi there","hlo"]
dateIntent = ["date","tell me date","what's the date","today's date"]
chat = True
while chat:
    msg = input("Enter your message..:")
    msg = msg.lower()
    #if msg == "hello" or msg == "hi" or msg == "hey":
    if msg in greetingIntent:
        print(random.choice(greetingIntent),"user")
    elif msg == "bye":
        print("Bye user")
        chat = False
    else:
        print("I don't understand..")
