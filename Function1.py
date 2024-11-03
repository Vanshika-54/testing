#Home work

#1 with rt and with argument.
'''
def Adding(a, b):
    Sum = a + b
    return Sum

x=int(input("enter x = "))
y=int(input("enter y = "))
z=Adding(x,y)
print("Addition Function",z)
'''
#Hw
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n=int(input("Enter a number"))
m=factorial(n)
print("The factorial is = ",m)
'''


#W RT W/O ARG
#2 with rt and without argument.
'''
def Adding():
    x=int(input("enter x = "))
    y=int(input("enter y = "))
    sum = x + y
    return sum

z=Adding()
print("Addition Function",z)
'''
#Hw
'''
def factorial():
    n=int(input("Enter a number ="))
    fact=1;
    for i in range (1,n+1):
        fact=fact*i;
    return fact
fc=factorial()
print("The factorial is ",fc)
'''


#W/O W ARG
#3 without rt and wth argumnt.
'''
def Adding(a, b):
    sum = a + b
    print("Addition Function:", sum)

x=int(input("enter x ="))
y=int(input("enter y ="))
Adding(x,y)
'''
#Hw
'''
def factorial(n):
    fact=1;
    for i in range(1,n+1):
        fact=fact*i;
    print("The factorial is",fact)


m=int(input("Enter a number = "))
factorial(m)
'''

#W/O RT W/O ARG
#4 without rt and without argument
'''
def Adding():
    x=int(input("enter x = "))
    y=int(input("enter y = "))
    Sum = x + y
    print("Addition function :", Sum)

Adding()
'''
#Hw
'''
def factorial():
    n=int(input("Enter a number = "));
    fact=1;
    for i in range (1,n+1):
        fact=fact*i;
    print("The factorial is = ",fact)

factorial()
'''

#RECURSION-----Recursion is a common mathematical and programming concept. It means that a function calls itself.
#This has the benefit of meaning that you can loop through data to reach a result.
# A process in which a function calls itself is called recursion.
#This process helps ease the method of solving problems by replacing iterative(for loop)code with recursive statements.

'''
def sum(n):
    if n <= 1:   # base case
        return n
    else:        # general or recursive case
        ans = sum(n - 1)
    return n + ans
num=int(input("enter a last number you want to take sum"))
print(sum(num))

'''
'''
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

m = int(input("Enter a number = "))
print("The factorial of", m, "is", factorial(m))

'''

#Lambda ===== your_function_name = lambda inputs : output
#A Lambda Function in Python programming is an anonymous function or a function without having a name and definition keyword  .
#Just like a normal function, a Lambda function can have multiple arguments with one expression.
#It is a small and restricted function having no more than one line. 
'''
sqrt=lambda x : x * x
#sqrt=lambda x:x**2
num1=int(input("enter 1 no"))
print("lambda sqrt is = " ,sqrt(num1))
mysum = lambda x,y : x + y
'''

'''
num1=int(input("enter 1 no ="))
num2=int(input("enter 2 no ="))
print("The sum is",mysum(num1,num2))
#print (mysum(10, 20))
'''

#+,-,0
'''
chknum = lambda num:"Positive" if num>0 else "Negative" if num<0 else "zero"
num1=int(input("Enter a number = "))
print(chknum(num1))

'''

#EVEN ODD
'''
num=lambda s:'Even' if s%2==0 else"Odd"
num1=int(input("Enter a number = "))
print(num(num1))
'''















































    

