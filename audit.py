"""
for i in range(10):
    for j in range(10):
            print("*",end=" ")
    print()"""

"""for i in range(10):
    for j in range(10):
        if(i%2==0):
            print(j+1,end=" ")
        else:
            print(10-j,end=" ")
    print()"""

"""n = 6
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    if i == 0 or i == n - 1:
        for j in range(2 * i + 1):
            print("*", end="")
    else:
        print("*", end="")
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*", end="")
    print()

for i in range(6):
    for j in range(6):
        if i==5 or j==0 or j==5:
           print("*",end=" ")
        else:
            print(" ",end=" ") 
    
    print()"""

"""q = 38
f = 11
for i in range(1,12):
    if i ==1:
        for u in range(1,11):
                print(u,end='  ')
        print()
    elif u and i<11:
        print(q," "*23,f)
        q-=1
        f+=1
    elif i ==11:
        for j in range(29,19,-1):
            print(j,end=' ')"""

"""n=int(input("Enter the len:"))
b=[]
for i in range(n):
    a=int(input())
    b.append(a)

#Arithmetic Mean
sum=0
for i in b:
    sum+=i
a=sum/len(b)
print("Average of numbers is",a)

#Geometric Mean
d=1
for i in b:
    d*=i
c=d**(1/len(b))
print("The geometric mean is",c)

#Harmonic Mean
z=[]
for i in b:
    k=1/i
    z.append(i)
co=0
for i in z:
    co+=i
r=co/len(z)
print("The harmonic mean is",r)"""

"""max=1
min=1
n=int(input("Enter the size:"))
for i in range(n):
    k=int(input())
    if(k>max):
        max=k
    if(k<min):
        min=k
print("Max is",max)
print("Min is",min)
"""
#Sum of digits
"""k=0
sum=0
n=int(input("Enter the number:"))
a=n
while(k<a):
    z=n%10
    sum+=z
    n=n//10
    k+=1
print(sum)"""

#Factorial
"""
n=int(input("Enter a number:"))
a=1
for i in range(1,n+1):
    a=a*i
print("Factorial of",n,"is",a)"""

#House
"""for i in range(10):
    for j in range(10-i):
        print(" ",end=" ")
    for j in range(1):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(20):
        print("*",end=" ")
    print()
for i in range(41):
    print("*",end=" ")
print()
for l in range(3):
    for m in range(41):
        if(m==0 or m==40 and l<2):
            print("*",end=" ")
        elif (l==2 and m == 7):
            print(" # # # # # # #", end="")
        elif (l==2 and (m==16 or m==34) ):
            print("*",end=" ")
        elif(l<2 and m==22):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
for k in range(13):
    for j in range(42):
        if(j==0 or j==40 or j==22):
            print("* ", end="")
        elif(k>3 and  (j==7 or j==15 or j==11) or k==4 and (j>6 and j<15)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
for b in range(41):
    print("*",end=" ")"""


#Currency denominations:
"""n=int(input("Enter the cost:"))
a=n//500
print(a,"*",500)
n=n%500
b=n//200
print(b,"*",200)
n=n%200
c=n//100
print(c,"*",100)
n=n%100
d=n//50
print(d,"*",50)
n=n%50
e=n//20
print(e,"*",20)
n=n%20
f=n//10
print(f,"*",10)
n=n%10
print("change:",n)"""


"""k=0
c=0
n=int(input("Enter the number:"))
a=n
while(k<a):
    z=n%10
    c+=z
    n=n//10
    k+=1
print(c)
i=0
d=c
sum=0
while(i<d):
    y=c%10
    sum+=y
    c=c//10
    i+=1
print(sum)"""

#Eprim
"""n=int(input("Enter a number:"))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
k=0
s=0
while(n>0):
    a=n%10
    n=n//10
    k+=1
    s=s*10+a
z=0
for i in range(1,s+1):
    if(s%i==0):
        z+=1
if(z==c):
    print("eprim")
else:
    print("Not eprim")"""

#Happy Number
"""n=int(input("Enter a number:"))
while(n>9):
    sum=0
    while(n>0):
        a=n%10
        sum=sum+(a*a)
        n=n//10
    n=sum
if(sum==1):
    print("HAPPY")
else:
    print("UNHAPPY")
"""

#strong number
"""n=int(input("Enter a number:"))
b=n
k=0
while(n>0):
    s=1
    i=1
    a=n%10
    while(i<=a):
        s=s*i
        i+=1
    k+=s
    n=n//10
print(k)
if(k==b):
    print("STRONG")
else:
    print("WEAK")"""

#Strings

"""c=[]
a=list(input("Enter the list of words:").split())
for i in range(len(a)):
    b=len(a[i])
    c.append(b)
d=max(c)
print(c[d-1])"""

"""a=input("Enter a string:")
if(len(a)<3):
    print(a)
else:
    if(a[-3:]=='ing'):
        print(a+'ly')
    else:
        print(a+'ing')"""

#Maximum frequency character in String
"""c=[]
a=input("Enter a string:")
for i in a:
    b=a.count(i)
    c.append(b)
d=max(c)
print(d)
e=c.index(d)
print(e)
print("The maximum of all characters in",a,"is",a[e])"""

#Replacing 1st 2 letters of strings
"""a=input("Enter the 1st string:")
b=input("Enter the 2nd string:")
c=a[0:2]
d=b[0:2]
z=a.replace(c,d)
y=b.replace(d,c)
print(z+" "+y)"""

"""s=input("Enter string:")
n=int(input("Enter number:"))
l=[]
for i in s:
    l.append(int(i))
l=list(sorted(set(l)))
if len(l)>=n:
    print(l[n-1])
else:
    print("-1")
"""

n=input("Enter a string:")
a={}
for i in n:
    a[i]=n.count(i)
b=list(a.keys())
c=list(a.values())
for i in range(len(b)):
    print(b[i],"",c[i])