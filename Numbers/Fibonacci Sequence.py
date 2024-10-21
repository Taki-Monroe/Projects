import math

try:
 n = int(input("Enter the number of Fibonacci terms: "))

 fib1 = 0
 fib2 = 1

 x = range(2, n)

 print("Fibonacci Sequence: ")
 print(fib1, fib2, end=" ")

 for i in x:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    print(fib3, end=" ")
except:
 print("Something went wrong.")
