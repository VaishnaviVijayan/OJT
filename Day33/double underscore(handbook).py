class myClass(object): 
    def __init__(self): 
        self.a = 123  
        self._b = 123 
        self.__c = 123  
        obj = myClass() 
        print(obj.a) 
        print(obj._b) 
        print(obj.__c)