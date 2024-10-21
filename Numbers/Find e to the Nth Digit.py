import math

MAX_DECIMAL_PLACES = 20

def calculate_e(n):
    return f"{math.exp(1):.{n}f}"

try:
 desired_places = int(input("What's your desired decimal places of e?"))
 if desired_places > MAX_DECIMAL_PLACES:
       print(f"Can't be more than {MAX_DECIMAL_PLACES}.")
 else:
       response = calculate_e(desired_places)
       print(f"Here it is: {response}")
except ValueError:
   print("Please enter a valid number.")
