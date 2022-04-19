str = list(input('Enter a string: '))
d = {}
s = set(str)
for i in s:
    d[i]=str.count(i)
    
d = dict(sorted(d.items(), key=lambda item: item[1],reverse = True))

for k in d:
    print(k,' ',d[k])