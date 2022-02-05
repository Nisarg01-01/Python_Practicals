# 20CE132
# Nisarg Shah
# Repository Link :: https://github.com/Nisarg01-01/Python_Practicals.git
# visit Practical5.py 

# TAKING INPUT FROM USER

st = input('Enter the String:')

# SWAPING STRING CASE USING SWAPCASE()

print('SWAPPED CASE STRING (USING SWAPCASE())::'+ st.swapcase())

# SWAPING STRING CASE WITHOUT SWAPCASE()


new_str=""
for i in range (len(st)):                 # parseing through the string
    if st[i].isupper():                   # checking if the character is upper case 
        new_str=new_str+st[i].lower()     # if upper case then covert it to lower case
    elif st[i].islower():                 # checking if character is lower case
        new_str=new_str+st[i].upper()     # if lower case then covert it to upper case
    else:                                 # if its a special character
        new_str=new_str+st[i]             # then adding it as it is
        
print('SWAPPED CASE STRING (NOT USING SWAPCASE())::'+ new_str)
