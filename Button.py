#ON THE SUBJECT OF THE BUTTON

class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   
#GATHER INFO
Bat1 = '?'
Held = '0'
Color = input("What color is the button? [1-Blue, 2-White, 3-Yellow, 4-Red]: ")
Text = input("What does the button say? [1-Abort, 2-Detonate, 3-Hold, 4-Press]: ")

#STEP 1
if Color == '1' and Text == '1':
    print(color.BOLD + "-> Press and hold the button" + color.END)
    Held = '1'
    
#STEP 2
else:
    if Text == '2':
        Battery = input("Is there more than one battery? [y/n]: ")
        if Battery == 'y':
            print(color.BOLD + "-> Press and immediately release the button" + color.END)
            exit()
        else:
            Bat1 = 'n'
    else:
        pass
    
#STEP 3
if Color == '2':
    Label = input("Is there a lit indicator labeled 'CAR'? [y/n]: ")
    if Label == 'y':
        print(color.BOLD + "-> Press and hold the button" + color.END)
        Held = '1'
    else:
        pass
        
#STEP 4
if Held == '0' and Bat1 == '?':
    Battery2 = input("Are there more than two batteries? [y/n]: ")
    if Battery2 == 'y':
        Label2 = input("Is there a lit indicator labeled 'FRK'? [y/n]: ")
        if Label2 == 'y':
            print(color.BOLD + "-> Press and immediately release the button" + color.END)
            exit()
        else:
            pass
    else:
        pass
else:
    pass

#STEP 5
if Held == '0' and Color == '3':
    print(color.BOLD + "-> Press and hold the button" + color.END)
    Held = '1'
else:
    pass
    
#STEP 6
if Held == '0' and Color == '4' and Text == '3':
    print(color.BOLD + "-> Press and immediately release the button" + color.END)
    exit()
else:
    pass

#STEP 7
if Held == '0':
	print(color.BOLD + "-> Press and hold the button" + color.END)
else:
	pass

#RELEASING A HELD BUTTON
#GATHER INFO
Strip = input("What color is the strip to the right of the module? [1-Blue, 2-White, 3-Yellow, 4-Other]: ")

if Strip == '1':
    print(color.BOLD + "-> Release when the countdown timer has a 4 in any position" + color.END)
elif Strip == '2':
    print(color.BOLD + "-> Release when the countdown timer has a 1 in any position" + color.END)
elif Strip == '3':
    print(color.BOLD + "-> Release when the countdown timer has a 5 in any position" + color.END)
else:
    print(color.BOLD + "-> Release when the countdown timer has a 1 in any position" + color.END)
