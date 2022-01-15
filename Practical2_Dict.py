# 20CE132
# Nisarg Shah
# Dictionary
# Repository Link ::

Dict1={1:10, 2:20}

Dict2={3:30, 4:40}

Dict3={5:50,6:60}

# Q.1 Write a Python script to check whether a given key already exists in a dictionary.

x=2
if x in Dict1:
    print( str(x) +" key is present")   # finding specific key in Dictionary
else:
    print("Does not exist")
    
# Q.2 Write a Python script to merge two Python dictionaries.

Dict1.update(Dict2)    #merging 2 dictionaries 
print(Dict1)

# Q.3 Write a Python program to sum all the items in a dictionary.

print(Dict1)
print(sum(Dict1.values()))

# Q.4 Write a Python script to add a key to a dictionary

Dict2['KeyAdded']='ValueAdded' #adding element to Dictionary
print(Dict2)

# Q.5 Write a Python script to concatenate following dictionaries to create a new one.

res = {**Dict1,**Dict2,**Dict3}    #concatenating 3 dictionaries together in new one
print(res)