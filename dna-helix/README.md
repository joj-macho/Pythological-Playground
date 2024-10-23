# DNA Animation

## Description

The DNA Animation program simulates an animated visualization of a DNA double-helix structure using ASCII art of a DNA stand.

## How it Works

- The program uses `STRAND` list that represents a template for the DNA structure using ASCII art.
- The `BASE_PAIRS` list contains tuples representing the complementary base pairs in DNA: Adenine (A) pairs with Thymine (T), and Cytosine (C) pairs with Guanine (G).
- The program runs in an infinite loop to continuously animate the DNA helix structure using the `STRAND` and randomly selected `BASE_PAIRS`.

## Running the Program

```bash
# Navigate to the project directory
cd dna-helix/

# Run the main script
python3 dna_animation.py
```

## Program Output

When you run `dna_animation.py`, the output will look like this;

![DNA Animation Result](output/dna-results.gif)