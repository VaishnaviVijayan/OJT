def print_multiplication_table(number, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")


number = int(input("Enter a number: "))
print_multiplication_table(number)
