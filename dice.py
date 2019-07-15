import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print ("Rolling the dice...")
    print ("The value is...")
    print (random.randint(min,max))
    break
print ("Would you like to roll again?")