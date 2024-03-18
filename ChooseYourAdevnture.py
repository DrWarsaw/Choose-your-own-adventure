import time
import random

def intro():
    print("Welcome to the Mysterious Forest!")
    print("You find yourself standing at the edge of a dense forest.")
    print("You have heard rumors about strange happenings in this forest, but you're determined to explore it.")
    print("You have three paths ahead of you: Left, Straight, and Right.")
    print("Which path will you choose?")

def left_path():
    print("\nYou chose the Left path.")
    print("As you venture deeper into the forest, you encounter a river blocking your way.")
    print("You can try to swim across (S), find another way around (A), or build a raft (R).")
    choice = input("What will you do? (S/A/R): ").lower()
    if choice == "s":
        if random.random() < 0.3:
            print("\nYou attempt to swim across the river.")
            time.sleep(2)
            print("But the current is too strong, and you're swept away.")
            print("Game Over.")
        else:
            print("\nYou successfully swim across the river and continue your journey.")
    elif choice == "a":
        print("\nYou decide to find another way around the river.")
        print("After a long walk, you find a bridge and cross it safely.")
        print("You continue your journey deeper into the forest.")
        time.sleep(2)
        print("\nYou've successfully crossed the river and continue your adventure.")
    elif choice == "r":
        print("\nYou decide to build a raft to cross the river.")
        if random.random() < 0.5:
            print("After gathering materials and constructing the raft, you successfully navigate across the river.")
            print("You continue your journey deeper into the forest.")
            time.sleep(2)
            print("\nYou've successfully crossed the river using a raft.")
        else:
            print("Your raft falls apart midstream, and you're swept away by the river.")
            print("Game Over.")

def straight_path():
    print("\nYou chose the Straight path.")
    print("You walk for a while until you stumble upon a hidden cave.")
    print("You can enter the cave (E), continue along the path (C), or climb the mountain nearby (M).")
    choice = input("What will you do? (E/C/M): ").lower()
    if choice == "e":
        print("\nYou enter the cave.")
        if random.random() < 0.2:
            print("Inside, you encounter a ferocious bear!")
            print("You barely escape with your life.")
            print("Game Over.")
        else:
            print("Inside, you find treasure and become rich!")
            print("Congratulations, you've won the game!")
    elif choice == "c":
        print("\nYou decide to continue along the path.")
        print("After some time, you encounter a friendly squirrel who guides you deeper into the forest.")
        print("You continue your journey with the squirrel by your side.")
        time.sleep(2)
        print("\nYou've made a new friend and continue your adventure.")
    elif choice == "m":
        print("\nYou choose to climb the mountain.")
        if random.random() < 0.3:
            print("As you climb higher, you slip and fall, injuring yourself.")
            print("You manage to crawl back down but must abandon your adventure.")
            print("Game Over.")
        else:
            print("As you climb higher, you encounter a breathtaking view of the entire forest.")
            print("You feel invigorated by the fresh air and stunning scenery.")
            time.sleep(2)
            print("\nYou've reached the summit of the mountain and enjoy the view.")

def right_path():
    print("\nYou chose the Right path.")
    print("You walk through dense foliage until you reach a fork in the road.")
    print("You can go left (L), right (R), or follow the path straight ahead (S).")
    choice = input("Which way will you go? (L/R/S): ").lower()
    if choice == "l":
        print("\nYou decide to go left.")
        print("As you walk, you come across a mysterious old tree.")
        print("You feel drawn to it and decide to investigate further.")
        time.sleep(2)
        print("\nYou've discovered the ancient tree and feel a strange energy emanating from it.")
    elif choice == "r":
        print("\nYou choose to go right.")
        print("You walk for what feels like hours until you find a hidden clearing.")
        print("In the clearing, you see a mystical fountain.")
        if random.random() < 0.4:
            print("You feel compelled to drink from it.")
            print("Drinking from the fountain curses you, and you're trapped in the forest forever.")
            print("Game Over.")
        else:
            print("You feel compelled to drink from it.")
            time.sleep(2)
            print("\nYou've drunk from the mystical fountain and feel rejuvenated.")
    elif choice == "s":
        print("\nYou decide to follow the path straight ahead.")
        print("The path leads you to a beautiful meadow filled with wildflowers.")
        time.sleep(2)
        print("\nYou've found a tranquil meadow and take a break.")

def main():
    intro()
    choice = input("Enter your choice (Left/L, Straight/S, Right/R): ").lower()
    if choice == "left" or choice == "l":
        left_path()
    elif choice == "straight" or choice == "s":
        straight_path()
    elif choice == "right" or choice == "r":
        right_path()
    else:
        print("Invalid choice. Please choose Left, Straight, or Right.")
        main()

if __name__ == "__main__":
    main()

