# ARITHMATIC OPERATORS

print("ARITHMATIC OPERATORS")

print(5+2)  # addition operator

print(5-2)  # subtraction operator

print(5*2)  # multiplication operator

print(5/2)  # division operator

print(5//2)  # to get result only in integers

print(5 % 2)  # modulo operator

print(5**2)  # power operator i.e. 5 power 2


# LOGICAL OPERATORS

print("LOGICAL OPERATORS")

print(3 > 2 or 2 > 3)  # prints true if any one of them is true

print(3 > 2 and 2 > 3)  # prints true if both of them are true

print(3 > 2 and 2 < 3)

print(not 3 > 2)  # prints false if output is true


# RELATIONAL OPERATORS

print("RELATIONAL OPERATORS")

print(5 > 2)   # greater than operator

print(5 >= 2)  # greater than or equal to operator

print(5 < 2)   # lesser than operator

print(5 <= 2)  # lesser than or equal to operator

print(5 == 2)  # equals to operator

print(5 != 2)  # not equal to operator


# ASSIGNMENT OPERATORS

print("ASSIGNMENT OPERATORS")

a = 1      # = is an assignment operator because it will assgin value
a += 1     # a=a+1 is equal to a+=a
print(a)

a = 1
a -= 1     # a=a-1 is equal to a-=a
print(a)

a = 1
a *= 1    # a=a*1 is equal to a*=a
print(a)

a = 1
a /= 1   # a=a/1 is equal to a/=a
print(a)


# BITWISE OPERATORS

print("BITWISE OPERATORS")

# complement operator i.e. if you give 1 then output will be 0 and vice versa
print(~12)

print(12 & 13)  # and operator the output will be sum of each bits of given number

print(12 | 13)  # or operator the output will be product of each bits of given number

print(12 ^ 13)  # xor operator

# left shift operation each bit of number will be shifted to left by 1 position
print(12 << 1)

# right shift operation each bit of number will be shifted to right by 1 position
print(12 >> 1)
