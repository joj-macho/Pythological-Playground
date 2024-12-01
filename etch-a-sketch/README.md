# Etch A Sketch Simulator

## Description

The Etch A Sketch Simulator replicates the classic drawing experience of an Etch A Sketch toy using keyboard inputs (`w`, `a`, `s`, `d`).

## How it Works

- Control movments the cursor using `w` (up), `a` (left), `s` (down), and `d` (right).
- As the cursor moves, it leaves a trail on the grid.
- Available commands include:
    - (h)elp screen: Displays instructions and usage information.
    - (c)lear canvas: Erases all drawings on the canvas.
    - (e)xport: Saves the canvas drawing to a text file.
    - (q)uit: Exits the program.

## Running the Program

```bash
# Navigate to the project directory
cd etch-a-sketch

# Run the main script
python3 etch_a_sketch.py
```

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
