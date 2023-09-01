# Etch A Sketch Simulator

## Description

The Etch A Sketch Simulator is a Python program that replicates the classic drawing experience of an Etch A Sketch toy. With the use of keyboard controls, users can move a virtual cursor on a canvas, creating drawings by navigating in different directions. This interactive program provides users with a range of features, including clearing the canvas, saving their artwork to a text file, and accessing a help screen for instructions.

## How it Works

- The program itself has clear comments explaining the program logic. Explaining the program line by line as usual will be too tedious, so here is a summary of the program features:s

- <strong>Canvas and Cursor</strong>: The program initializes a virtual canvas represented as a dictionary. This canvas stores information about drawn lines. A cursor is placed on the canvas, consisting of an (x, y) coordinate pair that users can control.

- <strong>User Interaction</strong>: Users utilize the WASD keys for navigation and drawing. Each key corresponds to a movement direction: W (Up), A (Left), S (Down), and D (Right). As users move the cursor, lines are drawn behind it.

- <strong>Commands</strong>: Users can issue commands by typing them in uppercase. Available commands include:
    - (H)elp screen: Displays instructions and usage information.
    - (C)lear canvas: Erases all drawings on the canvas.
    - (E)xport: Saves the canvas artwork to a text file.
    - (Q)uit: Exits the program gracefully.

- <strong>Drawing</strong>: As users move the cursor, the program interprets their input and renders lines on the canvas. Moving right (D) results in a horizontal line, while moving down (S) creates a vertical line. Users can combine these movements to create intricate patterns and drawings.

- <strong>Recording Moves</strong>: The program keeps track of the user's moves (W, A, S, D) in a list. Each move is recorded as users navigate and draw.

- <strong>Recording Moves</strong>: The program keeps track of the user's moves (W, A, S, D) in a list. Each move is recorded as users navigate and draw.

- <strong>Cursor Control</strong>: The program updates the cursor's position based on the user's input, ensuring it stays within the canvas boundaries.

- <strong>Updating Canvas</strong>: After each move, the canvas is updated to reflect the lines drawn. The program records the directions of lines at each (x, y) coordinate point. This information is used to render the canvas.

- <strong>Clearing the Canvas</strong>: Users can clear the canvas entirely, removing all drawings and resetting it to a blank state.

- <strong>Saving Artwork</strong>: The program allows users to save their artwork to a text file. Users specify the filename, and the program records their moves and the canvas state in the file.

- <strong>Help Screen</strong>: Typing 'H' or 'HELP' displays a help screen with clear instructions on using the program, controlling the cursor, and creating drawings. It also provides an example of how to draw a Hilbert Curve fractal.

## Program Input & Output

When you run the program `etch_a_sketch.py`, the output will look like this;

```
X                                       


.
.
.                                      
   
[Blank Screen]
.
.
.


Use WASD keys to move, (H)elp screen, (C)lear canvas, (E)xport to save, or (Q)UIT to exit.
> h
Welcome to the Etch-A-Sketch Simulator!
Use the following commands to draw and interact with the canvas:
---------------------------------------------------------------
WASD - Move the cursor and draw lines:
  W - Move Up   (Draws a vertical line below the cursor)
  A - Move Left (Draws a horizontal line to the left of the cursor)
  S - Move Down (Draws a vertical line above the cursor)
  D - Move Right (Draws a horizontal line to the right of the cursor)
---------------------------------------------------------------
H - Help: Display these instructions
C - Clear the canvas: Erase all drawings
E - Export the canvas: Save your masterpiece to a text file
Q - Quit the program: Exit the Etch-A-Sketch Simulator
---------------------------------------------------------------
Example: Drawing a Hilbert Curve Fractal
  To draw a Hilbert Curve fractal, you can use the following keys:
  SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW
  This sequence will create a beautiful Hilbert Curve fractal!
Press Enter to return to the program...


Use WASD keys to move, (H)elp screen, (C)lear canvas, (E)xport to save, or (Q)UIT to exit.
> WWADSDSWWADSDSWWADSDSWWADSDS
├┬┬┬┐                                    
 └┼┼┼┐                                   
  │││X                                   
                                         

Use WASD keys to move, (H)elp screen, (C)lear canvas, (E)xport to save, or (Q)UIT to exit.
> SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW
                                         
                                         
     │┌─┐┌─┐X                            
     └┘┌┘└┐└┘                            
     ┌┐└┐┌┘┌┐                            
     │└─┘└─┘│                            
     └┐┌──┐┌┘                            
     ┌┘└┐┌┘└┐                            
     │┌┐││┌┐│                            
     └┘└┘└┘└┘                            
                                         

Use WASD keys to move, (H)elp screen, (C)lear canvas, (E)xport to save, or (Q)UIT to exit.
> e
Enter filename to save to:
> hilbert_fractal
Canvas saved successfully.
                                         
                                         
     │┌─┐┌─┐X                            
     └┘┌┘└┐└┘                            
     ┌┐└┐┌┘┌┐                            
     │└─┘└─┘│                            
     └┐┌──┐┌┘                            
     ┌┘└┐┌┘└┐                            
     │┌┐││┌┐│                            
     └┘└┘└┘└┘                            


Use WASD keys to move, (H)elp screen, (C)lear canvas, (E)xport to save, or (Q)UIT to exit.
> q
Thanks for playing!
```
