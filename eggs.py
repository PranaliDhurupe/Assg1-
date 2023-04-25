# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:38:41 2022

@author: Pranali
"""

def eggs(e):
    if e > 0 and e < 20:
        o = 1
        for i in range(1,e):
            o = o * 2
        print(o,"eggs hatched")
        
e = int(input()) 
eggs(e)
       