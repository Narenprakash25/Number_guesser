import random

top_num=input("type a num:")

if top_num.isdigit():
    top_num=int(top_num)
    if top_num<=0:
        print("type a num greater than zero")
        quit()
else:
    print("type a num next time")
    quit()

rand_num=random.randint(0,top_num)


guess=0
while True:
    guess+=1
    random_guess = input("make a random guess:")

    if random_guess.isdigit():
        random_guess=int(random_guess)

    else:
        print("type a num next time")
        continue

    if random_guess==rand_num:
        print("YOU R CORRECT!")
        break
    else:
        if random_guess>rand_num:
            print("YOU R ABOVE THE NUM")
        else:
            print("YOU R BELOW THE NUM")




print("U HAVE GOT IT IN  "+str(guess)+"  GUESS")





