import random

  #------------------------ game functions ------------------------
def welcome_game():
    print(computer_says("Secret number: (??)"))
    print("_(~)_\t  Cow: \033[33m Hi!! I'm Cow.\033[0m\n )\"(\t   \033[33m     The system has a secret number between 1 to 100.\033[0m\n(@_@)\t\033[33m        We have 10 opportunities. Do you want to guess?\033[0m\n ) (\033[33m\t\tThen write a number bellow.\033[0m\n")
    game()

def game():
    min = 1
    max = 100
    secret_number = random_number(min,max)
    cow_guess = 0
    scores = []
    winner = ""
    i = 1
    while i !=11:
        print("secret:", secret_number, "// min:", min, "max:", max)
        user_input = user_shift(i)
        setting_scores(i, user_input, scores)
        # user shift ------------------
        if (int(user_input) == secret_number):
            winner = "user"
            end_game(secret_number, i, scores, winner)
            break
        else:
            if(int(user_input) > secret_number):
                print("\033[47m You went to far \033[0m\n")
                if (int(user_input) <= max):
                    max = int(user_input)-1
            else:
                print("\033[47m You fell short \033[0m\n")
                if (int(user_input) >= min):
                    min = int(user_input)+1
            # cow shift ------------------
            cow_guess =  random_number(min,max)
            if(cow_guess == secret_number):
                winner = "cow"
                end_game(secret_number, i, scores, winner)
                break
            elif (cow_guess > secret_number and cow_guess <= max):
                max = cow_guess-1
            elif (cow_guess < secret_number and cow_guess >= min):
                min = cow_guess+1
        i += 1
    # system winsn ------------------
    end_game(secret_number, i, scores, winner)

def end_game(secret_number, i, scores, winner):
    #print(scores)
    print(computer_says(f"End of the game. The secret number is {secret_number}"))
    if(winner == "user"):
        print(cow_says("You won!!!!!"))
    elif(winner == "cow"):
        print(cow_says("I won!!!"))
    elif(i == 11):
        print(cow_says("Oh no! We both lost against the system..."))
    for item in scores:
        print(item)
    play_again()

def play_again():
    print(computer_says("Do you want to play again?"))
    user_input = input(f"Write Y for yes and N for no ✏︎ ")
    if(user_input == "Y" or user_input == "y"):
        print(cow_says(f"Yay!! New game!!!!!!!!!!!!!"))
        print(computer_says(f"\033[47m New secret number: (??) \033[0m"))
        game()
    elif(user_input != "Y" or user_input != "y"):
        print(computer_says(f"\033[47m Shutting down... \033[0m"))
        print(cow_says(f"See you later!!"))

    #------------------------ shifts logic ------------------------
def user_shift(i):
    user_input = input(f"\nShift #{i} \033[47m Write your guess ✏︎ \033[0m ")
    print(user_says(user_input))
    return user_input

def cow_shift(min, max):
    cow_guess = random_number(min,max)
    #cow_guess = int((max - min) / 2) + min
    print(cow_says(f"It's my turn!! My guess is: {cow_guess}"))
    return cow_guess

def setting_scores(i, user_input, scores):
    scores.append(f"Your guess on shift #{i}: {user_input}")
    return scores

def random_number(min,max):
    return random.randint(min,max)
    
  #------------------------ message functions ------------------------
def computer_says(message):
    return f" ___\n|[_]|\n|+ ;|  System: \033[47m {message} \033[0m\n`---'\n"

def cow_says(message):
    return f"_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m {message}\033[0m\n ) (\n"

def user_says(message):
    return f"  //\n ('')    User:  \033[45m {message} \033[0m\n / rr\n*\\ ))_\n"

if __name__ == "__main__":
    welcome_game()

#registro de partidas y el ganador por partida