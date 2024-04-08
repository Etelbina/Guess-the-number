import random

class Player:
    def says(self, template):
        return print(template)
    def __init__(self, name, guess, games_played, games_won):
        self.name = name
        self.guess = guess
        self.games_played = games_played
        self.games_won = games_won

class Game:
    def start_game(self):
        self.game_number = 1
        self.shift_number = 1
        user_score = 0
        cow_score = 0
        system_score = 0
        winner = ""
        game.says(f" ___\n|[_]|\n|+ ;|  System: \033[47m Secret number: (??) \033[0m\n`---'\n")
        cow.says("_(~)_\t  Cow: \033[33m Hi!! I'm Cow.\033[0m\n )\"(\t   \033[33m     The system has a secret number between 1 to 100.\033[0m\n(@_@)\t\033[33m        We have 10 opportunities. Do you want to guess?\033[0m\n ) (\033[33m\t\tThen write a number bellow.\033[0m\n")
        user_name = input(f"\033[47m Write your name ✏︎ \033[0m  ")
        user.says(f"  //\n ('')      \033[45m {user_name} \033[0m\n / rr\n*\\ ))_")
        return self.game_logic(self.game_number, self.shift_number, user_score, cow_score, system_score, winner, user_name)

    def game_logic(self, game_number, shift_number, user_score, cow_score, system_score, winner, user_name):
        min = 1
        max = 100
        secret_number = random.randint(min,max)
        guesses = []
        i = 1
        while i !=11:
            #print("secret:", secret_number, "// min:", min, "max:", max)
            user_input = self.input(game_number, shift_number)
            user.says(f"  //\n ('')    {user_name}:  \033[45m {user_input} \033[0m\n / rr\n*\\ ))_")
            self.setting_guesses(i, user_input, guesses)
            # user shift ------------------
            if (int(user_input) == secret_number):
                # cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m You won!!!!!\033[0m\n ) (\n")
                winner = f"{user_name}"
                user_score += 1
                return self.end_game(secret_number, winner, user_score, cow_score, system_score, game_number, guesses, user_name)
            else:
                if(int(user_input) > secret_number):
                    print("\t\t\033[47m You went to far. \033[0m")
                    if (int(user_input) <= max):
                        max = int(user_input)-1
                    cow_guess =  random.randint(min,max)
                    cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m It's my turn!! My guess is: {cow_guess}\033[0m\n ) (\n")
                else:
                    print("\t\t\033[47m You fell short \033[0m")
                    if (int(user_input) >= min):
                        min = int(user_input)+1
                    cow_guess =  random.randint(min, max)
                    cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m Now me!! My guess is: {cow_guess}\033[0m\n ) (\n")
                # cow shift ------------------
                if(cow_guess == secret_number):
                    cow_score += 1
                    winner = "Cow"
                    return self.end_game(secret_number, winner, user_score, cow_score, system_score, game_number, guesses, user_name)
                elif (cow_guess > secret_number and cow_guess <= max):
                    max = cow_guess-1
                elif (cow_guess < secret_number and cow_guess >= min):
                    min = cow_guess+1

                shift_number += 1
                if(i == 10):
                    system_score += 1
                    winner = "System"
                    return self.end_game(secret_number, winner, user_score, cow_score, system_score, game_number, guesses, user_name)
            i += 1

    def end_game(self, secret_number, winner, user_score, cow_score, system_score, game_number, guesses, user_name):
        game.says(f"\033[36m\n-------------------------\033[0m\n\n\033[47m End of the game. The secret number is {secret_number} \033[0m")
        print(f"\nThe winner is: \033[46m {winner} \033[0m")
        if(winner == f"{user_name}"):
            cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m You won!!!!!\033[0m\n ) (\n")
        elif(winner == "Cow"):
            cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m I won!!!\033[0m\n ) (\n")
        else:
            cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m Oh no! We both lost against the system...\033[0m\n ) (\n")
        print(f"\033[35mYour guesses on game {game_number} \033[0m")
        for item in guesses:
            print(item)
        print(f"\n\033[36mGames played: {game_number} The score is:\033[0m \033[46m User {user_score} - Cow {cow_score} - System {system_score} \033[0m")
        print("\n\033[36m-------------------------\n\033[0m")
        return self.play_again(game_number, user_score, cow_score, system_score, winner, user_name)

    def play_again(self, game_number, user_score, cow_score, system_score, winner, user_name):
        user_input = input(f"\033[47m Write Y for yes and N for no ✏︎ \033[0m  ")
        if(user_input == "Y" or user_input == "y"):
            cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m Yay!! New game!!!!!!!!!!!!!\033[0m\n ) (\n")
            game.says(f" ___\n|[_]|\n|+ ;|  System: \033[47m New secret number: (??) \033[0m\n`---'\n")
            game_number +=1
            return self.game_logic(game_number, 1, user_score, cow_score, system_score, winner, user_name)
        elif(user_input != "Y" or user_input != "y"):
            if(user_score>cow_score and user_score>system_score):
                winner = f"{user_name}".upper()
            elif(cow_score>system_score and cow_score>user_score):
                winner = "COW"
            else:
                winner = "SYSTEM"
            print(f"\n\033[35m{game_number} games played: \n\n THE WINNER IS: \033[0m \033[45m {winner} \033[0m\n")
            game.says(f" ___\n|[_]|\n|+ ;|  System: Shutting down... \n`---'\n")
            return cow.says(f"\n_(~)_\n )\"(\n(@_@)\t  Cow:\t\033[33m See you later!!\033[0m\n ) (\n")

    def setting_guesses(self, i, user_input, guesses):
        guesses.append(f"Shift #{i}: \033[35m {user_input} \033[0m")
        return guesses
    
    def input(self, game_number, shift_number):
        return input(f"\nGame: {game_number}. Shift #{shift_number}. \033[47m Write your guess ✏︎ \033[0m  ")
    
    def says(self, template):
        return print(template)
    
    def __init__(self, game_number, shift_number, secret_number, game_score):
        self.game_number = game_number
        self.shift_number = shift_number
        self.secret_number = secret_number
        self.game_score = game_score

user = Player("name", 0, 0, 0)
cow = Player("Cow", 0, 0, 0)
game = Game(1, 1, "shift", "secret")

game.start_game()