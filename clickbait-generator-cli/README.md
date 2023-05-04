# Click-bait Text Generator

## Description

This program, Clickbait Headline Generator, is a simple demonstration of how to generate clickbait headlines using Python. It uses random number generation and string manipulation to create headlines that are designed to pique the reader's curiosity and encourage them to click on a link.

## How it works

- The program starts by defining several lists of words and phrases, including personal pronouns, possessive pronouns, states, nouns, adjectives, verbs, places, and time phrases. It also defines a dictionary of clickbait types, each with a pre-defined headline format that includes one or more of the lists.

- The `main()` function starts by displaying an introductory message and prompts the user to enter a number of clickbait headlines to generate. If the user enters a valid integer, the program enters a loop that runs the specified number of times. Inside the loop, the program generates a random integer to select one of the pre-defined clickbait types. It then generates a number of random selections from the various lists, and uses string formatting to insert those selections into the selected clickbait type to create a complete headline.


## Program Input & Output

When you run the program `click_bait_generator.py`, the output will look like this;

```
Clickbait Headline Generator!

This program will trick people into looking at ads.
    
Enter a number of clickbaits headlines to generate:
> 10

You Won't Believe What This Texas Video Game Found in His Donut Shop

15 Gift Ideas to Give Your Avocado From New York

Big Companies Hate It! See How This Michigan Avocado Invented a Cheaper Serial Killer

9 Reasons Why Chickens Are More Interesting Than You Think (Number 5 Will Surprise You!)

9 Gift Ideas to Give Your Telephone Psychic From North Carolina

What Plastic Straws Don't Want You To Know About Athletes

You Won't Believe What This Illinois Parent Found in Her School

Big Companies Hate Them! See How This Pennsylvania Avocado Invented a Cheaper Clown

Without This Clown, Shovels Could Kill You Next Week

This North Carolina Doctor Didn't Think Robots Would Take His Job. I Was Wrong.
```