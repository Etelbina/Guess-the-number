secret_number = 50
print("Cow says: -Hi!! I'm cow.\n\t  -The system has a secret number between 1 to 100.\n\t  -Do you want to guess? Then write a number bellow\n")
user_input = input()
if user_input == str(secret_number):
  print(f"\nCow says: -You won!! The secret number is {secret_number}")
elif int(user_input) > secret_number:
  print("\nCow says: -You went too far. Now is my turn")
else:
  print("\nCow says: -You fell short. Now is my turn")