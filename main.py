# import random

# secret_number = random.randint(1,100)
# cow_guess = random.randint(1,100)
# print("Cow says: -Hi!! I'm cow.\n\t   The system has a secret number between 1 to 100.\n\t   Do you want to guess? Then write a number bellow\n")
# user_input = input()
# if user_input == str(secret_number):
#   print(f"\nSystem says: -End of the game. The secret number is {secret_number}\
#         \n\nCow says: -You won!!!!!\n")
# elif int(user_input) > secret_number:
#   cow_guess = random.randint(1,int(user_input))
#   print(f"\nSystem says: -You went too far.\
#         \n\nCow says: -It's my turn!! My guess is: {cow_guess}")
#   if cow_guess == secret_number:
#     print(f"\nSystem says: -End of the game. The secret number is: {secret_number}\
#           \n\nCow says: -I won!!!!!!\n")
#   else:
#     print(f"\nSystem says: -End of the game. The secret number is: {secret_number}\
#           \n\nCow says: -We both lost...\n")
# else:
#   print(f"\nSystem says: -You fell short.\
#         \n\nCow says: -It's my turn!! My guess is: {cow_guess}")
#   cow_guess = random.randint(int(user_input), 100)
#   if cow_guess == secret_number:
#     print(f"\nSystem says: -End of the game. The secret number is: {secret_number}\
#         \n\nCow says: -I won!!!!!!\n")
#   else:
#     print(f"\nSystem says: -End of the game. The secret number is: {secret_number}\
#           \n\nCow says: -We both loose...\n")


# Colors
# print("\033[31mThis is red font.\033[0m")
# print("\033[45m For user\033[0m")
# print("\033[30;43m For Cow \033[0m")
# print("\033[47m Highlighted Gray Text\033[0m")
# print("\033[33mThis is yellow font may be for cow.\033[0m")
