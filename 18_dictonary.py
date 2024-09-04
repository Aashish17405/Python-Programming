# dictonary is a collection of key value pairs
"""
marks = {"english": 95, "chemistry": 98}

print(marks["chemistry"])  # displays chemistry marks
print(marks["english"])

marks["physics"] = 97  # physics marks will be displayed
print(marks)

marks["english"] = 94  # marks of english are changed
print(marks)

print(marks.values())  # prints the values of dictonary
print(marks.keys())  # prints the keys of dictonary

print(marks.items())  # prints the (key,value) of dictonary

# prints the value of dictonary (it returns none as it is not there in dictonary)
print(marks.get("maths"))
print(marks["maths"])  # throws an error as maths is not there in dictonary


# this is syntax for empty dictonary
x = {}
print(type(x))  # type helps us to find which type of argument

# this is syntax for empty set
x1 = set()
print(type(x1))  # type helps us to find which type of argument

# this is syntax for empty tupple
y = ()
print(type(y))  # type helps us to find which type of argument

# this is syntax for empty list
y1 = []
print(type(y1))  # type helps us to find which type of argument
"""

"""dict1={1:"asw","name":"Asha","gender":"f","age":36,"hobbies":["Shopping","eating"]}
dict1["name"]="Aashish"
dict2=dict(name="aashish",age=10)
dict2.pop("name")
dict2["gender"]="female"
print(dict2)

a={1:{"name":"pearly","age":40,"gender":"female"},3:{"name":"aashish","gender":"male","hobbies":["eating","playing"]}}
a[3]["hobbies"]="afhas"
print(a)
"""

a=list(map(str,input("Enter list of student names :").split()))
b=list(map(int,input("Enter student marks :").split()))
d={}
for i in range(len(a)):
    d[a[i]]=b[i]
print("Dictionary :",d)
print("Maximum Marks:",max(b))
print("Minimum Marks:",min(b))
print("student names with first class and less than 75:")
for i in b:
    if i>=60 and i<75:
        z=b.index(i)
        print(a[z])