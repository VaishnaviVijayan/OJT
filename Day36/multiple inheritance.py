class father: # parent class
    def father_name(self):
        print("my father name is selvaraj")

class mother: # parent class
    def mother_name(self):
        print("my mother name is jayanthi")
    
class son(mother,father): # child class
    pass

obj_father= father() # object for father class.
obj_mother=mother() # object for mother class.
obj_son=son() # object for son class.
obj_son.father_name() # you access son class to father class.
obj_son.mother_name() # you access son class to mother class.
obj_mother.father_name() # This statement did not work because mother and father are parents.