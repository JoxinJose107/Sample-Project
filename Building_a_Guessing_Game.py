#**********Building a guessing game************

# The basic idea is we will specify a secret word which is stored in the program and the user can interact with the program and try to guess the secret word. The user has to keep guessing until he gets the correct secret word..

#Creating  a variable to store our secret word..

print("The Greatest Football Player of All Time!!")
secret_word="Cristiano Ronaldo"

# Creating a variable that can store users guess.
guess_word=""
guess_count=0
guess_limit=3
out_of_guesses=False  #It tells us whether the user is out of guesses or not.

while guess_word!=secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess_word=input("Enter the guess: ")
        guess_count+=1
    else:
       out_of_guesses=True

if out_of_guesses:
    print("You loose!!!")
else:
    print("You Win!!!")


    
    

