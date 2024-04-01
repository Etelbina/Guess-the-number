import random

secret_number = random.randint(1,100)
cow_guess = random.randint(1,100)
print("Cow says: -Hi!! I'm cow.\n\t  -The system has a secret number between 1 to 100.\n\t  -Do you want to guess? Then write a number bellow\n")
user_input = input()
if user_input == str(secret_number):
  print(f"\nCow says: -You won!! The secret number is {secret_number}")
elif int(user_input) > secret_number:
  print(f"The secret number is {secret_number}")
  cow_guess = random.randint(1,int(user_input))
  print(f"\nCow says: -You went too far. It's my turn!! My guess is: {cow_guess}")
else:
  print(f"The secret number is {secret_number}")
  print(f"\nCow says: -You fell short. It's my turn!! My guess is: {cow_guess}")
  cow_guess = random.randint(int(user_input), 100)
