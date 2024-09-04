# Sets: It is a datastructure which stores set of values of different datatypes.
#       Sets are immutable i.e. they can't be modified after initializing.
#       In Sets we use '{}'.

marks = {95, 98, 96, 98, 98}  # A Set of marks is created using {}

print(marks)  # they are unordered and unindexed

marks.add(100)  # it will add 100 into the set
print(marks)
# adding a value more than once will not change the set since all the elements in a set are unique

marks.remove(100)  # it will remove 100 into the set
print(marks)

print(len(marks))

# marks.clear()            # empties the set
# marks.union(a, b)         # gives all the elements in sets a and b
# marks.intersection(a, b)  # gives common elements in sets a and b
