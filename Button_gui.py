#ON THE SUBJECT OF THE BUTTON
from tkinter import *
import tkinter as tk

window=Tk()
window.title("Button")

class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   
#GATHER INFO
Bat1 = '?'
Held = '0'

exvar=tk.IntVar()
def exCom():
    exvar.set(1)
    exit()

#color commands
var=tk.IntVar()
def bluePush():
    global Color
    Color='1'
    var.set(1)
def whitePush():
    global Color
    Color='2'
    var.set(1)
def yellowPush():
    global Color
    Color='3'
    var.set(1)
def redPush():
    global Color
    Color='4'
    var.set(1)
#had to put this shit way up top because it breaks for no reason down lower in the program so fuck it
stripQuestion=Label(window, text="What color is the strip to the right of the module?")
ans1=Label(window, text="Release when the countdown timer has a 4 in any position", fg="red")
ans2=Label(window, text="Release when the countdown timer has a 1 in any position", fg="red")
ans3=Label(window, text="Release when the countdown timer has a 5 in any position", fg="red")
#Color = input("What color is the button? [1-Blue, 2-White, 3-Yellow, 4-Red]: ")
colorQuestion=Label(window, text="What color is the button?")
bluButton=Button(window, text="Blue", bg="blue", command=bluePush)
whitButton=Button(window, text="White", bg="white", command=whitePush)
yellButton=Button(window, text="Yellow", bg="yellow", command=yellowPush)
redButton=Button(window, text="Red", bg="red", command=redPush)

colorQuestion.grid(row=1, column=1, columnspan=4)
bluButton.grid(row=2, column=1, padx=10, pady=10)
whitButton.grid(row=2, column=2, padx=10, pady=10)
yellButton.grid(row=2, column=3, padx=10, pady=10)
redButton.grid(row=2, column=4, padx=10, pady=10)

bluButton.wait_variable(var)
#remove all grid items - might be able to do all in one go but dont know how - ex: *.grid_forget()
colorQuestion.grid_forget()
bluButton.grid_forget()
whitButton.grid_forget()
yellButton.grid_forget()
redButton.grid_forget()
#Text = input("What does the button say? [1-Abort, 2-Detonate, 3-Hold, 4-Press]: ")

var2=tk.IntVar()
#text commands
def abPush():
    global Text
    Text='1'
    var2.set(1)
def dePush():
    global Text
    Text='2'
    var2.set(1)
def hoPush():
    global Text
    Text='3'
    var2.set(1)
def prPush():
    global Text
    Text='4'
    var2.set(1)

textQuestion=Label(window, text="What does the button say?")
abButton=Button(window, text="Abort", command=abPush)
deButton=Button(window, text="Detonate", command=dePush)
hoButton=Button(window, text="Hold", command=hoPush)
prButton=Button(window, text="Press", command=prPush)

textQuestion.grid(row=1, column=1, columnspan=4)
abButton.grid(row=2, column=1, padx=10, pady=10)
deButton.grid(row=2, column=2, padx=10, pady=10)
hoButton.grid(row=2, column=3, padx=10, pady=10)
prButton.grid(row=2, column=4, padx=10, pady=10)

abButton.wait_variable(var2)
textQuestion.grid_forget()
abButton.grid_forget()
deButton.grid_forget()
hoButton.grid_forget()
prButton.grid_forget()

#STEP 1
holdButLab=Label(window, text="Press and hold the button", fg="red")
holRelButton=Label(window, text="Press and immediately release the button", fg="red")
exButton=Button(window, text="Exit", command=exCom)
if Color == '1' and Text == '1':
#    print(color.BOLD + "-> Press and hold the button" + color.END)
    holdButLab.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
    Held = '1'
    
#STEP 2
else:
    if Text == '2':
        var3=tk.IntVar()
        def yePush():
            global Battery
            Battery='y'
            var3.set(1)
        def noPush():
            global Battery
            Battery='n'
            var3.set(1)
            
#        Battery = input("Is there more than one battery? [y/n]: ")
        batQuestion=Label(window, text="Is there more than one battery?")
        yeButton=Button(window, text="Yes", command=yePush)
        noButton=Button(window, text="No", command=noPush)
        
        batQuestion.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        yeButton.grid(row=2, column=1, padx=10, pady=10)
        noButton.grid(row=2, column=2, padx=10, pady=10)
        
        yeButton.wait_variable(var3)
        
        batQuestion.grid_forget()
        yeButton.grid_forget()
        noButton.grid_forget()
        
        if Battery == 'y':
#            print(color.BOLD + "-> Press and immediately release the button" + color.END)
            holRelButton.grid(row=0, column=1, padx=10, pady=10)
            exButton.grid(row=1, column=1, padx=10, pady=10)
            exButton.wait_variable(exvar)
            exit()
        else:
            Bat1 = 'n'
    else:
        pass
    
#STEP 3
if Color == '2':
    var4=tk.IntVar()
    def yePush2():
        global Label
        Label='y'
        var4.set(1)
    def noPush2():
        global Label
        Label='n'
        var4.set(1)
#    Label = input("Is there a lit indicator labeled 'CAR'? [y/n]: ")
    carQuestion=Label(window, text="Is there a lit indicator labeled 'CAR'?")
    yeButton2=Button(window, text="Yes", command=yePush2)
    noButton2=Button(window, text="No", command=noPush2)
    
    carQuestion.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    yeButton2.grid(row=2, column=1, padx=10, pady=10)
    noButton2.grid(row=2, column=2, padx=10, pady=10)
    
    yeButton2.wait_variable(var4)
    
    carQuestion.grid_forget()
    yeButton2.grid_forget()
    noButton2.grid_forget()
    
    if Label == 'y':
