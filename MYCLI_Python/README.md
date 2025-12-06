# MyCLI (Command Line in Python)

A simple Python command-line tool to greet a user or say goodbye.

---

## Features

- Greet a user with a friendly message.
- Say goodbye to a user.
- Uses Python's `argparse` for handling command-line arguments.

---

## Requirements

- Python 3.x

---

## Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/MYCLI_Python.git
cd MYCLI_Python
```
---

## Run the script
### Using Python
```bash
python3 CLI.py -o greet Hasnah
```
```bash
python3 CLI.py -o bye Hasnah
```


### Or directly if executable
```bash
./CLI.py -o greet Hasnah
```
```bash
./CLI.py -o bye Hasnah
```

---
## Options 
* -o, --operation : Operation to perform. Must be either greet or bye. 
* name : The name of the person.

---
## Example Output
```bash
$ python3 CLI.py -o greet Hasnah
```
### Hello, Hasnah! Welcome to MyCLI.
```bash
$ python3 CLI.py -o bye Hasnah
```
### Goodbye, Hasnah! See you next time.
---
## Help
```bash
python3 CLI.py -h
```




