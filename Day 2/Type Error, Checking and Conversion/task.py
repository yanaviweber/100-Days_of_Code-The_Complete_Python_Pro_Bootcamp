congratulation = len("Hello")
print(congratulation) #Output 5

# print of the type of the variable
print(type("abc")) #Output 'str'
print(type(123)) #Output 'int'
print(type(3.14)) #Output 'float'
print(type(True)) #Output 'bool'

# transformation of the type of variable

print("123" + "456") #Output  as a text type 123456
print(int("123") + int("456")) #Output as a number type 579
# print(int("abc") + int("456"))
int("123") #Output as a number type 123
float()
str()
bool()

# print and output art of data of user
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))
print(type(length_of_name))

print("Number of letters in your name: " + str(length_of_name))