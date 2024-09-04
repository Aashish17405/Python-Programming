# Tupple : It is a datastructure which stores set of values of different datatypes.
#          Lists are immutable i.e. they can't be modified after initializing.
#          In list we use '()'.


marks = (95, 98, 96, 98, 98)  # A Tupple of marks is created using ()
print(marks)

print(marks.count(98))  # gives the number of occurances of 98

print(marks.index(96))  # gives position of 96

# marks=(95)   #we get an error here, wrong way to declare a tuple with single element
# print(marks)

marks = (95,)  # tuple with single element
print(marks)

# marks[1] = 100  # This line of code will give us an error because we cannot modify data in tupple
# print(marks)
