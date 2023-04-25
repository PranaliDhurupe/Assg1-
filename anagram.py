# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:14:08 2022

@author: Pranali
"""

def anagram(str1, str2):
    if (sorted(str1) == sorted(str2)):
        print("Anagram")
    else:
        print("Not an anagram")
        
str1 = input() 
str2 = input()
anagram(str1, str2)       