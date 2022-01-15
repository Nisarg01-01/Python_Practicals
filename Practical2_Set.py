# 20CE132
# Nisarg Shah
# Set
# Repository Link :: 

# Q.1 Write a Python program to add member(s) in a set and clear a set

set1 = {'one','two','three'}
set1.add('four')   #adding element to set
print(set1)
set1.clear()   #clearing whole set
print(set1)

# Q.2 Write a Python program to remove an item from a set if it is present in the set.

set2 = {'hello','how','are','you','Go'}
set2.remove('are')   #Remove function
print(set2)

# Q.3 Write a Python program to create an intersection, Union, difference of sets.

set3 = {1,2,3,4}
set4 = {5,6,1}
inte = set3.intersection(set4)  #intersection
uni = set3.union(set4)          #Union
diff = set3.difference(set4)    #Difference
print('Interaction::')
print(inte)
print('union:')
print(uni)
print('Diff:')
print(diff)

# Q.4 Write a Python program to find maximum and the minimum value in a set.

# consider set Union to find max and min values
print('MAX::'+str(max(uni)))  #Maximum in Union set
print('MIN::'+str(min(uni)))  #Minimum in Union set

# Q.5 Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# for dictionary and tuple convert both into list first then apply same function on them
# element in a list

from itertools import count

def most_frequent(List):
	counter = 0
	num = List[0]
	
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i

	print("frequant element is %d and counter for element is %d"%(num,counter))
     

List = [45, 45, 22, 21, 45, 31]
(most_frequent(List)) #this function will print most frequant element in list with their count.