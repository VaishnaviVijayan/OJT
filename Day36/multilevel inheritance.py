class g_father:# parent class
    def g_father_name(self):
        print("my father name is ramasamy")
 
class father(g_father): # child class
    def father_name(self):
        print("my father name is selvaraj")

class son(father): # child class
    def son_name(self):
        print("my name is Anjali")


obj_g_father= father() # object for g_father class.
obj_father= father() # object for father class.
obj_son=son() # object for son class.

obj_son.g_father_name() # you access son class to g_father class.
obj_son.father_name() # you access son class to father class.
obj_son.son_name() # you access same class.