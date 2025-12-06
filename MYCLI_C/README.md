# MyCLI (Command Line in C)


A simple C command-line program to print the arguments entered by the user.

---

## Features

- Prints the total number of arguments entered (excluding the program name).  
- Iterates through each command-line argument and prints it.  
- Shows usage instructions if no arguments are provided.  

---

## Requirements

- GCC (or any C compiler)  
- Terminal / Command Prompt  

---

## Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/CLI_C.git
cd CLI_C
```
---
## Compile the program
```bash
gcc CLI.c -o CLI
```
---
## Options
- arguments: Any number of words or strings you want the program to print.
---

## Run the program
### With arguments
```bash
./CLI Hello World
```
Output:

You entered 2 arguments:

Argument 1: Hello

Argument 2: World

--- 
### Without arguments
```bash
./CLI
```

Output:

Usage: ./CLI <arguments>

---



