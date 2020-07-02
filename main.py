# Make A game  Stone Paper & Scissor.
import random
W = 0
L = 0
D = 0 
def Score(a,b,c):
    global W
    global L
    global D
    W = W + a
    L = L + b
    D = D + c
    # print(f"Score is:-\n{name} Win {W} times\n{name} Loss {L} times\ngame Draw {D} times")
    print(f"Score is:-\n|\t{name}\t|\tcomputer\t|\tDraw\t|")
    print(f"|\t  {W}  \t|\t   {L}    \t|\t  {D} \t|")

print("\nWelcome to Stone Paper & Scissor Game")
print("\nRule Of the game is:-\nYou have to play the game 10 times with Computer\nIf you win maximum time then you will be winner other wise you loose this game")
input("press Enter continue")
# while(1): 
#     yn = input ("\nIf you want to play this game press Y\nIf you don't want to play this game press N\nEnter your Choise:- ")
#     if yn == 'y' or yn == 'Y':
#         break
#     elif yn == 'n' or yn =="N":
#         exit()
#     else:
#         print("Invalid Input! Try again.")
#         continue

while 1:
    name = input("\nEnter Your Name:- ")
    print("\nWelcome %s To this Game"%name)
    # input("To start the game press Enter")
    for i in range(10):
        while 1:
            print("\nChoose Any One:-\npress 1 for Stone\nPress 2 for Paper\nPress 3 for Scissor")
            try:
                user = int(input("Enter your choise:-"))
            except Exception as e:
                user = 12
            list1 = ["Stone", "Paper", "Scissor"]
            pc = random.choice(list1)
            pcs = "\nComputer Select ----> %s"%pc
            try:
                users = f"\n{name} Select ----> %s"%list1[int(user)-1]
            except Exception as e:
                print()
            win = "\nConguralations! You win this Round"
            loss = "\nSorry you Loss this the Round"
            draw = "\noops! This round is Draw"

            if (pc == "Stone"):
                if(int(user) == 1):
                    print(users,pcs,draw)
                    Score(0,0,1)
                    break
                elif(int(user) == 2):
                    print(users,pcs,win)
                    Score(1,0,0)
                    break
                elif(int(user) == 3):
                    print(users,pcs,loss)
                    Score(0,1,0)
                    break
                else:
                    print("Invalid!! please choose again.")
                    continue
            elif (pc == "Paper"):
                if(int(user) == 1):
                    print(users,pcs,win)
                    Score(0,1,0)
                    break
                elif(int(user) == 2):
                    print(users,pcs,draw)
                    Score(0,0,1)
                    break
                elif(int(user) == 3):
                    print(users,pcs,loss)
                    Score(1,0,0)
                    break
                else:
                    print("Invalid!! please choose again.")
                    continue
            elif (pc == "Scissor"):
                if(int(user) == 1):
                    print(users,pcs,loss)
                    Score(1,0,0)
                    break
                elif(int(user) == 2):
                    print(users,pcs,win)
                    Score(0,1,0)
                    break
                elif(int(user) == 3):
                    print(users,pcs,draw)
                    Score(0,0,1)
                    break
                else:
                    print("Invalid!! please choose again.")
                    continue
    print(f"\n\nThe final Score is:-\nOut of 10 rounds\n{name} Win {W} times\nComputer Win {L} times\ndraw {D} times")
    if(W < L):
        print(f"\nSorry!! {name} You Loss this Game againts Computer")
    elif(W == L):
        print(f"\nOpps!! It's Tie Between {name} And Computer")
    else:
        print(f"\nCongratulations! {name} You Win This Game")

    while(1): 
        print(f"\nHey {name} Hope You like this game")
        yn = input ("If you want to play this game Again press Y\npress N To exit the game\nEnter your Choise:- ")
        if yn == 'y' or yn == 'Y':
            W = 0
            L = 0
            D = 0 
            break
        elif yn == 'n' or yn =="N":
            exit()
        else:
            print("Invalid Input! Try again.")
            continue


