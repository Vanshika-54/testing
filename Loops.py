#LOOPS


#FOR LOOPS
#RANGE
"""
x=range(0,10,1);
print (x);


x=range(0,10);
print (x);


x=range(10);
print (x);

"""



#FOR LOOP
'''
for i in range (10):
    print (i);
'''   


# end for horizontal
'''
for i in range (10):
    print (i,end="");
'''
#TABLE
'''
n=int(input("Enter your number = "));
for i in range(1,11,1):
    print (i*n);
'''
#TABLE WD FORMAT
'''
n=int(input("Enter your number = "));
for i in range(1,11,1):
    print (n,"*",i,"=",i*n);

'''    
#FOR ELSE BLOCK
'''
n=int(input("Enter your number = "));
if n==0:
    print("PLEASE ENTER GREATER THAN ZERO");
else:
    for i in range(1,11,1):
        print (n,"*",i,"=",i*n);
'''

#FACTORIAL

"""
#FACTORIAL IN LOOP 
n=int(input("Enter your number = "));
fact=1;
for i in range(1,n+1):
    fact=fact*i;
    print(fact);
"""
"""
#FACTORIAL OUTSIDE LOOP
n=int(input("Enter your number = "));
fact=1;
for i in range(1,n+1):
    fact=fact*i;
print(fact);
"""

#Reverse looping factorial
"""
n=int(input("Enter your number = "));
fact=1;
for i in range(n,1,-1):
    fact=fact*i;
print(fact);
"""

#ELSE BLOCK 

"""
n=int(input("Enter your number = "));
if n==0:
    print("FACTORIAL OF 0 IS 1");
elif n==1:
    print("FACTORIAL OF 1 IS 1");
else:
    fact=1;
    for i in range(1,n+1):
        fact=fact*i;
        print(fact);
"""


#  FACTORIAL OUTSIDE LOOP !!

"""
n=int(input("Enter your number = "));
if n==0:
    print("FACTORIAL OF 0 IS 1");
elif n==1:
    print("FACTORIAL OF 1 IS 1");
else:
    fact=1;
    for i in range(1,n+1):
        fact=fact*i;
print(fact);

"""




#For loop with continue , break and pass

"""
s="greeks"
for i in s:
    if i=='e':
        continue
    if i=='k':
        pass
    if i=='s':
        break
    print(i)
"""

"""
x=int(input("ENTER THE NUMBER = "));
if x==1:
    print("You selected one");
if x==2:
    print("You selected two");    
if x==3:
   pass
"""

#FOR LOOP WITH NUMBER PATTERN
"""
for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()
"""

#FOR LOOP WITH * PATTERN
"""
x=int(input("ENTER THE NUMBER of rows = "));
for i in range(1,x+1):
    for j in range(1,i+1):
        print('*',end="")
    print()

"""
#ALTERNATIVE
"""
x=int(input("ENTER THE NUMBER of rows = "));
for i in range(1,x+1):
        print('*'*i)
print()
"""
#TABLE USING THIS LOOP
"""
for i in range(2,3):
    for j in range (1,11):
        print(i,'*',j,"=",j*i)
print()
"""
#DIFFERENT PATTERN 
"""
a=['red','big','tasty']
fruits=["apple","banana","cherry"]
for x in a:
    for y in fruits:
        print(x,y);
"""




