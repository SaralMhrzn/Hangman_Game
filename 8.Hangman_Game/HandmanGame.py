import random
import hangman_stages
import fruit_list

# Define a list of fruits
# fruits = ["Apple", "Banana", "Cherry", "Grapes", "Kiwi", "Lemon", "Mango", 
#           "Orange", "Papaya", "Strawberry", "Watermelon"]a

def hangman():
    #importing list of fruits from fruit_list. 
    Fruits= fruit_list.fruits

    random_fruit= random.choice(Fruits).lower()
    print(f"You have to guess a word of letter {len(random_fruit)}.")

    blank_space= []
    for blank in range(len(random_fruit)):
        blank_space += '_'
    print(blank_space)

    a = len(hangman_stages.stages)
    # print(a)
    lives= a - 1  # Number of stages minus one for zero-based indexing
    print(f"you have {lives} lives")


    while True:
        Guessed_letter= input("Enter a letter: ").strip().lower()
        
        position= 0
        while position < len(random_fruit):

            if Guessed_letter in random_fruit[position]:
                blank_space[position] = Guessed_letter          
                print(f"You entered correct letter.")
            position+=1
                    
        if Guessed_letter not in random_fruit:
            lives -= 1
            print(f"You entered incorrect letter.")

            if lives == 0:           
                print(hangman_stages.stages[lives])
                print(f"You lose!! The word was: {random_fruit}")
                break
            
        
        if '_' not in blank_space:
            print(f"you won! The word is: {random_fruit}")
            exit()

        print(blank_space)
        print(hangman_stages.stages[lives])
        print(f"Remaining lives: {lives}")
        
hangman()

while True:
    asking= input("Do you want to play again?(Yes/No): ")
    if asking not in ["yes", "no"]:
        print("please Type valid input.")
    if asking== "yes":
        hangman()
    if asking== "no":
        print("Thanks for playing.")
        exit()


