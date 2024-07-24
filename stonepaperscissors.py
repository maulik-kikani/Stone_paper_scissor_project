import random

rock = '''
    _______
___'   ____)
      (_____)
      (_____)
      (____)
---.__(___)    
'''

paper = '''
    _______
___'   ____)____
          ______)
          ________)
        _______)
---._________)
'''

scissors = '''
    _______
___'   ____)____
          ______)
        _________)
        (____)
---.__(___)
'''

while True:
    game_image = [rock,paper,scissors]
    user_choice = int(input("enter your choice: type 0 for rock, 1 for paper, 2 for scissors. "))

    if user_choice >= 3 or user_choice < 0:
        print("you enter invalid number and you lose.")
    else:
        print(game_image[user_choice])
        computer_choice = random.randint(0, 2)
        print("computer chose: ")
        print(game_image[computer_choice])
        if computer_choice == user_choice:
            print("it's a draw")
        elif computer_choice == 0 and user_choice == 2:
            print("you lose.")
        elif user_choice == 0 and computer_choice == 2:
            print("you win.")
        elif computer_choice > user_choice:
            print("you lose.")
        elif user_choice > computer_choice:
            print("you win.")

    while True:
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again == 'y' or play_again == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    if play_again != "y":
        break  # Exit the while loop if play_again is not 'y'

print("Thanks for playing!")
        


