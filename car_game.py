command = ""
started = False

while True:
    command = input('> ').upper()
    if command == "START":
        if(started):
            print('Car is already started')
        else:
            started = True
            print("Cart start... ready to go!")
    elif command == 'STOP':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print('Car stopped')
    elif command == 'HELP':
        print("""
Start - To start the cart
Stop - To stop the car
Quit - To quit
        """)
    elif command == 'QUIT':
        break
    else:
        print("I don't understand that.")
