# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:02:57 2020

@author: Aaditree Jaisswal
"""

name = input("Enter your name:")

print("Hello ",name)

print("-----------------------------")

print("Let's play Hangman!")

print("-----------------------------")

print("Guess the word. YOu have 10 attempts left")

word = random.choice(open(r"C:\Users\Aaditree Jaisswal\Desktop\Guided Projects\hangman.txt").read().split())

guess=""

attempts=0

length = len(word)

end = word


    print("The word is : ",end)      

while attempts <=10:
    
    g = input("Guess a letter")
    
    if length == 0:
        print("YOU WON")
        break
    
    if g in word:
        length=length-1
        print(g," is correct!")
       
    
    else:
        attempts=attempts+1
        print(g," is incorrect!")
    
 
if length !=0:
    print("YOU LOST")

print("The word is : ",end)      
        

            
            
            