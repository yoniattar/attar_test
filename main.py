import time
from virtual_pet import VirtualPet
from dog import Dog
from cat import Cat
from parrot import Parrot

def main():
    print("Welcome to Virtual Pet!")
    pet_type = input("Choose a pet (dog/cat/parrot): ").lower()
    pet_name = input("What is the pet's name? ").lower()
    if pet_type == 'dog':
        pet = Dog(pet_name)
    elif pet_type == 'cat':
        pet = Cat(pet_name)
    elif pet_type == 'parrot':
        pet = Parrot(pet_name)
    else:
        print("Invalid pet type. Exiting.")
        return

    while pet.is_alive:  # Keep looping as long as the pet is alive
        print("\n--- Pet Status ---")
        pet.display_status()

        action = input("Choose an action (feed/play/groom/sleep/talk/exit): ").lower()

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "groom":
            pet.groom()
        elif action == "sleep":
            pet.sleep()  # Call the sleep method
        elif action == "talk":
            if pet_type == "dog":
                pet.bark()
            elif pet_type == "cat":
                pet.meow()
            elif pet_type == "parrot":
                pet.repeat()
        elif action == "exit":
            print("Exiting the game.")
            break
        else:
            print("Invalid action. Try again.")

        # Update the happiness and hunger levels over time
        pet.happiness -= 2  # Decrease happiness over time
        pet.hunger -= 5  # Decrease hunger over time
        if pet.happiness < 0:
            pet.happiness = 0
        if pet.hunger < 0:
            pet.hunger = 0

        time.sleep(1)  # Optional: add a delay to simulate time passing


if __name__ == "__main__":
    main()
