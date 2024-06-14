x = 10
learning_rate =0.1
num_iteration = 100

#loop for gardient

for i in range(num_iteration):
    #compute our gradienet
    gradient = 2 * x 
    
    #update the x with new parameter
    x = x- learning_rate * gradient


print(f"iteration {i+1}: x = {x}, f{x} = {x**2}")

print(f"minimum value of the x:{x}")