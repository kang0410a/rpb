# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:58:30 2026

@author: kang0
"""
def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    
    
def add(a, b):
    return a + b
    
    
# TODO: divide() 함수 정의
def divide(x, y):
    if y:
        return x/y
    else: print('Error: cannot divide by zero.')

if __name__ == "__main__":
    main()
