######################################
###- CC1-S01 Recursion
###- Reid A. Martin
###- October 29, 2021
######################################
#note: programmed with hatred and a cat licking my elbow
#note 2: yes i know this is being drawn backwards... but this is honestly the only way i could get it to work
#AND YOU SAID IT HAD TO PRODUCE SOMETHING SIMILAR NOT EXACT... and no i dont know how i did it...

#################

import turtle #imports turtle module

##############

go = True #sets while variable

run = 3 #number of runs variable set
size = 2 #size? variable set... I used to know what it did

branchLen = 40 #sets branch length

####################

t = turtle.Turtle() #sets turtle variable
myWin = turtle.Screen() #sets up screen

t.left(90) #puts turtle in position and sets his colour
t.color("green")

while go == True: #while loop

    if run == 3:
        if size == 2: #draws first branch
            t.right(60)
            t.backward(10)
            t.left(40)
            t.forward(10)
            t.backward(10)
            t.right(20)
            t.backward(20)
            size = size - 1
        elif size == 1: #draws second end branch with mid branch
            t.left(40)
            t.forward(20)
            t.right(20)
            t.forward(10)
            t.backward(10)
            t.left(40)
            t.forward(10)
            t.backward(10)
            t.right(20)
            t.backward(20)
            t.right(20)
            t.backward(30)
            t.left(40)
            size = size + 1
            run = run - 1
            
    elif run == 2:
        if branchLen >= 10: #draws path of branches on other side
            t.forward(branchLen - 10)
            branchLen = branchLen - 10
            t.left(20)            
        elif branchLen == 0: #sends turtle back up to finish the branch
            branchLen = branchLen + 5
            t.right(40)
            branchLen = 40
            run = run - 1
            
    elif run == 1:
        if size == 2: #takes back to second level of branch to draw one part
            t.backward(10)
            t.right(40)
            t.forward(10)
            t.backward(10)
            t.left(20)
            t.backward(20)
            t.right(40)
            size = size - 1            
        elif size == 1: #draws remaining branch
            t.forward(20)
            t.right(20)
            t.forward(10)
            t.backward(10)
            t.left(40)
            t.forward(10)
            t.backward(10)
            t.right(20)
            t.backward(20)
            size = size - 1        
        else: #takes turtle back home to the bottom
            t.left(20)
            t.backward(30)
            run = run + 10
            t.right(20)
            t.backward(branchLen)
            
    else:#ends the while loop
        go = False