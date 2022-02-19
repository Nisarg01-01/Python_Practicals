# 20CE132
# Nisarg Shah
# Repository Link :: https://github.com/Nisarg01-01/Python_Practicals.git
# visit Practical6.py 

# Taking input from user
n=int(input())

# Taking string input from user
str=[input() for i in range(n)]
count=0
setstr = set(str)

# Printing output of total number unique 
print('Total unqiue strings:',len(setstr))
print('Count of string:')

# Printing output of occurence of each string
for i in setstr:
    print(str.count(i))