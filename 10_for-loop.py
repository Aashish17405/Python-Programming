#1:
"""number=int(input("Enter any integer:"))
count = 0
while number > 0:
    digit = number % 10
    if digit == 4:
        count += 1
    number = number // 10
print(count)"""

#2:
"""number=int(input("Enter any integer:"))
a=[]
while(number>0):
    digit=number%10
    a.append(digit)
    number=number//10
if(number>0):
    x=a[0]-a[-1]
    print(x)
else:
    print("Invalid Input")"""

#3:
"""A=int(input("Enter an integer A:"))
B=int(input("Enter an integer B:"))
N=int(input("Enter the number of turns:"))
i=1
while(i<=N):
    if(i%2==0):
        B=B*2
    else:
        A=A*2
    i=i+1
print(A+B)
"""
#5:
"""N=int(input("Enter the number of registration codes issued:"))
a=list(map(int,input().split()))
count,c=0,0
for i in a:
    if(i%2==0):
        count+=1
    else:
        c+=1
print(count,c)"""

#6:
"""
a=int(input())
b=int(input())
print("All positions change in year",a)
while(a<=b):
    if(a+60<=b):
        print("All positions change in year",a+60)
        a=a+60
        break"""

#7:
"""x=int(input("Enter lower limit:"))
y=int(input("Enter upper limit:"))
aes=0
for i in range(x,y+1):
    count=0
    for j in range(1,y+1):
        if(i%j==0):
            count+=1
    if(count==4):
        aes+=1
print(aes)
"""

#8:
"""a=int(input("Enter cost of PINK ticket:"))
b=int(input("Enter cost of GREEN ticket:"))
c=int(input("Enter cost of RED ticket:"))
d=int(input("Enter cost of ORANGE ticket:"))
e=int(input("Enter amount to be raised:"))
"""

#9:
"""a=int(input())
b=int(input())
c=int(input())
d=int(input())"""


"""for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()"""

"""for i in range(5):
    for j in range(i,5):
        print("*",end=" ")
    print()"""

"""for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
"""
"""for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,5):
        print("*",end="")
    print()"""

"""for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()"""

"""for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,5):
        print("*",end="")
    for j in range(i,4):
        print("*",end="")
    print()"""

"""for i in range(4):
    for j in range(i,5):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,5):
        print("*",end="")
    for j in range(i,4):
        print("*",end="")
    print()"""


#PATTERNS:

"""for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()"""

"""for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()"""

"""for i in range(3):
    for j in range(2*i +1):
        print("*",end="")
    print()"""

"""for i in range(5):
    for i in range(i,5):
        print("*",end="")
    print()"""

"""for i in range(5):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,4):
        print("b",end="")
    print()
"""

"""for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()"""

"""a=['abc', 'xyz', 'aba', '1221']
ctr=0
for i in range(len(a)):
    b=a[i]
    m=len(b)
    if(b[0]==b[-1]):
        ctr+=1
print(ctr)"""

"""a=input("Enter the number:")
b=0
c=""
for i in a:
    if(i.isdigit()):
        if(int(i)%2==1):
            b=int(i)**2
            c=c+str(b)
c=c[:4]
print(c)"""

"""print("Enter the numbers:")
a=list(map(int,input().split()))
b=max(a)
d=0
for i in a:
    c=0
    for j in range(1,b+1):
        if(i%j==0):
            c+=1
    if(c==2):
        d+=1
if(d==len(a)):
    print("True")
else:
    print("False")
    """

"""a=[1,3,5,7,9]
b=[1,2,4,6,7,8]
c=set(a)
d=set(b)
print((c-d).union(d-c))
"""

"""a=input("Enter a string:")
b=''
for i in a:
    if(len(a)>2):
        b=a[0:2]+a[-2]+a[-1]
    if(len(a)==2):
        b=a+a
    if(len(a)<2):
        b=''
print(b)"""

"""a=input("Enter a string:")
b=a[0]
c=a[1:]
d=c.replace(a[0],'$')
b=b+d
print(b)"""

"""a=input("Enter a string:")
b=input("Enter another string:")
c=a.replace(a[0],b[0])
d=c.replace(c[1],b[1])
e=' '
f=b.replace(b[0],a[0])
g=f.replace(f[1],a[1])
print(d+e+g)"""

