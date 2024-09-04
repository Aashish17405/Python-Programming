old_age=input("enter your old age : ")
#new_age = old_age + 2  #if we execute this line we get error since old_age here is taken as a string but we need to add it to int
new_age = int(old_age) + 2 #we converted old age here into integer
print("new age is : ")
print(new_age)