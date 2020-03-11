# Ideabank

## Story

You have a brilliant mind and you come up with better and better ideas every day.
The problem is, you would forget them quickly, so you decide to write an app that
helps you keep track of them.

## What are you going to learn?
You will learn and practice how to do the following things with Python:
- use loops,
- ask for user input,
- work with files,
- use command line arguments,
- handle errors.

## Tasks


1. Create a program in which you can add ideas and it lists them after addition.

    - The program asks for a new idea with printing out the phrase `What is your new idea?` until the user exit with `Ctrl+C`
    - After adding a new idea the list of the ideas is printed out with leading numbers (e.g. `1. first idea`)
    - If the user restarts the program, the ideas added earlier still remain

2. Add the option to list all the existing ideas without adding a new one with command line argument `--list`.

    - Calling the program with the command line argument `--list` prints out the list of the ideas with leading numbers (e.g. `1. first idea`)
    - Giving more command line arguments is ignored by the program.

3. Add an option to remove an idea by the leading number. Use console arguments like `--delete 2`.

    - Calling the program with the command line argument `--delete` and a number deletes the idea corresponding to the number and prints out the list of the ideas with leading numbers (e.g. `1. first idea`)
    - Not giving any arguments after the `--delete` argument prints out the error message `Specify a number after --delete`
    - Giving non-number arguments after the `--delete` argument prints out the error message `Specify a number after --delete`
    - Giving more command line arguments is ignored by the program.


## General requirements


None

## Hints

- Use a txt file to save data in order to have the ideas after restart as well.
- For deleting an idea you probably want to use some data structure in your program :)

## Starting repository

Click here to clone your own Git repository:
https://classroom.github.com/a/X1X2ZQMf

## Background materials

- :exclamation: [Strings](../pages/python/strings.md)
- :exclamation: [Control structures](../pages/python/control-structures.md)
- :exclamation: [Functions](../pages/python/functions.md)
- :exclamation: [Tutorial about command line arguments in Python](https://www.pythonforbeginners.com/system/python-sys-argv)
- :exclamation: [Error handling in Python](https://python-textbok.readthedocs.io/en/stable/Errors_and_Exceptions.html)

## Acceptance review

You will need this only at review time, **after** completing the project.
[Use this form](https://forms.gle/txDrU2D732PXmM7y7) to record the review you provide for your peer.