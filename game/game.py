import random

actions_done = 0

def game():
    global actions_done
    path = ""
    player_level = 1
    player_hp = 10

    while player_level < 100:
        print(f"You are on a dirt road, in the middle of a dark forest. You are currently level {player_level} with {player_hp} HP.")
        path = input("Which path will you choose? Safe, Adventurous, or Mysterious? ").lower()

        if path == "safe":
            actions_done += 1
            print("You took the safe path. It was a long journey, but you made it out of the forest safely.")
            print("You find yourself in a peaceful village. You can either rest or continue your journey.")
            path = input("What will you do? Rest or Continue? ").lower()
            if path == "rest":
                actions_done += 1
                print("You rest in the village and regain your strength.")
            elif path == "continue":
                print("You decided to continue your journey. You come across a beautiful lake.")
                actions_done += 1
                print("You decide to swim in the lake and find a hidden underwater cave.")
            else:
                print("Invalid choice. You can only choose 'Rest' or 'Continue'.")

        elif path == "adventurous":
            actions_done += 1
            print("You took the adventurous path. It was filled with challenges, but you enjoyed the adventure and made it out of the forest.")
            print("You find yourself in front of a mysterious cave. You can either enter the cave or continue your journey.")
            path = input("What will you do? Enter or Continue? ").lower()
            if path == "enter":
                print("You decided to enter the cave. Inside, you find a treasure chest!")
                print("You can either open the chest or leave it.")
                path = input("What will you do? Open or Leave? ").lower()
                if path == "open":
                    actions_done += 1
                    print("You open the chest and find a magical sword!")
                elif path == "leave":
                    print("You decide to leave the chest. As you exit the cave, you feel a sense of mystery.")
                    actions_done += 1
                else:
                    print("Invalid choice. You can only choose 'Open' or 'Leave'.")
            elif path == "continue":
                print("You decided to continue your journey. You come across a dangerous dragon!")
                actions_done += 1
                print("You use your magical sword to defeat the dragon and save the kingdom!")
            else:
                print("Invalid choice. You can only choose 'Enter' or 'Continue'.")
        else:
            print("Invalid choice. You can only choose 'Safe', 'Adventurous', or 'Mysterious'.")

        if actions_done >= 3:
            player_level += 1
            actions_done = 0
            print(f"You leveled up! You are now level {player_level}.")

if __name__ == "__main__":
    game()