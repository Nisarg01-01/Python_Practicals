class Student:
    def __init__(self, name, num):
        self.rollno = num
        self.name = name
    
class Exam(Student):
    def __init__(self,name,num,marks):
        Student.__init__(self,name,num)
        self._marks = marks

class Result(Exam):
    def __init__(self,name,num,marks):
        Exam.__init__(self,name,num,marks)
        self.total_marks = 0
        for i in marks:
            self.total_marks += i   
    
    def display(self):
        print(str(self.name)+' has secured '+str(self.total_marks)+' marks out of 150')
    
       
if __name__ == '__main__':
    s1 = Result('Nisarg',131,[25,20,18,25,20])
    s2 = Result('Srushti',132,[30,25,20,30,29])
    s3 = Result('Krish',133,[25,30,25,25,25])
    s4 = Result('Raj',134,[25,25,25,24,15])
    s5 = Result('Kunal',135,[25,20,20,30,25])

    s1.display()
    s2.display()
    s3.display()
    s4.display()
    s5.display()