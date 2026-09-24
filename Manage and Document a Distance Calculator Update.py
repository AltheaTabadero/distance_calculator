
# Define all values and add import math
import math

x1 = float(input("enter x1: "))
y1 = float(input("enter x1: "))
x2 = float(input("enter x2: "))
y2 = float(input("enter y2: "))

# processing stage
distance = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

# print the results
print("the distance is: ", round(distance, 2))

#reflection

#the math library helped simplify my program by giving us ready-made functions like sqrt and pow.
# And without sqrt or pow, we would have to manually write the formula, which would take a lot of time.

