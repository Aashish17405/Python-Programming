# LIST : It is a datastructure which stores set of values of different datatypes.
#        Lists are mutable i.e. they can be modified.
#        In list we use '[]'.


marks = ["g", 95, 98, 96, "hi"]  # A List of marks is created using []

print(marks)    # All the elements in the list will be displayed

print(marks[0])  # It will display element present in 0th index
print(marks[1])
print(marks[2])
print(marks[3])

print(marks[-1])  # element present at index of first element from last
print(marks[-2])
print(marks[-3])
print(marks[-4])

# prints marks from 0th index to 2nd index but not including 2nd positon
print(marks[0:2])

marks.append(99)  # append will add the element at the last position of list
print(marks)

marks.extend([90, 80, 70, 60])  # extend will add multiple elements at a time
print(marks)

marks.insert(0, 99)  # insert will insert 99 in 0th index of list
print(marks)

print(98 in marks)  # checking whether 98 is present in given list
print(85 in marks)  # checking whether 85 is present in given list

marks.remove('hi')  # deletes 'hi' from the list
print(marks)

marks.pop(1)  # deletes element at 1st index
print(marks)

print(sum(marks))  # It will give sum of all the elements in a list

print(len(marks))  # gives length of the list

marks[1] = 0  # changing the element present at 1st index to 0
print(marks)

marks.sort  # will sort the elements given to the list
print(marks)

marks.reverse  # will sort the elements given to the list
print(marks)

marks.clear()  # it will clear the list
print(marks)
print("Helo")