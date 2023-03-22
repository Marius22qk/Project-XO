# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:21:37 2022

@author: mariu
"""

def user_choice(): # validare user input
    
    choice = "Wrong"
    acceptable_range = range(0,10)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
        choice = input("Please enter a number (0-10): ")
        
        #Digit check
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
        # Range check
        
        if choice.isdigit() == True:
            
            if int(choice) in acceptable_range:
                within_range == True
                break
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range = False
                
    return int(choice)

print(user_choice())