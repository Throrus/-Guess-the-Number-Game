import random

def main():

    diff = {'easy':10, 'medium':7, 'hard':5, 'insane':3}

    def choose_diff():
        difficulty_choice = input("\nChoose a difficulty: \n\nEasy \nMedium \nHard \nInsane \n\n")
        difficulty_choice = difficulty_choice.lower()
        diffs = ['easy', 'medium', 'hard', 'insane']
        if difficulty_choice in diffs:
            difficulty = diff[difficulty_choice]
        else:
            print("\nCheck your spelling and try again. ")
            choose_diff()

        def game(difficulty):
            guesses = difficulty
            hidden_number = random.randint(1,100)
            while True:
                guess = int(input("\nEnter a number between 1 & 100: "))
                guesses -= 1
                if guess == hidden_number:
                    if guesses == 1:
                        print("\nYou have won the game with 1 guess remaining! ")
                        again()
                        break
                    else:
                        print("\nYou won the game with {} guesses remaining! ".format(guesses))
                        again()
                        break
                elif guess < hidden_number:
                    print("The number is higher! \nGuesses = {} ".format(guesses))

                elif guess > hidden_number:
                    print("The number is lower! \nGuesses = {} ".format(guesses))
                    
                if guesses <= 0:
                    print("\nYou are out of guesses... \nThe number was {}.".format(hidden_number))
                    again()
                    break

                def again():
                    ag = input("\nDo you want to play again? y/n \n")
                    if ag == 'y':
                        change_difficulty = input("\nDo you want to change the difficulty? y/n \n")
                        if change_difficulty == 'y':
                            choose_diff()
                        else:
                            game(difficulty)
                    elif ag == 'n':
                        print("\n\nThanks for playing! ")
                    else:
                        print("\nUnknown Input!")
                        again()

        game(difficulty)

    print("\n\n\nWelcome to Guess The Number! \n\nThe object of the game is to guess a hidden number in as few guesses as possible. ")
    choose_diff()

if __name__ == '__main__':
    main()
