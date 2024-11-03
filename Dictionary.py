
"""dict={"NAME":"VANSHIKA " ,"COURSE":"PYTHON","AGE":"SALARY"}
for d in dict:
    print(d)

    """
"""dict={"NAME":" VANSHIKA " ,"COURSE":" PYTHON ","AGE":" SALARY "}
for d,e in dict.items():
    print(d,e)"""
#d,e=iteraters
'''#Dictionary

#{}

#key :values

#how to declare a dictionary;

"""

d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

print(d);



val=d["Name"];

print(val);



#access using get();

d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

val=d.get("Phone");



print(val)



# access items of dictionary one by one

for i in d:

    print(i)#only key print







for i in d:

    val=d[i];

    print(val); # print value





#want both of them



#we use items()



for i, j in d.items():

    print(i,j);



#only print values we use values method also

for i in d.values():

    print(i)









# to cahnge the values/elements of the dictionary

d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

d["Roll"]=2;

print(d)





#Add some key and values in the existing dictionary;





d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

d["Gender"]="Male";

print(d)





#Dictionary methods



#1.len()



d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

d["Gender"]="Male";

l=len(d);

print(l)



#for removing an items/elements;



d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

print(d);

d.pop("Phone")

print(d);







#popitem()---- this method remove the last elements of the dictionay;

d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

print(d);

d.popitem();

print(d);

"""



#del -- this will remove the items with specific key name;

d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

print(d);

del d["Phone"];

print(d);





#Clear ---- delete all elemets;



d={"Roll":1,"Name":"Abhishek","Phone":85248,"Address":"Uttam nagar"};

print(d);

d.clear();

print(d)    '''

