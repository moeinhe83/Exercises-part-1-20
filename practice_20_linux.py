# Practice_20

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 20', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value 
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Convert List To Set
a = set(a)
b = set(b)

# Computing
print(f'a-b ===> {a-b}')
print('===============')
print(f'b-a ===> {b-a}')

# Finish
# Create By Moein Heshmati
