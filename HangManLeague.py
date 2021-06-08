from random import randint
import json

def displayWelcome(data_list):
    print("\n--- Welcome to Hangman - League of Legends version!---")
    print(f"\nCurrently there are {len(data_list)} champions as of version 11.11")
    print("Try to guess a champion's name from an ability")
    print('You can type "/ff" to surrender and see the answer')
    
    
def get_data(file_object):
    try:
        with open(file_object, 'r') as file:
            content = json.load(file)
            return content
    except:
        print("File open error. Make sure you have 'league.json' located in the same folder")
    finally:
        file.close()
        
    
def game_loop(data_list, score):
    lives = 5
    random_champ = data_list[randint(0, len(data_list) - 1)]
    # random_champ = data_list[len(data_list) - 5] # zed only hehe xd
    champName = random_champ["name"]
    abilities_list = random_champ["abilities"]
    ability_index = randint(0, len(abilities_list) - 1)
    random_ability = abilities_list[ability_index]
    spells = ['Q', 'W', 'E', 'R']
    
    game_state = 'play'
    
    word_list = []
    guess_list = []
    trial_list = []
    for char in champName:
        word_list.append(char.lower())
        guess_list.append("")
    
    # Display player UI
    print(f'\nAbility: "{random_ability}"\n{len(champName)} characters')
    print('Lives:', '♥️ ' * lives)
    print("\n" + " _ " * len(guess_list) + "\n\n")
    
    guess = input("What's your guess: ")
    
    while True:
        
        if guess == '/ff':
            score -= 1
            game_state = 'end'
        
        # This /help feature is still bugged
        # if guess == '/help':
        #     lives -= 1
        #     rand_index = randint(0, len(word_list) - 1)
        #     guess_list[rand_index] = word_list[rand_index]
        
        if game_state == 'play':
            
            if guess == "":
                print("Please enter something")
                guess = input("Enter your guess again: ").lower()
            elif len(guess) > 1:
                print("Please enter only 1 character at a time")
                guess = input("Enter your guess again: ").lower()
            elif guess.isalpha() == False:
                print("Invalid character")
                guess = input("Enter your guess again: ").lower()
            elif guess in trial_list:
                print(f'You have already guessed {guess}')
                guess = input("Enter your guess again: ").lower()
                
            
            trial_list.append(guess)
            found = False
            foundCount = 0
            
            for i in range(len(champName)):
                if guess == word_list[i]:
                    guess_list[i] = guess
                    found = True
                    foundCount += 1
                    
            if found == True:
                print(f"Found {foundCount} {guess}!\n")
            elif found == False:
                lives -= 1
                print("Hmmm...you lost a life\n")
                
            # Update player UI
            print(f'Ability: "{random_ability}"\n{len(champName)} characters')
            print('Lives:', '♥️ ' * lives + '\n')
            for i in range(len(guess_list)):
                if guess_list[i] == "":
                    print(" _ ", end="")
                else:
                    print(" " + guess_list[i], end=" ")
            print("\n\n")
            
            if lives == 0:
                score -= 1
                print("Sorry, you lose :(")
                game_state = 'end'
            elif word_list == guess_list:
                score += 1
                print("Congratulations, you won!")
                game_state = 'end'
            else:
                guess = input("What's your guess: ").lower()
            
        elif game_state == 'end':
            print(f'"{random_ability}" is {champName}\'s {spells[ability_index]}.')
            print(f'You currently have {score} score')
            repeat = input("\nHit Enter to play again, gg to quit: ")
            if repeat.lower() == 'y' or repeat == '':
                random_champ = data_list[randint(0, len(data_list) - 1)]
                game_loop(data_list, score)
            elif repeat.lower() == 'gg':
                print("GGWP!")
                exit()
            else:
                print('Invalid input')
                repeat = input("\nHit Enter to play again, gg to quit: ")
    
    
def main():
    file_obj = 'league.json'
    data_list = get_data(file_obj)    
    score = 0
    displayWelcome(data_list)
    game_loop(data_list, score)


if __name__ == "__main__":
    main()