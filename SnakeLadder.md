```python

import random as r
n_players=int(input("Enter the number of players "))
d={}
snake={45:7,51:10,38:20,76:54,97:61,91:73}
ladders={5:58,14:49,42:60,53:72,64:83,75:94}
for i in range(n_players):
    name=input("Enter the name of the player ")
    d.update({name:0})
won = False
while won!=True:
    for i in d:
        print(i,end=" ")
        input("press Enter to roll the dice")
        dice = r.randint(1,6)
        print(f"Dice => {dice}\n")
        if d[i]+dice <= 100:
            d[i]+=dice
        else:
            print("Exceeding")
        if d[i] in snake:
            print("Opps!! you got bitten by snake")
            d[i] = snake[d[i]]
        elif d[i] in ladders:
            print("congo!! you got a ladder")
            d[i] = ladders[d[i]]
        
        print(i,"you are at",d[i])
        if d[i] == 100:
            print("Congo you won",i)
            won = True
            break
    ```