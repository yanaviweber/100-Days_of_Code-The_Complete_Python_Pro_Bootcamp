print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Program with if / else instruction
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# Program with if / elif / else instruction
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


# Program about measuring degrees score
maths_score = int(input("Which is your Math degrees in Semester?"))
english_score = int(input("Which is your English degrees in Semester?"))
if maths_score >= 90:
    if english_score >= 90:
         print("You are good at everything")
    else:
        print("You are good at maths")
if english_score >= 90:
    print("You are good at english")

# Program about BMI Index measuring
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("owerweight")