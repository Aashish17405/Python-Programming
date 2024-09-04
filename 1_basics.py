'''
=>VARIABLES : Variables are the names you give to computer memory locations which are used to store values in a 
              computer program.
              Ex : a = 1 here we are storing 1 in a


=>DATATYPE : It tells us the kind of data stored in a variable.

             There are different types of datatypes :
             Numeric = 1)Integer : This value is represented by int class. It contains positive or negative whole 
                        numbers (without fraction or decimal). In Python there is no limit to how long an integer 
                        value can be.
                       2)Complex numbers : Complex number is represented by complex class. It is specified as 
                        (real part) + (imaginary part)j. For example - 2+3j
                       3)Float : This value is represented by float class. It is a real number with floating point 
                        representation. It is specified by a decimal point. Optionally, the character e or E followed
                        by a positive or negative integer may be appended to specify scientific notation.

             Dictonary = Dictionary in Python is an unordered collection of data values, used to store data values like
                         a map, which unlike other Data Types that hold only single value as an element, Dictionary holds
                         key:value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value
                         pair in a Dictionary is separated by a colon :, whereas each key is separated by a 'comma'.

             Boolean = Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false).

             Set = In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate 
                   elements. The order of elements in a set is undefined though it may consist of various elements.

             Sequence type = 1)String : A string is a collection of one or more characters put in a single quote, 
                              double-quote or triple quote. In python there is no character data type, a character is 
                              a string of length one. It is represented by str class.
                             2)List : Lists are just like the arrays, declared in other languages which is a ordered 
                              collection of data. It is very flexible as the items in a list do not need to be of the 
                              same type.
                             3)Tupple : Just like list, tuple is also an ordered collection of Python objects. The 
                              only difference between tuple and list is that tuples are immutable i.e. tuples cannot 
                              be modified after it is created. It is represented by tuple class.
'''

print("hello world")

print(''' 
Hi my name is abhiram
I am learning python''')      # triple quotations are used to write multi line statements
# single and double quotations are used to write single line statements
print('Hi my name is abhiram I am learning python')
print("Hi my name is abhiram I am learning python")

# printing variables

name = "abhiram"  # name variable is declared
age = 18          # age variable is declared
is_adult = True   # is_adult is a boolean variable which gives True or False
print("name")     # we get name being displayed
print(name)       # we get what is stored in name
print("age")
print(age)
print("is adult")
print(is_adult)
print(type(name))  # we get variable of datatype in output
print(type(age))
print(type(is_adult))
print(id(name))   # id will give us address of given variable
print(id(age))
print(id(is_adult))


