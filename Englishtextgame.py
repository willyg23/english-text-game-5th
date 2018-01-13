from time import sleep
print("Name: Gordon Freeman")
sleep(1)
print("Date: 1/10/2018")
sleep(1)
print("Location: WD High School")
sleep(1)
print("It's the afternoon, a period after lunch, and you walk down to your 6th period science class.")
sleep(3)
print("You sit down in your seat waiting for Mrs. Bowles to begin class.")
sleep(3)
print("Ms. Bowles is a little late today, so you close your eyes for a little bit")
sleep(3)
print("Bowles: Alright class, today I have a math problem for you to solve.")
sleep(2)
print("Bowles: If you get it wrong, you will be kicked out of school.")
sleep(2)
print("Bowles: If you get it right, you'll have an open for the rest of the period.")
sleep(3)
print("Bowles: Is the number I'm thinking of odd or even?")
sleep(1)

while (True):
    firstans = input("What do you answer? ")
    # Use .lower to make input lowercase to make answering easier
    if firstans.lower() == "odd":
        print("You chose odd!")
        sleep(1)
        # "break" breaks you out of a loop
        break
    elif firstans.lower() == "even":
        print("You chose even!")
        sleep(1)
        break
    else:
        print("Wow, you're really the dumbest, most idiotic student i've ever had. Odd or even")

print("Pain sears across your face as Ms. Bowles smacks you with a ruler." )
sleep(1)
print("YOU CHOSE WRONG TODAY SON! YOU'RE EXPELLED")
sleep(1)
print("You jolt awake from your dream, with the whole class staring at you.")
sleep(2)
print("Kid behind you: What a nice kid")
sleep(1)
print("Bowles: Jeez Gordon, fall asleep like that again and I'll have to whack you.")
sleep(2)
print ("The bell rings, you gather your stuff and hurry out of class.")
sleep(2)
print ("As you gather your things at your locker, you see a ruler on the floor.")
sleep(2)
ruler = False

while (True):
    answer = input("Do you pick it up?" )
    if answer.lower() in ['y', 'yes']:
        ruler = True
        print("You pick up the ruler!")
        sleep(1)
        break
    elif answer.lower() in ['n', 'no']:
        ruler = False
        print("You leave the ruler on the ground.")
        sleep(1)
        break
    else:
        print("Wow, am I high right now? I need to think 'yes' or 'no' not "+answer)
