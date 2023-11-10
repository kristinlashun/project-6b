# #Author: Kristin Towns
# GitHub username: kristinlashun
# Date: November 9th, 2023
# Description: This program defines a function 'add_surname' that appends the surname 'Kardashian' 
# to first names in a given list that start with the letter 'K'.

def add_surname(names):
    
    return [name + " Kardashian" for name in names if name.startswith("K")]