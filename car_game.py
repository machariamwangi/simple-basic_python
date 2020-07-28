command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started ....")
    elif command == "stop":
        if not started:
            print("car is alredy stopped!.")
        else:
            started: False
            print("car stopped ...")
    elif command == "quit":
        print("car has been destroyed")
        break
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit =- to quit
        """)
    else:
        print("sorry, i don't understand that")
