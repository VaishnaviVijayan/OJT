def empinfo(name = "ABC", designation = "Dev"): 
    print ("Name : ", name) 
    print ("Designation : ", designation) 
    return; 
empinfo( designation = "Dev" )  


#Example

def empinfo(name = "XYZ", designation = 'Dev'): 
    print ("Name : ", name) 
    print ("Designation : ", designation) 
    return; 
empinfo( name = "ABC", designation = "Dev" ) 
empinfo( designation = "Dev" )