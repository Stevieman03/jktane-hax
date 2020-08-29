#35 WORDS
possible_words = [
"about", "after", "again", "below", "could",
"every", "first", "found", "great", "house",
"large", "learn", "never", "other", "place",
"plant", "point", "right", "small", "sound",
"spell", "still", "study", "their", "there",
"these", "thing", "think", "three", "water",
"where", "which", "world", "would", "write",
]
# Blank list to contain any possible matches
possible_matches = [] 


def firstLetter():
    colIn = input("COL1: Enter all letters: ")
    test = []
    counter=0
    inLen=len(colIn)

    while inLen != counter:
        test.append(colIn[counter].lower())
        counter+=1

    #remove dups and convert set back to list - sets have no order so letters get scrambled
    test=set(test)   
    test=list(test)
    print(test)

    loopVar=len(test)
    superCount=0
    while superCount < loopVar:
        #LOOP SEC - FIRST LETTER
        counter=0
        while counter < 35:
            if possible_words[counter][0] == test[superCount]: #Do with for loop?
                possible_matches.append(possible_words[counter])
            counter+=1

        superCount+=1
    print(possible_matches)
    
    
def secondLetter():
    #ASK QUESTION   
    colIn = input("COL2: Enter all letters: ")
    inLen=len(colIn)
    counter=0
    test=[]
    while inLen != counter:
        test.append(colIn[counter].lower())
        counter+=1
    #remove dups and convert set back to list - sets have no order so letters get scrambled
    test=set(test)   
    test=list(test)
    print(test)
    
    #COMPARE AND REMOVE NON MATCHES - THIS IS SUPER SHIT AND SHOULD BE FIXED
    container=[]
    for i in possible_matches:
        for j in test:
            if i[1]==j:
                container.append(i)
    return(container)


def thirdLetter():
    #ASK QUESTION   
    colIn = input("COL3: Enter all letters: ")
    inLen=len(colIn)
    counter=0
    test=[]
    while inLen != counter:
        test.append(colIn[counter].lower())
        counter+=1
    #remove dups and convert set back to list - sets have no order so letters get scrambled
    test=set(test)   
    test=list(test)
    print(test)
    
    #COMPARE AND REMOVE NON MATCHES - THIS IS SUPER SHIT AND SHOULD BE FIXED
    container=[]
    for i in possible_matches:
        for j in test:
            if i[2]==j:
                container.append(i)
    return(container)


def fourthLetter():
    #ASK QUESTION   
    colIn = input("COL3: Enter all letters: ")
    inLen=len(colIn)
    counter=0
    test=[]
    while inLen != counter:
        test.append(colIn[counter].lower())
        counter+=1
    #remove dups and convert set back to list - sets have no order so letters get scrambled
    test=set(test)   
    test=list(test)
    print(test)
    
    #COMPARE AND REMOVE NON MATCHES - THIS IS SUPER SHIT AND SHOULD BE FIXED
    container=[]
    for i in possible_matches:
        for j in test:
            if i[3]==j:
                container.append(i)
    return(container)


def fifthLetter():
    #ASK QUESTION   
    colIn = input("COL3: Enter all letters: ")
    inLen=len(colIn)
    counter=0
    test=[]
    while inLen != counter:
        test.append(colIn[counter].lower())
        counter+=1
    #remove dups and convert set back to list - sets have no order so letters get scrambled
    test=set(test)   
    test=list(test)
    print(test)
    
    #COMPARE AND REMOVE NON MATCHES - THIS IS SUPER SHIT AND SHOULD BE FIXED
    container=[]
    for i in possible_matches:
        for j in test:
            if i[4]==j:
                container.append(i)
    return(container)

    
#FIRST LETTER
firstLetter()
#SECOND LETTER
if len(possible_matches)>1:
    possible_matches=secondLetter()
    if len(possible_matches)>1:
        print(possible_matches)
#THIRD LETTER
if len(possible_matches)>1:
    possible_matches=thirdLetter()
    if len(possible_matches)>1:
        print(possible_matches)
#FOURTH LETTER
if len(possible_matches)>1:
    possible_matches=fourthLetter()
    if len(possible_matches)>1:
        print(possible_matches)
#FIFTH LETTER
if len(possible_matches)>1:
    possible_matches=fifthLetter()
    if len(possible_matches)>1:
        print(possible_matches)
    
if len(possible_matches) ==1:
    print("The word is:", *possible_matches)
          
if len(possible_matches) ==0:
    print("You fucked up")


'''
#SECOND LETTER
counter=0
while counter < 35:
    if possible_words[counter][0] == test[1]:
        possible_matches.append(possible_words[counter])
    counter+=1
print(possible_matches)


#FUTURE USE? USE FOR SECOND SHIT WHEN REMOVING DONGS FROM LIST
counter=0
count=len(possible_matches)
while counter <= count:
    if possible_matches[counter][0] != test[1]:
        possible_matches.remove(possible_words[counter])
    counter+=1
print(possible_matches)

#ISOLATE SECOND LETTER - WORKS BUT DONT NEED IT
    secondLet=[]
    #GET SECOND LETTER FROM POSSIBLE MATCHES
    lenList=len(possible_matches)
    counter2=0
    while counter2 < lenList:
        secondLet.append(possible_matches[counter2][1])
        counter2+=1

        
    #remove dups and convert set back to list - sets have no order so letters get scrambled
    secondLet=set(secondLet)   
    secondLet=list(secondLet)
    print(secondLet)

'''