#        print(color.BOLD + "-> Press and hold the button" + color.END)
        holdButLab.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
        Held = '1'
    else:
        pass
        
#STEP 4
if Held == '0' and Bat1 == '?':
    var5=tk.IntVar()
    def yePush3():
        global battery2
        battery2='y'
        var5.set(1)
    def noPush3():
        global battery2
        battery2='n'
        var5.set(1)
        
#    Battery2 = input("Are there more than two batteries? [y/n]: ")
    batQuestion2=Label(window, text="Are there more than two batteries?")
    yeButton3=Button(window, text="Yes", command=yePush3)
    noButton3=Button(window, text="No", command=noPush3)
    
    batQuestion2.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    yeButton3.grid(row=2, column=1, padx=10, pady=10)
    noButton3.grid(row=2, column=2, padx=10, pady=10)
    
    yeButton3.wait_variable(var5)
    
    batQuestion2.grid_forget()
    yeButton3.grid_forget()
    noButton3.grid_forget()
    
    if battery2 == 'y':
        var6=tk.IntVar()
        def yePush4():
            global Label2
            Label2='y'
            var6.set(1)
        def noPush4():
            global Label2
            Label2='y'
            var6.set(1)
#        Label2 = input("Is there a lit indicator labeled 'FRK'? [y/n]: ")
        frkQuestion=Label(window, text="Is there a lit indicator labeled 'FRK'?")
        yeButton4=Button(window, text="Yes", command=yePush4)
        noButton4=Button(window, text="No", command=noPush4)
        
        frkQuestion.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        yeButton4.grid(row=2, column=1, padx=10, pady=10)
        noButton4.grid(row=2, column=2, padx=10, pady=10)
        
        yeButton4.wait_variable(var6)
        
        frkQuestion.grid_forget()
        yeButton4.grid_forget()
        noButton4.grid_forget()
        
    
        if Label2 == 'y':
#            print(color.BOLD + "-> Press and immediately release the button" + color.END)
            holRelButton.grid(row=0, column=1, padx=10, pady=10)
            exButton.grid(row=1, column=1, padx=10, pady=10)
            exButton.wait_variable(exvar)
            exit()
        else:
            pass
    else:
        pass
else:
    pass

#STEP 5
if Held == '0' and Color == '3':
#    print(color.BOLD + "-> Press and hold the button" + color.END)
    holdButLab.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
    Held = '1'
else:
    pass
    
#STEP 6
if Held == '0' and Color == '4' and Text == '3':
#    print(color.BOLD + "-> Press and immediately release the button" + color.END)
    holRelButton.grid(row=0, column=1, padx=10, pady=10)
    exButton.grid(row=1, column=1, padx=10, pady=10)
    exButton.wait_variable(exvar)
    exit()
else:
    pass

#STEP 7
if Held == '0':
#	print(color.BOLD + "-> Press and hold the button" + color.END)
    holdButLab.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
else:
	pass

#RELEASING A HELD BUTTON
#GATHER INFO

#Strip = input("What color is the strip to the right of the module? [1-Blue, 2-White, 3-Yellow, 4-Other]: ")
var7=tk.IntVar()
def bluePush2():
    global Strip
    Strip='1'
    var7.set(1)
def whitePush2():
    global Strip
    Strip='2'
    var7.set(1)
def yellowPush2():
    global Strip
    Strip='3'
    var7.set(1)
def otherPush():
    global Strip
    Strip='4'
    var7.set(1)
    
bluButton2=Button(window, text="Blue", bg="blue", command=bluePush2)
whitButton2=Button(window, text="White", bg="white", command=whitePush2)
yellButton2=Button(window, text="Yellow", bg="yellow", command=yellowPush2)
othButton=Button(window, text="Other", command=otherPush)

stripQuestion.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
bluButton2.grid(row=2, column=1, padx=10, pady=10)
whitButton2.grid(row=2, column=2, padx=10, pady=10)
yellButton2.grid(row=2, column=3, padx=10, pady=10)
othButton.grid(row=2, column=4, padx=10, pady=10)

othButton.wait_variable(var7)

stripQuestion.grid_forget()
bluButton2.grid_forget()
whitButton2.grid_forget()
yellButton2.grid_forget()
othButton.grid_forget()
holdButLab.grid_forget()

if Strip == '1':
#    print(color.BOLD + "-> Release when the countdown timer has a 4 in any position" + color.END)
    ans1.grid(row=0, column=1, padx=10, pady=10)
    exButton.grid(row=1, column=1, padx=10, pady=10)
    exButton.wait_variable(exvar)
    exit()
elif Strip == '2':
#    print(color.BOLD + "-> Release when the countdown timer has a 1 in any position" + color.END)
    ans2.grid(row=0, column=1, padx=10, pady=10)
    exButton.grid(row=1, column=1, padx=10, pady=10)
    exButton.wait_variable(exvar)
    exit()
elif Strip == '3':
#    print(color.BOLD + "-> Release when the countdown timer has a 5 in any position" + color.END)
    ans3.grid(row=0, column=1, padx=10, pady=10)
    exButton.grid(row=1, column=1, padx=10, pady=10)
    exButton.wait_variable(exvar)
else:
#    print(color.BOLD + "-> Release when the countdown timer has a 1 in any position" + color.END)
    ans2.grid(row=0, column=1, padx=10, pady=10)
    exButton.grid(row=1, column=1, padx=10, pady=10)
    exButton.wait_variable(exvar)
    
window.mainloop()