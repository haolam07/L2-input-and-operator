'''
userName = input("Enter your name: ")
# print("Hey " + userName)

userGrade=  input("What grade are you in? ")
print("Hey " + userName + ", " + userGrade + " is a lame grade")

userYear = input("What year were you born? ")
userAge = 2022 - int(userYear)
print(str(userAge) + " is so young!")
'''


#Create your own madlib
#have at least 5 inputs
userName = input("Enter your name: ")
userAge = input("Enter your age: ")
userBrother = input("Enter another name: ")
userObject = input("Enter an object: ")
location = input("enter a location: ")
month = input("Enter a month: ")
print("A " + userAge + " teenager called " + userName + " has been hitting "  + userBrother + " with a " + userObject + " since " + month + ". " + userBrother + " is now resting in a " + location) 