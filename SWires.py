#ON THE SUBJECT OF WIRES

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

#GATHER INFO
Wires = input("How many wires are there? [3,4,5,6]: ")


#3 WIRES
if Wires == '3':
    First = input("Are there any red wires? [y/n]: ")
    if First == 'n':
        print(color.BOLD + "-> Cut the second wire" + color.END)
        exit()
    else:
        Second = input("Is the last wire white? [y/n]: ")
    if Second == "y":
        print(color.BOLD + "-> Cut the last wire" + color.END)
        exit()
    else:
        Third = input("Is there more than one blue wire? [y/n]: ")
    if Third == "y":
        print(color.BOLD + "-> Cut the last blue wire" + color.END)
        exit()
    else:
        print(color.BOLD + "-> Cut the last wire" + color.END)
        exit()


#4 WIRES
elif Wires == '4':
    First = input("How many red wires are there? [0,1,2,3,4]: ")
    if First == '0':
        First2 = input("Is the last wire yellow? [y/n]: ")
        if First2 == 'y':
            print(color.BOLD + "-> Cut the first wire" + color.END)
            exit()
        else:
            pass
    elif First > '1':
        First3 = input("Is the last digit of the serial number odd? [y/n]: ")
        if First3 == 'y':
            print(color.BOLD + "-> Cut the last red wire" + color.END)
            exit()
        else:
            pass
    else:
        pass
    Second = input("Is there exactly one blue wire? [y/n]: ")
    if Second == 'y':
        print(color.BOLD + "-> Cut the first wire" + color.END)
        exit()
    else: 
        Second2 = input("Is there more than one yellow wire? [y/n]: ")
        if Second2 == 'y':
            print(color.BOLD + "-> Cut the last wire" + color.END)
            exit()
        else:
            print(color.BOLD + "-> Cut the second wire" + color.END)
            exit()
        
        

#5 WIRES
elif Wires == '5':
    First = input("Are there any black wires? [y/n]: ")
    if First == 'y':
        First2 = input("Is the last wire black? [y/n]: ")
        if First2 == 'y':
            First3 = input("Is the last digit of the serial number odd? [y/n]: ")
            if First3 == 'y':
                print(color.BOLD + "-> Cut the fourth wire" + color.END)
                exit()
            else:
                print(color.BOLD + "-> Cut the first wire" + color.END)
                exit()
        else:
            print(color.BOLD + "-> Cut the first wire" + color.END)
            exit()
    else:
        Second = input("Is there exactly one red wire? [y/n]: ")
        if Second == 'y':
            Second2 = input("Is there more than one yellow wire? [y/n]: ")
            if Second2 == 'y':
                print(color.BOLD + "-> Cut the first wire" + color.END)
                exit()
            else:
                 print(color.BOLD + "-> Cut the second wire" + color.END)
            exit()
        else:
            print(color.BOLD + "-> Cut the second wire" + color.END)
            exit()
            
            
#6 WIRES
else:
    First = input("How many yellow wires are there? [0,1,2,3,4,5,6]: ")
    if First == '0':
        First2 = input("Is the last digit of the serial number odd? [y/n]: ")
        if First2 == 'y':
            print(color.BOLD + "-> Cut the third wire" + color.END)
            exit()
        else:
            pass
    elif First == '1':
        First3 = input("Is there more than one white wire? [y/n]: ")
        if First3 == 'y':
            print(color.BOLD + "-> Cut the fourth wire" + color.END)
            exit()
        else:
            pass
    else:
        pass
    Second = input("Are there any red wires? [y/n]: ")
    if Second == 'y':
        print(color.BOLD + "-> Cut the fourth wire" + color.END)
        exit()
    else:
        print(color.BOLD + "-> Cut the last wire" + color.END)
        exit()
            
