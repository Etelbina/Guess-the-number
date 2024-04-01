import random

secret_number = random.randint(1,100)
print("Cow says: -Hi!! I'm cow.\n\t  -The system has a secret number between 1 to 100.\n\t  -Do you want to guess? Then write a number bellow\n")
user_input = input()
if user_input == str(secret_number):
  print(f"\nCow says: -You won!! The secret number is {secret_number}")
elif int(user_input) > secret_number:
  print(f"\nCow says: -You went too far. The secret number is {secret_number}")
  secret_number = random.randint(1,int(user_input))
  print(f"the range is now 1 to {user_input}. Now the secret is {secret_number}")
else:
  print(f"\nCow says: -You fell short. The secret number is {secret_number}")
  secret_number = random.randint(int(user_input), 100)
  print(f"the range is now {user_input} to 100. Now the secret is {secret_number}")