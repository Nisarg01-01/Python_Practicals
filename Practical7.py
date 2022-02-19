n=int(input())
# taking input from user
for i in range(n):
   str =input()
   size = len(str)

# coverting to upper case to make it case insensitive    
   str=str.upper()
# if the string is has even length then consider mid character   
   if(size%2==0):
    left = str[:size//2]
    right = str[size//2:]

# if the string is has odd length then don't consider mid character
   else:
    left = str[:size//2]
    right = str[size//2+1:]
    
   leftpart = list(left)
   rightpart = list(right)
   leftpart.sort()
   rightpart.sort()

# left part and right part are equal then print yes else no
   if(leftpart==rightpart):
       print('Yes')
   else:
       print('No')
       
