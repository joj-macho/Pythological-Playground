# DNA Animation

## Description

This program generates an animation for visualizing the structure of DNA and how it is constructed from nucleotide pairs. The random selection of nucleotides adds an element of unpredictability to the animation, making it different every time the program is run.

## How it Works

- The program starts by defining a variable `STRAND` which is a list of strings representing different rows of the DNA strand. Each row contains placeholders `{}`,  except for index 0 and 9, which will be replaced by nucleotides in the animation.

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

- The `main()` function runs the animation. It enters a loop that displays the different rows of the DNA strand with random nucleotides. The loop keeps going until the user presses `Ctrl-C` to terminate the program.

- Within the loop, the program increments the `strand_i` variable to move to the next row of the strand. If `strand_i` is 0 or 9, the program simply prints the string without nucleotides. Otherwise, the program randomly selects a pair of nucleotides from the set of possible nucleotide pairs (AT, TA, GC, CG). It then formats the string at the current index in `STRAND` with the selected nucleotides and prints the resulting string.

- Finally, the program waits for 0.15 seconds before proceeding to the next iteration of the loop. When the user terminates the program by pressing `Ctrl-C`, the program prints a goodbye message and exits.

## Running the Program

```bash
# Navigate to the project directory
cd pico-fermi-bagels

# Run the main script
python3 pico_fermi_bagels.py
```

## Program Output

When you run `dna_animation.py`, the output will look like this;

![DNA Animation Result](output/dna-animation-result.gif)