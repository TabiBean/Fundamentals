#A normal string
my_string = "alpha"

#A multiline string
multiline_string = '''bravo
charlie'''
print(my_string)
print(multiline_string)

#How you print the index of a string
print(my_string[0])
print(my_string[3])

#Printing from 0 to 2 excluding 3
print(my_string[0:3])
#Printing from 0 to 1 excluding 2
print(my_string[ :2])
#Printing from 2 to the end of the string
print(my_string[2:])
#Strings are immutable so the string is unchanged after these slices
print(my_string)

#A for loop can be used to iterate through an entire string
for char in my_string:
    print(char)

#You can use in statements to test the boolean of if something is or is not in a string
print("pha" in my_string)
print("z" not in my_string)











