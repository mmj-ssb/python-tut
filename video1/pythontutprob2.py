# Problem: Print different responses based on the users age
# Complete problem with 10 or less lines

# If age is 5, go to Kindergarten
# Ages 6 through 17 goes to grade 1-12
# If age is greater than 17, go to college

age = eval(input('Enter your age: '))

if age == 5:
    print('Go to kindergarten')
elif (age >= 6) and (age <= 17):
    print('Go to grade {}'.format(age - 5))
elif (age >= 18):
    print('Go to college')
else:
    print('You are too young for school')
