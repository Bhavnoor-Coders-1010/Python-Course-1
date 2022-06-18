#COMMENTS

# This is a single line comment!!

'''
This is the first line of a multi-line comment!!
this is the second line of the multi-line comment!!
'''


#PRINT STATEMENTS

print("12348", "Singh", sep="##**__", end = "|")


#VARIABLES

age = 16
print("My age is", age)

'''
1) Variable names cannot contain any sp. character except for and _
2) Variable names cannot begin with a number
3) Variable names cannot be reserved keywords
4) Variable names must be relevant to what value is being stored.
'''

#DATATYPES


# different datatypes are string, integer, float, boolean, complex

name = "Bhavnoor Singh"
print(type(name))

age = 16
print(type(age))

marks = 98.5
print(type(marks))

yes_or_no = True
print(type(yes_or_no))

complex_num = 2 + 3j
print(type(complex_num))

marks = "98.5a"
print(type(marks))


#TYPE CASTING

# total_marks = float(marks) + 50  #Erroneous line of code
# print(total_marks)


#VARIABLE SWAPPING
num_1 = 10
num_2 = 20
print(num_1, num_2)

num_1, num_2 = num_2, num_1 #swapping of vars

print(num_1, num_2)