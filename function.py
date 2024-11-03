# function----creted by ourself or the part of the pragram ..
#type of function-
#1 Pre-defined func-----print,int ,or and,while,not
#2. user defined function; created by user;


#How to declare a function;
#1.Func Declaration;
#2.func Defination;
#3.Func Call;

"""
def msg():#declare
    print("Hello");# define

msg();#call


def add():
    a=int(input("Enter"));
    b=int(input("Enter"));
    c=a+b;
    print("Hello");
    print(c);

def sub():
    a=int(input("Enter"));
    b=int(input("Enter"));
    c=a-b;
    print(c);


#Argument/Parameter---the value which we pass to the function to operate on it
def add1(a,b):
    c=a+b;
    print(c);


x=int(input("Enter"));
y=int(input("Enter"));





def add2(a,b):
    c=a+b;
    print(c);


    x=int(input("Enter"));
    y=int(input("Enter"));

"""

'''

#return statement---which we take from function;
    
def add(a,b):
    c=a+b;
    return c;


x=int(input("Enter"));
y=int(input("Enter"));

z=add(x,y)
print(z);

print(z);



''''



#Ankit sir
"""
def myfunction(a,b):
    c=a+b;
    print(c)
#myfunction(10,12)
"""
"""
def myfunction1(a,b):
    c=a-b;
    print(c)
"""

#myfunction(n,v)
#myfunction1(n,v)
'''
def aor(a,b):
    d=a*b;
    print(d)
n=int(input("ENTERA A NO ="))
v=int(input("ENTER ANOTHER NO ="))
aor(n,v)
'''
#key word argument
'''
def myfunction2(name,msg):
    print("HELLO",name,msg)


#n=input("ENTERA A Name =")
#m=input("ENTER A msg =")
myfunction2(name="Vanshika",msg="gdsgcjksdcksj")
'''
'''
def myfunction3(a,b=0):
    c=a+b;
    return c 
print("sum is",myfunction3(3,7))   
'''
'''
#arbitrary

#variable length
#tuple * arg


def my_sum(*arg):
    result=0;
    for i in arg:
        result=result+i
    print(result)




my_sum(45,54,6,4,7,45,8,4,4,)

'''

#variable length

#dict=== **kwarg
'''
def my_sum(**kwarg):
    result=0;
    for i in kwarg:
        result=result+i
    print(result)

'''






















