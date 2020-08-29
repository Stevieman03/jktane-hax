#ON THE SUBJECT OF MEMORY

class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   
superVar=0
while superVar==0:
    #GATHER INFO
    Display = input("S1: What number is displayed? [1,2,3,4]: ")
    #STAGE 1
    if Display == '1':
        print(color.BOLD + "-> Press the button in the second position" + color.END)
        P1 = 'second'
        superVar=1
    elif Display == '2':
        print(color.BOLD + "-> Press the button in the second position" + color.END)
        P1 = 'second'
        superVar=1
    elif Display == '3':
        print(color.BOLD + "-> Press the button in the third position" + color.END)
        P1 = 'third'
        superVar=1
    elif Display == '4':
        print(color.BOLD + "-> Press the button in the fourth position" + color.END)
        P1 = 'fourth'
        superVar=1
    else:
        print(color.BOLD + "Invalid entry" + color.END)
        
#STAGE 1.5
while superVar==1:
    L1 = input("What is the button labeled? [1,2,3,4]: ")
    if L1 !='1' and L1 !='2' and L1 !='3' and L1 != '4':
        print(color.BOLD + "Invalid entry" + color.END)
    else:
        superVar=2
    
#STAGE 2
while superVar==2:
    Display2 = input("S2: What number is displayed? [1,2,3,4]: ")
    if Display2 == '1':
        print(color.BOLD + "-> Press the button labeled '4'" + color.END)
        L2 = '4'
        superVar=3
    elif Display2 == '2':
        print(color.BOLD + "-> Press the button in the " + P1 + " position" + color.END)
        P2 = P1
        superVar=3
    elif Display2 == '3':
        print(color.BOLD + "-> Press the button in the first position" + color.END)
        P2 = 'first'
        superVar=3
    elif Display2 =='4':
        print(color.BOLD + "-> Press the button in the " + P1 + " position" + color.END)
        P2 = P1
        superVar=3
    else:
        print(color.BOLD + "Invalid entry" + color.END)
    
#STAGE 2.5
while superVar==3:
    if Display2 == '1':
        P2 = input("What position is that in? [1,2,3,4]: ")
        #P2 CONVERSION - POSSIBLY USE A DICTIONARY INSTEAD
        if P2 == '1':
            P2 = 'first'
            superVar=4
        elif P2 == '2':
            P2 = 'second'
            superVar=4
        elif P2 == '3':
            P2 = 'third'
            superVar=4
        elif P2 == '4':
            P2 = 'fourth'
            superVar=4
        else:
            print(color.BOLD + "Invalid entry" + color.END)
            continue
    else:
        L2 = input("What is the button labeled? [1,2,3,4]: ")
        if L2 != '1' and L2 != '2' and L2 != '3' and L2 != '4':
            print(color.BOLD + "Invalid entry" + color.END)
            continue
        else:
            superVar=4
        
        
    
#STAGE 3
while superVar==4:
    Display3 = input("S3: What number is displayed? [1,2,3,4]: ")
    if Display3 == '1':
        print(color.BOLD + "-> Press the button labeled '" + L2 + "'" + color.END)
        L3 = L2
        superVar=5
    elif Display3 == '2':
        print(color.BOLD + "-> Press the button labeled '" + L1 + "'" + color.END)
        L3 = L1
        superVar=5
    elif Display3 == '3':
        print(color.BOLD + "-> Press the button in the third possition" + color.END)
        P3 = 'third'
        superVar=5
    elif Display3 == '4':
        print(color.BOLD + "-> Press the button labeled '4'" + color.END)
        L3 = '4'
        superVar=5
    else:
        print(color.BOLD + "Invalid entry" + color.END)
        
#STAGE 3.5
while superVar==5:
    if Display3 == '3':
        L3 = input("What is the button labeled? [1,2,3,4]: ")
        if L3 != '1' and L3 != '2' and L3 != '3' and L3 != '4':
            print(color.BOLD + "Invalid entry" + color.END)
            continue
        else:
            superVar=6
    else:
        P3 = input("What position is that in? [1,2,3,4]: ")
        #P3 CONVERSION
        if P3 == '1':
            P3 = 'first'
        elif P3 == '2':
            P3 = 'second'
        elif P3 == '3':
            P3 = 'third'
        else:
            P3 = 'fourth'
        superVar=6

#STAGE 4
while superVar==6:
    Display4 = input("S4: What number is displayed? [1,2,3,4]: ")
    if Display4 == '1':
        print(color.BOLD + "-> Press the button in the " + P1 + " position" + color.END)
        P4 = P1
        superVar=7
    elif Display4 == '2':
        print(color.BOLD + "Press the button in the first position" + color.END)
        P4 = 'first'
        superVar=7
    elif Display4 == '3' or Display4 == '4':
        print(color.BOLD + "Press the button in the " + P2 + " position" + color.END)
        P4 = P2
        superVar=7
    else:
        print(color.BOLD + "Invalid entry" + color.END)

#STAGE 4.5
while superVar==7:
    L4 = input("What is the button labeled? [1,2,3,4]: ")
    if L4 != '1' and L4 != '2' and L4 != '3' and L4 != '4':
        print(color.BOLD + "Invalid entry" + color.END)
    else:
        superVar=8
    
#STAGE 5
while superVar==8:
    Display5 = input("S5: What number is displayed? [1,2,3,4]: ")
    if Display5 != '1' and Display5 != '2' and Display5 != '3' and Display5 != '4':
        print(color.BOLD + "Invalid entry" + color.END)
    else:
        superVar=900

if Display5 == '1':
    print(color.BOLD + "Press the button labeled '" + L1 + "'" + color.END)
elif Display5 == '2':
    print(color.BOLD + "Press the button labeled '" + L2 + "'" + color.END)
elif Display5 == '3':
    print(color.BOLD + "Press the button labeled '" + L4 + "'" + color.END)
elif Display5 == '4':
    print(color.BOLD + "Press the button labeled '" + L3 + "'" + color.END)