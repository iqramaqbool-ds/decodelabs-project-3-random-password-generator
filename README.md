# Enterprise Random Password Generator

A secure random password generator developed as part of my DecodeLabs Industrial Training Program - Project 3.

## Project Objective

The objective of this project is to generate strong random passwords using Python's secure `secrets` module and standard character collections from the `string` module.

## Features

- Accepts a user-defined password length
- Requires a minimum password length of 15 characters
- Generates lowercase letters
- Generates uppercase letters
- Generates numbers
- Generates special characters
- Uses `secrets.choice()` for secure random selection
- Uses `secrets.SystemRandom().shuffle()` for secure shuffling
- Uses `''.join()` for efficient string construction
- Handles invalid input
- Prevents passwords shorter than the required minimum

## Security Approach

The project uses Python's `secrets` module rather than the standard `random` module for password generation.

The generator guarantees at least:

- One lowercase letter
- One uppercase letter
- One number
- One special character

The remaining characters are selected from the complete character pool using secure random selection.

## Example

```text
================================
   Enterprise Password Generator
================================
Minimum password length: 15 characters
Enter the required password length.

Enter password length: 15

Generated Password:
[Randomly generated password]

Password Length: 15 characters