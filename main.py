import random

min = 1
max = 100
secret_number = random.randint(min,max)
cow_guess = 0
user_input = int("0")

print(" ___\n|[_]|\n|+ ;| \033[47m System: \033[0m Secret number: (??) \n`---'\n")
print(    "_(~)_\t  Cow: \033[33m Hi!! I'm cow.\033[0m\n )\"(\t   \033[33m     The system has a secret number between 1 to 100.\033[0m\n(@_@)\t\033[33m        We have 10 opportunities. Do you want to guess?\033[0m\n ) (\033[33m\t\tThen write a number bellow.\033[0m\n")
print("secret:", secret_number, "// min:", min, "max:", max)
    
i = 1
while i != 10:
  user_input = input(f"Shift #{i} Write your guess ✏︎ ")
  print(f"  //\n ('')    User:  \033[45m {user_input} \033[0m\n / rr\n*\\ ))_")
  #------------------------user guess well------------------------
  if (int(user_input) == secret_number) or (cow_guess == secret_number):
    break
  #------------------------if user guess is bigger------------------------
  elif (int(user_input) > secret_number):
    print("-You went to far\n")
    if (int(user_input) < max): #reset max or min number
       max = int(user_input) #reset the max number
    cow_guess = random.randint(min,max-1) #cow makes new guess
    #------------------------cow shift------------------------
    print(f"_(~)_\n )\"(\n(@_@)\t   Cow:\t\033[33mIt's my turn!! My guess is: {cow_guess}\033[0m\n ) (")
    if ((cow_guess > secret_number) and (cow_guess < max)): #reset max or min number
        max = cow_guess
    elif ((cow_guess < secret_number) and (cow_guess > min) ):
        min = cow_guess
        print("secret:", secret_number, "min:", min, "max:", max ) #print to check
  #------------------------if user guess lower------------------------
  else:
    print("-You fell short\n") #let know the user
    if (int(user_input) > min):
        min = int(user_input) #reset the min number
    cow_guess = random.randint(min+1,max) #cow makes new guess
    #------------------------cow shift------------------------
    print(f"_(~)_\n )\"(\n(@_@)\t   Cow:\t\033[33mNow me! My guess is: {cow_guess}\033[0m\n ) (")
    if ((cow_guess > secret_number) and (cow_guess < max)): #reset max or min number
        max = cow_guess
    elif ((cow_guess < secret_number) and (cow_guess > min) ):
        min = cow_guess
    print("secret:", secret_number, "min:", min, "max:", max ) #print to check
    #------------------------------------------------
  i += 1 #shift index added

# when loop ends we notify winner
if (int(user_input) == secret_number):
	print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mYou won!!!\n\033[0m")
elif (cow_guess == secret_number ):
    print(f"\n-End of the game. The secret number is {secret_number}\nCow:\t\033[33mI won!!!\n\033[0m")
else:
    print(f"\n-End of the game. The secret number is {secret_number}\n\
        Cow:\t\033[33mWe both lost against the system...\n\033[0m")
    
# corregir break y mensajes finales de la vaca estrategia de mitadespara la vaca