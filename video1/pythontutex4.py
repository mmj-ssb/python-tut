# Provide different output based on age
# 1-18 -> Important
# 21, 50 or > 65 -> Important
# Others -> Not important

# Ask the user to input age and output wether it is an important age or not
age = eval(input('Enter age: '))

if (age >= 1) and (age <= 18):
    print('That is an important age')
elif (age == 21) or (age == 50):
    print('That is an important age')
elif not(age < 65):
    print('That is an important age')
else:
    print('That is NOT an important age')
