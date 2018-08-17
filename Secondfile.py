print("Welcome to guessing game")
score=0
print("score=0")

answer=input("What season is it now? \n")

print(answer)


if answer=="summer":
    print("Correct! You have 1 score")
    score=score+1
else:
    print("Not correct, try again!")


answertwo=input("What month is it now? \n")

if answertwo=="august":
    print("Correct!")
    score=score+1
else:
    print("Oops! Not correct!")

if score==0:
    print("Oops too bad! Only got {} score".format(score))

elif score <2:
    print("Almost got it, you got {} score".format(score))

elif score==2:
    print("Perfect! You got {} score".format(score))

