class student :
    def __init__(self , name , age ):
        self.name = name
        self.age = age 

    def identif_student(self) :
        return f" student {id(student_1)} : \n name : {self.name} \n age : {self.age} "
        

class exillent(student) :
    def __init__(self, name, age, degre):
        super().__init__(name, age)
        self.degre = degre
    def Student_exillent(self) :
        if self.degre > 100 : 
            return super().identif_student() + "\n" + f" that student is exillent" 
        else :
            return super().identif_student() + "\n" + f" that student is faible "



student_1 = exillent("younes", 23 , 120)
student_2 = exillent("mohamed", 22 , 90)

print(student_1.Student_exillent())

    
        