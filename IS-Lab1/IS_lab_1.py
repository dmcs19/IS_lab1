from random import random

data = [[0.21835,0.81884,1],
        [0.14115,0.83535,1],
        [0.37022,0.8111,1],
        [0.31565,0.83101,1],
        [0.36484,0.8518,1],
        [0.46111,0.82518,1],
        [0.55223,0.83449,1],
        [0.16975,0.84049,1],
        [0.49187,0.80889,1],
        [0.14913,0.77104,-1],
        [0.18474,0.6279,-1],
        [0.08838,0.62068,-1],
        [0.098166,0.79092,-1]]

x1 = [data[0][0], data[1][0], data[2][0], data[9][0], data[10][0]]
x2 = [data[0][1], data[1][1], data[2][1], data[9][1], data[10][1]]

test_x1 = [data[3][0], data[4][0], data[5][0], data[6][0], data[7][0], data[8][0], data[11][0], data[12][0]]
test_x2 = [data[3][1], data[4][1], data[5][1], data[6][1], data[7][1], data[8][1], data[11][1], data[12][1]]
test_T = [1,1,1,1,1,1,-1,-1]

P = [x1, x2]

T = [1,1,1,-1,-1]

w1 = random()
w2 = random()
b = random()

e_total = 0
# Calculate weighted sum with randomly generated parametrers
for i in range(5):
        v = x1[i] * w1 + x2[i] * w2 + b
        if v > 0:
            y = 1
        else:
            y = -1
        e = T[i] - y
        
        # Calculate the total error
        e_total += abs(e)

print("Task 1")
print(e_total)


print("Task 2")

eta = 0.15
counter = 0

while e_total != 0:
    counter += 1
    
    # Calculate output for current example
    # Calculate error for current example
    # Update parameters using current inputs and current error
    for i in range(5):
        v = x1[i] * w1 + x2[i] * w2 + b
        if v > 0:
            y = 1
        else:
            y = -1
        e = T[i] - y
        
        w1 = w1 + eta * e * x1[i]
        w2 = w2 + eta * e * x2[i]
        b = b + eta * e
    
    
    # Test how good are updated parameters (weights) on all examples used for training
    # calculate outputs and errors for all 5 examples using current values of the parameter set {w1, w2, b}
    # calculate 'v1', 'v2', 'v3',... 'v5'
    # calculate 'y1', ..., 'y5'
    # calculate 'e1', ... 'e5'
        
    e_total = 0
    
    for i in range(5):
        v = x1[i] * w1 + x2[i] * w2 + b
        if v > 0:
            y = 1
        else:
            y = -1
        e = T[i] - y
        
        e_total += abs(e) 
    
    print(e_total)
        
print('Training Counter: ' + str(counter))

print('Test results:')
for i in range(len(test_x1)):
    v = test_x1[i] * w1 + test_x2[i] * w2 + b
    if v > 0:
        y = 1
    else:
        y = -1
    e = test_T[i] - y
        
    e_total += abs(e) 
print('Total error = ' + str(e_total))