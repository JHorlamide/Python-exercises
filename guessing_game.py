# Guessing game
secrete_number = 5
number_of_guess = 0
guess_limit = 3

while number_of_guess < guess_limit:
  guess = int(input('Guess a number: '))
  number_of_guess += 1

  if(guess == secrete_number):
    print(f"You won! {guess} is the correct number")
    break
else:
  print("Sorry you failed")
  

