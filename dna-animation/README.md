# DNA Animation

## Description

This program provides a fun and educational tool for visualizing the structure of DNA and how it is constructed from nucleotide pairs. The random selection of nucleotides adds an element of unpredictability to the animation, making it different every time the program is run.


## How it Works.

- The program starts by defining a variable `STRAND` which is a list of strings representing different rows of the DNA strand. Each row contains placeholders {},  except for index 0 and 9, which will be replaced by nucleotides in the animation.

```python
    STRAND = [

        '         ##', 
        '        #{}-{}#',
        '       #{}---{}#',
        '      #{}-----{}#',
        '     #{}------{}#',
        '    #{}------{}#',
        '    #{}-----{}#',
        '     #{}---{}#',
        '     #{}-{}#',
        '      ##',
        '     #{}-{}#',
        '     #{}---{}#',
        '    #{}-----{}#',
        '    #{}------{}#',
        '     #{}------{}#',
        '      #{}-----{}#',
        '       #{}---{}#',
        '        #{}-{}#']
```

- The `main()` function starts by printing a message indicating the start of the animation. It then prompts the user to press `Enter` to start the animation. Next, it enters a loop that displays the different rows of the DNA strand with random nucleotides. The loop keeps going until the user presses `Ctrl-C` to terminate the program.

- Within the loop, the program increments the `strand_i` variable to move to the next row of the strand. If `strand_i` is 0 or 9, the program simply prints the string without nucleotides. Otherwise, the program randomly selects a pair of nucleotides from the set of possible nucleotide pairs (AT, TA, GC, CG). It then formats the string at the current index in `STRAND` with the selected nucleotides and prints the resulting string.

- Finally, the program waits for 0.15 seconds before proceeding to the next iteration of the loop. When the user terminates the program by pressing `Ctrl-C`, the program prints a goodbye message and exits.


## Program Output

When you run `dna.py`, the output will look like this;

```
DNA Animation

Press Enter To Continue...
        #A-T#
       #G---C#
      #G-----C#
     #C------G#
    #G------C#
    #A-----T#
     #G---C#
     #A-T#
      ##
     #T-A#
     #A---T#
    #T-----A#
    #T------A#
     #A------T#
      #A-----T#
       #G---C#
        #C-G#
         ##
        #A-T#
       #A---T#
      #A-----T#
     #T------A#
    #C------G#
    #C-----G#
     #G---C#
     #G-C#
      ##
     #C-G#
     #T---A#
    #G-----C#
    #T------A#
     #C------G#
      #T-----A#
       #C---G#
        #C-G#
         ##
        #T-A#
       #T---A#
      #G-----C#
     #A------T#
^CGoodbye
```