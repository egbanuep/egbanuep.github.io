import random
print ("welcome to the guess my number hardcore edition ")
print ("In this program you only get 5 guesses\n")
print ("You are to guess a number between 1 and 25...good luck")


the_number = random.randint(1,25)

guesses = 0
while guesses < 5:

    guess = int(input("What's the number?"))
    guesses +=1

    if guess > the_number:
        print ("Lower")
    elif guess < the_number:
        print ("Higher")
    elif guess == the_number:
        break

while guess != the_number:

    if guesses == 5:
        print ("Sorry, You ran out of guesses!!")
    break

else:

        print("You guessed it!!, the number is", the_number, "and it only"
        "took you", guesses , "tries")