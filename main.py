'''
userName = input("Enter your name: ")
# print("Hey " + userName)

userGrade=  input("What grade are you in? ")
print("Hey " + userName + ", " + userGrade + " is a lame grade")

userYear = input("What year were you born? ")
userAge = 2022 - int(userYear)
print(str(userAge) + " is so young!")
'''


#Create your own madlibda
#have at least 5 inputs
userName = input("Enter your name: ")
userAge = input("Enter your age: ")
userBrother = input("Enter another name: ")
userAction = input("Enter an action in past tense: ")
place = input("Enter your location: ")
print(userAge + " years old teenager, " + userName + ", has " + userAction + " his brother, " + userBrother + ", after he told him a joke" + ", in the " + place + ". His brother is now horrible condition.") 