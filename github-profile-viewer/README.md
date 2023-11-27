# GitHub Profile Viewer

## Description

The GitHub Profile Viewer is a Python command-line program that allows users to fetch and display GitHub profiles along with their top repositories. The program utilizes the GitHub API to retrieve user information and repository data.

## How it Works

- The program consists of three main functions:
  - `main()`: The main function to execute the GitHub Profile Viewer. It prompts the user to enter a GitHub username, fetches and displays the user's information and top repositories.
  - `get_user(username)`: Fetches user information and repositories from the GitHub API.
  - `display_user(user_data)`: Displays user information, including name, bio, followers, following, public repositories, and top repositories.

- The user is prompted to input a GitHub username, and the program fetches the corresponding user data and repository data using the GitHub API.

- If the entered GitHub username is not found (404 error), the program displays a "User not found".

## Program Input & Output

When you run the program `github_profile_viewer.py`, the output will look like this:

```

Welcome to GitHub Profile Viewer

Enter a GitHub username: joj-macho

User Information:
Name: Joj Macho
Bio: I do stuff
Followers: 8
Following: 23

Top Repositories:
Computational-Programming-Playground: https://github.com/joj-macho/Computational-Programming-Playground
Cryptography-Playground: https://github.com/joj-macho/Cryptography-Playground
Data-Science-Playground: https://github.com/joj-macho/Data-Science-Playground
GUI-Applications-Playground: https://github.com/joj-macho/GUI-Applications-Playground
joj-macho: https://github.com/joj-macho/joj-macho
joj-macho.github.io: https://github.com/joj-macho/joj-macho.github.io
Math-Science-Playground: https://github.com/joj-macho/Math-Science-Playground
Pygame-Playground: https://github.com/joj-macho/Pygame-Playground
Pythological-Playground: https://github.com/joj-macho/Pythological-Playground
Web-Development-Playground: https://github.com/joj-macho/Web-Development-Playground
```