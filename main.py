"""
Filename: recursive_menu_program.py
Author: Jordan Wang
Date: June 10, 2025
Description: This program demonstrates recursion with a menu-based interface
that allows users to calculate factorials, find Fibonacci numbers,
and (optionally) draw a recursive fractal using the turtle module.

Created as part of my Cognizant Externship.
"""

import turtle

# 1. this is the recursive factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 2. this is the recursive Fibonacci function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3. this is the recursive fractal drawing (bonus): fractal tree
def draw_fractal_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# making sure that the inputted number is valid
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# display the menu and main loop
def main():
    print("Welcome to the Recursive Artistry Program!")
    
    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        
        choice = input("> ")
        
        if choice == "1":
            num = get_positive_integer("Enter a number to find its factorial: ")
            result = factorial(num)
            print(f"The factorial of {num} is {result}.")
        
        elif choice == "2":
            num = get_positive_integer("Enter the position of the Fibonacci number: ")
            result = fibonacci(num)
            print(f"The {num}th Fibonacci number is {result}.")
        
        elif choice == "3":
            print("Drawing a fractal tree... close the window to return to menu.")
            screen = turtle.Screen()
            screen.bgcolor("white")
            t = turtle.Turtle()
            t.color("green")
            t.left(90)
            t.speed("fastest")
            draw_fractal_tree(100, t)
            screen.exitonclick()

        elif choice == "4":
            print("Thank you for using the Recursive Artistry Program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
