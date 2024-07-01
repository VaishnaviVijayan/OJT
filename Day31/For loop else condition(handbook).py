#program to check weather the given number is prime number or not 
num = int(input("Enter a Number : ")) 
for i in range(2,num): 
    if(num%i==0): 
        print("%d is not a prime number..."%num) 
        break 
    else: 
        print("%d is a prime number..."%num)