# Ask the user to input two values and store them in variables num1 and num2
num1, num2 = input('Enter two numbers: ').split()

# Convert the strings into regular numbers Integer
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Subtract the values and store in difference
difference = num1 - num2

# Multiply the value and store in product
product = num1 * num2

# Divide the values and store in quotient
quoutient = num1 / num2

# Use modulus on the values and store in remainder
remainder = num1 % num2

# Print the results
print('{} + {} = {}'.format(num1, num2, sum))
print('{} - {} = {}'.format(num1, num2, difference))
print('{} * {} = {}'.format(num1, num2, product))
print('{} / {} = {}'.format(num1, num2, quoutient))
print('{} % {} = {}'.format(num1, num2, remainder))
