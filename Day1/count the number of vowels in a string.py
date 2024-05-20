def count_vowels(string):
   
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    vowel_count = 0
    
    for char in string:
      
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

input_string = input("Enter a string: ")
print("Number of vowels:", count_vowels(input_string))
