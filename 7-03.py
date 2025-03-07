#oops:


class Human:
    def __init__(self):
        pass


    def speak(self):
        print("im Speaking")



class Student(Human):
      pass
std1=Student()
std1.speak()

#multilevel Inheritance:
#   inheritance from  parent class to child class and child class to sub child class (A---->B----->C)
# class User:
#      pass
# class Teacher(User):
#      pass
# class Admin(Teacher):     
#      pass








#multiple Inheritance:
   #  child inheritance from one and more Parent Classes At a time 

class Lion:
     def hunt(self):
          print("im lion Hunting")
     pass  
class Tiger:
     pass
class Liger(Tiger,Lion):
     pass

liger1=Liger()
liger1.hunt()