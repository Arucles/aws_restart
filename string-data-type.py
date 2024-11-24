myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

##exercise 2: concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print("the concatenation is: " + thirdString)

##exercise 3: Working with inputs
name = input("What is your name? ")
print(name)

##exercise 4: usando format() para mostrar resultados
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))