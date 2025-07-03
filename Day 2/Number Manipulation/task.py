bmi = 84 / 1.65 ** 2 # bmi index = weight / heigh squared
print(bmi) #Output 30.85399449035813

print(int(bmi)) #Output 30

print(round(bmi)) #Output 31
print(round(3.9)) #Output 4
print(round(3.3)) #Output 3

# round for 2 points of decimals
print(round(bmi, 2)) #Output 30.85

round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14


# User scores a point
# score += 1
# print(score)
#
# score -= 1
# print(score)
#
# score *= 1
# print(score)
#
# score /= 1
# print(score)

# print("Your score is " + str(score))


score = 0
height = 1.0
is_winning = True

# f-String
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.") # Output of values of 3 variables