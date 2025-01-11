import random
set={ "rock":1,
      "paper":2,
      "scissor":3  }
Score1=0
Score2=0

def computer():
    choice=random.randint(1,3)
    cp=""
    if choice==1:
        cp="rock"
    elif choice==2:
        cp="paper"
    else:
        cp="scissor"
    return cp

while Score1!=3 and Score2!=3:
    user=input("rock,paper,scissor:")
    cp=computer()
    if (set.get(user))-1==set.get(cp) or (set.get(user))+2==set.get(cp):
        Score1+=1    
    if (set.get(user))+1==set.get(cp) or (set.get(user))-2==set.get(cp):
        Score2+=1
    print(f"{cp}\n you:{Score1}   computer:{Score2}")
if Score1>Score2:
    print(f"you win")
else:
    print(f"you lose")
