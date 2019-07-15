import random

def  main():
    randnum = random.randint(1,10)
    tries = 5
    while tries > 0:
        guess = int(input("Guess a number between 1 and 10: "))
        if (guess == randnum):
            print("You Win")
            break
        else:
            print("Try again")
            tries = tries - 1
            print("You have " + str(tries) + " left")
    if (tries==0):
        print("You Lose")
        
if __name__ == "__main__":
    main()