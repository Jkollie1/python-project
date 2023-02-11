Welcome_message = "To Nova Web Python Group Project"
print(Welcome_message)
print("The below porgram will accept information from a user and display it what the user entern\?")

def User_info(name, age):
    print("Welcome to", Welcome_message)
    print ("Hello", name)
    print ("You are", age, "year old")


name = input("What is your name?")
age = input("What is your age")
User_info(name, age)

def ask_Any_Question(message):
    print("This is your ans:", message)
    print("This is your ans:", message1)

message = input("Why you choose to do programming?")
message1 = input("List all the arethmetic operator you learn from this book")
ask_Any_Question(message)

