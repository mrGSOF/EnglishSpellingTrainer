# English Spelling Trainer

### A fun game to help improve English spelling skills.

**By:** Guy Soffer (GSOF), 2019

- - -

## Overview

This project is a **terminal-based spelling exercise program** designed to help children practice English word spelling through an interactive and engaging interface.

Each word is pronounced through audio playback, and users must type the correct spelling. Immediate feedback is provided with sound effects, making the learning process both **educational and entertaining**.

- - -

## Features

*   Practice **English word spelling** with audio pronunciation
    
*   Three difficulty modes:
    
    *   🟢 **Easy** – Multiple choice format with 4 options
        
    *   🟡 **Medium** – Word list shown as reference, type full word
        
    *   🔴 **Hard** – No visual hints, spell purely from audio
        
*   Randomly selected words from the Words/ directory
    
*   Sound effects for correct ("Good.wav") and incorrect ("Error.wav") answers
    
*   Compatible with both Windows (`winsound`) and cross-platform (`playsound`) audio playback
    
*   Optional enhanced visuals using `liveconsole` (larger font, custom prompt)
    

- - -

## Installation

### 1. Clone or Download the Repository

```
git clone https://github.com/TzurSoffer/EnglishSpellingTrainer.git
cd EnglishSpellingTrainer
```

### 2. Install Dependencies

The script attempts to import `winsound` (Windows built-in) or fallback to `playsound`:

```
pip install playsound
```

(Optional) For enhanced visuals with larger font and custom prompt:

```
pip install liveconsole
```
- - -

## Running the Program

Simply run:

`python EnglishApp.py`

You'll be prompted to:

1.  Choose difficulty level (`A`, `B`, or `C`):
    - A: Multiple choice from 4 options
    - B: Type word with reference list visible
    - C: Type word with no visual hints
    
2.  Set how many words you want to practice
    
3.  Based on the chosen level:
    - Easy: Select the correct word from numbered options (1-4)
    - Medium/Hard: Type the complete word you hear
    

The program will then quiz you interactively!

- - -

## 💡 Example Interaction


```

Choose difficulty level (A,B,C): 
a
How many words? 
3
1. Book
2. Cat
3. Kitchen
4. Television
[Playing audio for Book]
Choose the word (1,2,3,4): 
1
Excellent!

1. Book
2. Computer
3. Dog
4. Kitchen
[Playing audio for Computer]
Choose the word (1,2,3,4): 
2
Excellent!

1. Door
2. House
3. Mouse
4. Table
[Playing audio for Table]
Choose the word (1,2,3,4): 
4
Excellent!
```
<img width="894" height="693" alt="image" src="https://github.com/user-attachments/assets/61d27aee-32a0-478c-85c9-b2271df8813d" />

- - -

## Author

**Guy Soffer (GSOF)**  
2019 — Educational freeware project.
- - -
