import random

secret_number = random.randint(1,100)
cow_guess = random.randint(1,100)

print("\n\033[47mSystem:\033[0m  Secret number: (??) \n")
print(" Cow:\t\033[33m Hi!! I'm cow.\n\
      \t The system has a secret number between 1 to 100.\n\
      \t We have 10 opportunities. Do you want to guess?\n\
      \t Then write a number bellow.\n\033[0m")
print(secret_number)
user_input = input("-Shift #1 Write your guess: ")
    
i = 1
while i <= 10:
  print(f"\nYou:\t\033[45m {user_input} \033[0m")
  if (int(user_input) == secret_number) or (cow_guess == secret_number):
    break
  if(int(user_input) > secret_number):
    print("-You went to far")
    print(f" Cow:\t\033[33mIt's my turn!! My guess is: {cow_guess}\n\033[0m")
    cow_guess = random.randint(1,int(user_input))
  else:
    print("-You fell short")
    print(f" Cow:\t\033[33mNow me. My guess is: {cow_guess}\n\033[0m")
  user_input = input(f"Shift #{i+1} Write your guess ✏︎ ")
  cow_guess = random.randint(int(user_input),100)
  i += 1

if (int(user_input) == secret_number):
	print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mYou won!!!\n\033[0m")
elif (cow_guess == secret_number ):
    print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mI won!!!\n\033[0m")
else:
    print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mWe both loose against the system...\n\033[0m")