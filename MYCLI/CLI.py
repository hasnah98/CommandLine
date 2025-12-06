#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="MyCLI with options")
    parser.add_argument("-o", "--operation", choices=["greet","bye"], required=True, help="Operation to perform")
    parser.add_argument("name", help="Name of the person")
    args = parser.parse_args()

    if args.operation == "greet":
        print(f"Hello, {args.name}! Welcome to MyCLI.")
    elif args.operation == "bye":
        print(f"Goodbye, {args.name}! See you next time.")

if __name__ == "__main__":
    main()
