# -*- coding: utf-8 -*-
"""Ex01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o7LMGceAHwAVSCSiMgqik4N8HuiA518E
"""

#Bahare_th#Ex01
#Calculator
import math

list = ['sin', 'log','fact','tan','cot','sqrt']

while True: 
  #calculator option
  print("welcome to my calculator")
  print("log") 
  print("sin") 
  print("+")  
  print("-")  
  print("/")  
  print("fact")
  print("tan") 
  print("cot")
  print("sqrt") 
  print("power") 
  print("exit") 

  #input options
  #input number
  operator = input("choose operator: ")
  if operator in list:
    a = float(input("Enter A: "))
  else:
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
 
#claculate plus
  if operator == "+":
    result = a + b

#claculate  minus  
  elif operator == "-":
    result = a - b

#claculate multiple
  elif operator =="*":
    result = a * b

#claculate divide
  elif operator == "/":
    if b == 0:
      result = "Cannot divide by zero"
    else:
      result = a / b

#calculate power
  elif operator == "**" or operator == "^":
    result = math.pow(a,b)

#calculate sin
  elif operator == "sin":
    result = math.sin(a)
  
#calculate log
  elif operator == "log":
    result = math.log2(a)

#calculate factorial
  elif operator == "fact":
    result = math.factorial(a)
  
#calculate tan
  elif operator == "tan":
    result = math.tan(a)

#calculate sqrt
  elif operator == "sqrt":
    result = math.sqrt(a)

#calculate cot
  elif operator == "cot":
    x = math.radians(a)
    result = math.cos(x)/ math.sin(x)


#print result
  print("result is :",result)
  print("-------------------")