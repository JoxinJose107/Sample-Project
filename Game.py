
print("Greatest player of all time")
guessword=""
secret_word="Cristiano Ronaldo"
guess_count=0
guess_limit=3

while guessword!=secret_word:
    if guess_count<=guess_limit:
        guessword=input("Enter the guess")
        guess_count+=1
    else:
        print("Out of chances....You Loose")

print("You Win")

