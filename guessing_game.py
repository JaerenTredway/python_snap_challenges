secret_word = "opensesame"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1

if guess != secret_word:
    print("ACCESS DENIED")
else:
    print("ACCESS AUTHORIZED")
    
