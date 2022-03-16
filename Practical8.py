class Stack:  
    def __init__(self): 
        self.stck = [] 
    def push(self, data): 
        self.stck.append(data) 
    def pop(self): 
        self.stck.pop()
    def traverse(self): 
        for i in range(len(self.stck)-1, -1, -1): 
            print(str(self.stck[i])+' ')
        print('\n')

s1 = Stack()
print('Pushing elements into the stack')
for i in range(1,6):
    s1.push(i)

print('\nTraversing the stack')
s1.traverse()

print('Popping elements from the stack')
for i in range(1,3):
    s1.pop()

print('\nTraversing the stack')
s1.traverse()

        
