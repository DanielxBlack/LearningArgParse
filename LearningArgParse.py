# Learning Arg Parse

# Import required modules
import argparse
import os
import sys


print("We are going to learn argparse today.")


def someCaca():

    # W args will go here.
    if args.w == "tacos":
        print("This is a string called tacos.")

    if args.w == "nachos":
        print("This is a string called nachos.")

    if args.w == "fritos":
        print("You wanna frito pie?")
        meow = 2 + 2 + 5 + 20
        print("This is just something called meow, added for the sake testing. It should print a number:", meow)

    if args.d == "tacos":
        print("This is a different string also called tacos.")

    if args.d == "nachos":
        print("This is another string. It is also about nachos.")


parser = argparse.ArgumentParser(description="Print something based on argument provided.")
parser.add_argument("-w", help="Print a string.")

parser = argparse.ArgumentParser(description="Do something else with another argument.")
parser.add_argument("-d", help="Print this thing")


args = parser.parse_args()

someCaca()
