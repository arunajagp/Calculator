# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:34:41 2021

@author: ARUNAJA GEETHAPRASAD
"""

def my_operations(a,b):
        if x=="+":
          sum=a+b
          print("The sum is: "+ str(a) + " + " + str(b)+ " = " +str(sum))
        elif x=="-":
          diff = a-b
          print("The Difference is: "+ str(a) + " - " + str(b)+ " = " +str(diff))
        elif x=="*":
          multi = a*b
          print("The Product is: "+ str(a) + " * " + str(b)+ " = " +str(multi))
        elif x=="/":
          div = a/b
          print("The Quotient is: "+ str(a) + " / " + str(b)+ " = " +str(div))
        elif x=="**":
          power = a**b
          print("The Power is: "+ str(a) + " ** " + str(b)+ " = " +str(power))
        
x = input("+\n-\n*\n/\n**\n Enter your operation:")   
a = input("Enter the value of a:")
b = input("Enter the value of b:") 
a=float(a)
b=float(b)


my_operations(a,b)
