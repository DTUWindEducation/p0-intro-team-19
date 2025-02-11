# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:11:44 2025

@author: adru_
"""


#Exercise 1.

def greet(name):
    print("Hello,", name)

greet("world")  # Calling the function


#Exercise 2.

def Goldilocks(lenght):

    small_bed=140
    big_bed=150    

    if lenght < small_bed:
        print ("Too small")
    else:
        if lenght < big_bed:
            print ("just right")
        else:
            print ("too big")


Goldilocks (130)
Goldilocks (141)
Goldilocks (150)

#Exercise 3.

def square_list(numbers):  # Changed list to numbers
    length = len(numbers)
    list_squared = [0] * length
    
    for i in range(length):  # Loop correctly using range()
        list_squared[i] = numbers[i] ** 2  # Square each element
    
    print(list_squared)  # Print the squared list


square_list([1, 2, 3, 4])  
    
#Exercise 4.
 
def fibonacci(max_value):
    fibonacci_numbers = [0, 1]  # Start with the first two Fibonacci numbers
    
    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]  # Sum of last two numbers
        if next_fib > max_value:  # Stop if the next number exceeds max_value
            break
        fibonacci_numbers.append(next_fib)  # Append the next Fibonacci number

    print(fibonacci_numbers)  # Print the sequence
    
fibonacci(100)  # Generates Fibonacci numbers up to 100

#Exercise 5.

def clean_pitch(angles,status):
    
    cleaned_angles = [0]*len(angles)
    
    for i in range (len(angles)):
        if status [i]==1:
            cleaned_angles [i] = -999
        else:
            cleaned_angles [i] = angles [i]
    print (cleaned_angles)
    
x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
status = [1, 0, 0, 0]  # status signal
clean_pitch(x, status)




    
    