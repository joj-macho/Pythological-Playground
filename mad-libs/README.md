# Mad Libs Game

## Description

The Mad Libs Game is a Python program that allows users to create amusing and imaginative stories by filling in the blanks with various words such as nouns, adjectives, and locations.

## How it Works

- The program starts by importing the `random` to be used to select random stories and welcomes the user to the Mad Libs game.

- Inside the `main()` function, the program enters a loop that continues until the user decides to stop playing. Within this loop, the `mad_lib()` function is called to generate and display a Mad Libs story.

- The `mad_lib()` function guides the user through providing inputs for various parts of speech such as nouns, plural nouns, adjectives, and locations. It ensures that each input is non-empty and prompts the user to try again if any input is invalid.

- Once the user provides valid inputs, the function randomly selects a story template from a predefined list. It then substitutes the user-provided inputs into placeholders within the story template to create a unique Mad Libs story.

- After generating the story, the program displays it to the user.

- The user is prompted to decide whether they want to create another story. If they choose to continue, the loop repeats. If not, the program thanks the user for playing and exits.

- The program employs error handling to catch any `ValueError` exceptions raised during input validation, providing informative error messages to guide the user.

## Running the Program

```bash
# Navigate to the project directory
cd pico-fermi-bagels

# Run the main script
python3 pico_fermi_bagels.py
```

## Program Input & Output

When you run `mad_libs.py`, the output will look like this:

```

Welcome to Mad Libs!

Enter a noun (person, place, or thing): Dragon
Enter a plural noun: Heroes
Enter another noun: Treasure
Enter a location (e.g., city, forest, beach): Castle
Enter an adjective (describing word): Mighty 
Enter another noun related to the story: Knight

Once upon a time, in a mystical forest, there lived a brave Dragon who embarked on a quest to rescue a group of endangered Heroes. Along the journey, they encountered a wise Treasure who guided them through treacherous paths and enchanted Castle. With their Mighty courage, they vanquished the evil sorcerer and restored peace to the land.

Do you want to create another story? (yes/no): yes

Enter a noun (person, place, or thing): Wizard
Enter a plural noun: Spells
Enter another noun: Potion
Enter a location (e.g., city, forest, beach): Enchanted Forest
Enter an adjective (describing word): Mystical
Enter another noun related to the story: Wand

Deep beneath the ocean waves, there existed a hidden kingdom ruled by an ancient Wizard. The kingdom was populated by majestic Spells and colorful Potion. However, their peaceful existence was threatened by a powerful Mystical sea monster that terrorized the underwater realm. Determined to protect their home, a young Wand embarked on a daring adventure to confront the monster and restore harmony to the seas.

Do you want to create another story? (yes/no): yes

Enter a noun (person, place, or thing): Pirate
Enter a plural noun: Buccaneers
Enter another noun: Ship
Enter a location (e.g., city, forest, beach): Caribbean See
Enter an adjective (describing word): Swashbuckling
Enter another noun related to the story: Treasure Map

Once upon a time, in a mystical forest, there lived a brave Pirate who embarked on a quest to rescue a group of endangered Buccaneers. Along the journey, they encountered a wise Ship who guided them through treacherous paths and enchanted Caribbean See. With their Swashbuckling courage, they vanquished the evil sorcerer and restored peace to the land.

Do you want to create another story? (yes/no): yes

Enter a noun (person, place, or thing): Detective
Enter a plural noun: Clues
Enter another noun: Mystery
Enter a location (e.g., city, forest, beach): Crime Scene
Enter an adjective (describing word): Suspenseful
Enter another noun related to the story: Suspect

In the bustling city of Crime Scene, there was a renowned Detective known for their extraordinary talent. They were admired by many for their dedication to helping the community and their commitment to justice. One day, they received a mysterious message asking for their help to solve a puzzling mystery involving missing Clues. With their sharp wit and keen intellect, they unraveled the truth behind the disappearance and brought the culprit to justice.

Do you want to create another story? (yes/no): no

Thanks for playing!
```