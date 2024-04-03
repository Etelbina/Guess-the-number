import random

min = 1
max = 100
secret_number = random.randint(min,max)
cow_guess = 0
user_input = int("0")

print(" ___\n|[_]|\n|+ ;| \033[47m System: \033[0m Hi \n`---'\n")
print(    "_(~)_\n )\"(\n(@_@)     Cow: \033[33m  Hi\033[0m\n ) (\n")
print("  //\n ('>     User:  \033[45m Hi \033[0m\n /rr\n*\\))_\n")

print("\n\033[47mSystem:\033[0m  Secret number: (??) \n")
print(" Cow:\t\033[33m Hi!! I'm cow.\n\
      \t The system has a secret number between 1 to 100.\n\
      \t We have 10 opportunities. Do you want to guess?\n\
      \t Then write a number bellow.\n\033[0m")
#print("secret:", secret_number, "// min:", min, "max:", max)
    
i = 1
while (i != 10) or (int(user_input) != secret_number) or (cow_guess != secret_number):
  user_input = input(f"Shift #{i} Write your guess ✏︎ ")
  print(f"\nYou:\t\033[45m {user_input} \033[0m")
  #------------------------user guess well------------------------
  if (int(user_input) == secret_number) or (cow_guess == secret_number):
    break
  #------------------------if user guess is bigger------------------------
  elif (int(user_input) > secret_number):
    print("-You went to far")
    if (int(user_input) < max): #reset max or min number
       max = int(user_input) #reset the max number
    cow_guess = random.randint(min,max) #cow makes new guess
    #------------------------cow shift------------------------
    if (not (cow_guess == int(user_input))): #be sure cow dont use the same number as user
        print(f" Cow:\t\033[33mIt's my turn!! My guess is: {cow_guess}\n\033[0m") #cow guess printed
        if ((cow_guess > secret_number) and (cow_guess < max)): #reset max or min number
            max = cow_guess
        elif ((cow_guess < secret_number) and (cow_guess > min) ):
            min = cow_guess
        print("secret:", secret_number, "min:", min, "max:", max ) #print to check
    else:
       cow_guess = random.randint(min,max) #cow makes new guess
  #------------------------if user guess lower------------------------
  else:
    print("-You fell short") #let know the user
    if (int(user_input) > min):
        min = int(user_input) #reset the min number
    cow_guess = random.randint(min,max) #cow makes new guess
    if (not (cow_guess == int(user_input))): # be sure cow dont use the same number as user
        print(f" Cow:\t\033[33mNow me. My guess is: {cow_guess}\n\033[0m") #cow guess printed
        if ((cow_guess > secret_number) and (cow_guess < max)): #reset max or min number
            max = cow_guess
        elif ((cow_guess < secret_number) and (cow_guess > min) ):
            min = cow_guess
        print("secret:", secret_number, "min:", min, "max:", max ) #print to check
    else:
       cow_guess = random.randint(min,max) #cow makes new guess
    #------------------------------------------------
  i += 1 #shift index added

# when loop ends we notify winner
if (int(user_input) == secret_number):
	print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mYou won!!!\n\033[0m")
elif (cow_guess == secret_number ):
    print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mI won!!!\n\033[0m")
else:
    print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mWe both lost against the system...\n\033[0m")
    
# estrategia de mitadespara la vaca