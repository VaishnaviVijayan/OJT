class Jasmine(): 
    def color(self): 
        print("Jasmine flower comes in white, pink, blue, orange, yellow, purple, and red color") 
        def scientific_name(self): 
            print("Jasminum sambac is scientific name of Jasmine") 
            def family(self): 
                print("Jasmine is from Oleaceae family") 
                class Lily(): 
                    def color(self): 
                        print("Lilies commonly grow in white, yellow, pink, red, and orange color.") 
                        def scientific_name(self): 
                            print("Lilium is scientific name of Lily") 
                            def family(self): 
                                print("Lily is from Liliaceae family") 
                                obj_jasmine = Jasmine() 
                                obj_lily = Lily() 
                                for flower in (obj_jasmine, obj_lily): 
                                    flower.color() 
                                    flower.scientific_name() 
                                    flower.family()