# Leetspeak Converter

## Description

The Leetspeak Converter program converts English text into "Leetspeak", a form of written internet slang where letters are replaced with similar-looking numbers or symbols.

## How it Works

- Enter the message to convert to leet.
- The progam iterates over each character in the message. Where for each character, it checks the corresponding Leetspeak replacement in the `CHAR_MAPPING` dictionary.
- A random chance (60%) is used to decide whether to replace the character with its Leetspeak equivalent.

## Running the Program

```bash
# Navigate to the project directory
cd leetspeak_converter/

# Run the main script
python3 leetspeak.py
```

## Program Input & Output

When you run the program `leetspeak.py`, the output will look like this;

```
Leetspeak Converter.

Enter your message or (q) to quit: The quick brown fox jumps over the lazy dog.
Leetspeak: The qu![|< brown f()x jumps o\/er 7he |_@zy d()9. 

Enter your message or (q) to quit: The quick brown fox jumps over the lazy dog.
Leetspeak: 7he qui[k 8rown fox jump$ 0\/er +he |_@zy d()g. 

Enter your message or (q) to quit: Hello World
Leetspeak: He||o Wor|_|) 

Enter your message or (q) to quit: q
Bye!
```
