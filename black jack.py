import random

def deposit():
    while True:
        n=input("how much money do you wish to deposit  $")
        if n.isdigit():
            n=float(n)
            if n>0:
                break
            else:
                print("pls give an amount bigger than zero  $")
        else:
            print("pls give an amount  $")
    return n
def bet():
    while True:
        a=input("how much money do you wish to bet  $")
        if a.isdigit():
            a=float(a)
            if a>0:
                break
            else:
                print("pls give an amount bigger than zero  $")
        else:
            print("pls give an amount  $")
    return a
#deck
deck=[2,3,4,5,6,7,8,9,10,"A","Q","J","K"]*4
playerhand=[]
dealerhand=[]
player=True
dealer=True
#givecard
def give_cards(hand):
    card= random.choice(deck)
    hand.append(card)
    deck.remove(card)

#total
def total(hand):
    total=0
    face=["Q","K","J"] 
    for card in hand:
        if card in range(1,11):
            total+=card
        elif card in face:
            total+=10
        else:
            if total>11:
                total+=1
            else:
                total+=11
    return total
#check win
def dealershand():
    if len(dealerhand)==2:
        return dealerhand[0]
    elif len(dealerhand)>2:
        return dealerhand[0],dealerhand[1]
#play
for _ in range(2):
    give_cards(playerhand)
    give_cards(dealerhand)
d=deposit()
while True:
    x=bet()
    if x>d:
        print ("you dont have enough money for that bet")
    else:
        break
t=d-x
print(playerhand)
print(dealerhand)
p="you have ",playerhand,"and a total of ",total(playerhand)
d="dealer has ",dealerhand,"and a total of ",total(dealerhand)
win=False
print (total(playerhand))
print(total(dealerhand))
while player or dealer:
    if player:
        nextmove=input("1:stay or 2:hit")
        if nextmove=="1":
            player=False
        else:
            give_cards(playerhand)
            print(playerhand,total(playerhand))
    if total(dealerhand)>16:
        dealer=False
    else:
        give_cards(dealerhand)
    if total(playerhand)>=21:
        break
    elif total(dealerhand)>=21:
        break
if total(playerhand)==21:
    print(p,d,"blackjack! you win")
    win=True
elif total(dealerhand)==21:
     print(p,d,"blackjack!dealer wins")
elif total(playerhand)>21:
    print(p,d,"you lose")
elif total(dealerhand)>21:
    print(p,"dealer has",dealerhand,"and a total",total(dealerhand),"dealer loses")
elif total(playerhand)==total(dealerhand):
    print(p,d,"its a draw")
elif total(playerhand)<21 and total(dealerhand)<21:
    if total(playerhand)>total(dealerhand):
        print (p,d,"you win")
        win=True
    else:
        print(p,d,"you lose")
if win==True:
    x=x*2
    t=t+x
    d=t
    print("your total in now",d)
else:
    print("your total in now",t)     
       
