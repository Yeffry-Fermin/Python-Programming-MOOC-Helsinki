# Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

# Write your solution here
name = input("What is your name?")
familyName = input("What is your family name?")
streetAddress = input("What is your street address")
cityAndPostal = input("What is your your city and postal code")

print(name + " " + familyName)
print(streetAddress)
print(cityAndPostal)