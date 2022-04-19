class parent1():

    def disp1(self):
        print("Inside Parent1")

class parent2():

    def disp2(self):
        print("Inside Parent2")
 
    
class derived(parent1, parent2): 
    
    def disp1(self):
        print("Inside Child Class")

obj = derived()

obj.disp1() 
obj.disp2()
