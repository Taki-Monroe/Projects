import random

chances = 10
numrange = 1000
num2guess = random.randrange(numrange)

print(f"Hi! Welcome to number guessing game.\nYou have {chances} chances left to guess. The number is between 0 to {numrange-1}." )

while chances > 0:
 try:
  user_guess = int(input(f"What's your guess? {chances} tries left. \n"))
  if user_guess == num2guess and chances > 0:
    print(f"Correct, it was {num2guess}.")
    break
  elif user_guess < num2guess and chances > 0:
      if num2guess - user_guess <= 10:
          print("Too small but close enough.")
      else:
          print(f"Too small.")
  elif user_guess > num2guess and chances > 0:
      if user_guess - num2guess <= 10:
          print("Too big but close enough.")
      else:
          print(f"Too big.")
  chances = chances - 1
  if chances == 0:
    print(f"Game Over! It was {num2guess}.")
 except:
  print("Invalid input.")
