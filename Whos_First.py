#ON THE SUBJECT OF WHO'S ON FIRST

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

#GATHER INFO
Display = input("What does the display say? (Enter a space if display is empty): ")
Display = Display.lower()

#STEP 1
#TOP LEFT
if Display == 'ur':
    Value = input("What's displayed in the top left?: ")
    
#TOP RIGHT
elif Display == 'first' or Display == 'okay' or Display == 'c':
    Value = input("What's displayed in the top right?: ")

#MIDDLE LEFT
elif Display == 'yes' or Display == 'nothing' or Display == 'they are' or Display == 'LED':
    Value = input("What's displayed in the middle left?: ")
    
#MIDDLE RIGHT
elif Display == 'blank' or Display == 'read' or Display == 'red' or Display == 'you' or Display == 'your' or Display == "you're" or Display == 'their':
    Value = input("What's displayed in the middle right?: ")
    
#BOTTOM LEFT
elif Display == ' ' or Display == 'reed' or Display == 'leed' or Display == "they're":
    Value = input("What's displayed in the bottom left?: ")
    
#BOTTOM RIGHT
elif Display == 'display' or Display == 'says' or Display == 'no' or Display == 'lead' or Display == 'hold on' or Display == 'you are' or Display == 'there' or Display == 'see' or Display == 'cee':
    Value = input("What's displayed in the bottom right?: ")
    
#NONE
else:
    print(color.BOLD + "-> Invalid entry" + color.END)
    exit()
    

#STEP 2
#CLUSTERFUCK OF IF STATEMENTS AND INFORMATION
if Value == 'ready':
    print(color.BOLD + "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, FIRST, UHHH, NOTHING, WAIT" + color.END)
    exit()
elif Value == 'first':
    print(color.BOLD + "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST" + color.END)
    exit()
elif Value == 'no':
    print(color.BOLD + "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST" + color.END)
    exit()
elif Value == 'blank':
    print(color.BOLD + "WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, WHAT, LEFT, UHHH, YES, FIRST" + color.END)
    exit()
elif Value == 'nothing':
    print(color.BOLD + "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING, READY" + color.END)
    exit()
elif Value == 'yes':
    print(color.BOLD + "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, LEFT, BLANK, NO, WAIT" + color.END)
    exit()
elif Value == 'what':
    print(color.BOLD + "UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, WAIT, YES, PRESS, RIGHT" + color.END)
    exit()
elif Value == 'uhhh':
    print(color.BOLD + "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH, MIDDLE, WAIT, FIRST" + color.END)
    exit()
elif Value == 'left':
    print(color.BOLD + "RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, PRESS, READY, OKAY, NOTHING" + color.END)
    exit()
elif Value == 'right':
    print(color.BOLD + "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, UHHH, BLANK, OKAY, FIRST" + color.END)
    exit()
elif Value == 'middle':
    print(color.BOLD + "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE, RIGHT, FIRST, UHHH, YES" + color.END)
    exit()
elif Value == 'okay':
    print(color.BOLD + "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, BLANK, PRESS, WHAT, RIGHT" + color.END)
    exit()
elif Value == 'wait':
    print(color.BOLD + "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, NOTHING, READY, RIGHT, MIDDLE" + color.END)
    exit()
elif Value == 'press':
    print(color.BOLD + "RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, LEFT, FIRST, WHAT, NO, WAIT" + color.END)
    exit()
elif Value == 'you':
    print(color.BOLD + "SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, UH UH, LIKE, DONE, U" + color.END)
    exit()
elif Value == 'you are':
    print(color.BOLD + "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE" + color.END)
    exit()
elif Value == 'your':
    print(color.BOLD + "UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU'RE, YOU, WHAT?, HOLD, LIKE, DONE" + color.END)
    exit()
elif Value == "you're":
    print(color.BOLD + "YOU, YOU'RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, SURE, DONE, LIKE, HOLD" + color.END)
    exit()
elif Value == 'ur':
    print(color.BOLD + "DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU'RE, LIKE, NEXT, UH UH, YOU ARE, YOU" + color.END)
    exit()
elif Value == 'u':
    print(color.BOLD + "UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U, YOU, LIKE, HOLD, YOU ARE, YOUR" + color.END)
    exit()
elif Value == 'uh huh':
    print(color.BOLD + "UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, LIKE, YOU'RE, UR, U, WHAT?" + color.END)
    exit()
elif Value == 'uh uh':
    print(color.BOLD + "UR, U, YOU ARE, YOU'RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, YOUR, SURE, HOLD, WHAT?" + color.END)
    exit()
elif Value == 'what?':
    print(color.BOLD + "YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?, SURE" + color.END)
    exit()
elif Value == 'done':
    print(color.BOLD + "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE" + color.END)
    exit()
elif Value == 'next':
    print(color.BOLD + "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, UR, YOU'RE, U, YOU" + color.END)
    exit()
elif Value == 'hold':
    print(color.BOLD + "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD, UH HUH, YOUR, LIKE" + color.END)
    exit()
elif Value == 'sure':
    print(color.BOLD + "YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE, U, WHAT?, NEXT, YOUR, UH UH" + color.END)
    exit()
elif Value == 'like':
    print(color.BOLD + "YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, SURE, YOU ARE, YOUR" + color.END)
    exit()
else:
    print(color.BOLD + "-> Invalid entry" + color.END)
    exit()