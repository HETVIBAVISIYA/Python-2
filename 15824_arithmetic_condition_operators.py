# arithmetic operators 
# addition 
Add1=int(input('insert any number='))
Add2=int(input('insert any number='))
sum= Add1+Add2
print(sum)

# aiofowifoiewjfoiwjiofjiowjioa

# subtraction 
sub1=int(input('insert a number='))
sub2=int(input('insert a number='))
sub= sub1-sub2
print(sub)

# division 
d1=int(input('insert a number='))
d2=int(input('insert a number='))
div= d1 / d2
print (div)

# multiplication 
m1=int(input('insert a number='))
m2=int(input('insert a number='))
mul= m1*m2
print(mul)

# modulus 
mod1=int(input('insert a number='))
mod2=int(input('insert a number='))
mod = mod1 % mod2
print(mod)

# Exponentiation--- raises the value to the power of the second  value  

e1=int(input('insert a number='))
e2=int(input('insert a number='))
e = e1 ** e2
print (e)

# area of circle 
pi=3.15
r = int(input('enter redius mesturment: '))
A= pi*r*r
print (A)

a = int(input('enter a number: '))
b = int(input('enter a number: '))
c = int(input('enter a number: '))
d = int(input('enter a number: '))
e = int(input('enter a number: '))
final= print('the answer is:', e+a-d+c/b*e)

# celsius to Fahrenheit
c= int (input('enter celsius amount:'))
f= (c*1.8)+32
conv=print(f)



#conditional operator 
# there are three types of conditional operators : 1 is if, 2nd is else and third is if else 


a = int(input('enter a number: '))
b = int(input('enter a number: '))
c = int(input('enter a number: '))
d = int(input('enter a number: '))

if(a>b):
    if(a>c):
        if(a>d):
            print('a is big')
        else:
            print('d is big')
    else:
        if(c>d):
            print('c is big') 
        else:
            print('d is big')
else:
    if(b>c):
        if(b>d):
            print('b is big')
    else:
        if(c>d):
            print('c is big')  
        else:
            print('d is big')      


a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))
d = int(input('enter fourth number'))
e = int(input('enter fifth number'))

if(a>b):
        if(a>c):
                if(a>d):
                        if(a>e):
                                print('a')
                        else:
                             print('e is big')
                else:
                        if(d>e):
                                print('d is big')
                        else:
                              print('e is big')
        else:
                if(c>d):
                        if(c>e):
                              print('c is big')
                        else:
                              print('e is big')
                else:
                        if(d>e):
                            print('d is big')
                        else:
                              print('e is big')
else:
        if(b>c):
                if(b>d):
                        if(b>e):
                                print('b is big')
                        else:
                              print('e is big')
                else:
                        if(d>e):
                                print('d is big')
                        else:
                                print('e is big')
        else:
                if(c>d):
                        if(c>e):
                                print('c is big')
                        else:
                                print('e is big')
                else:
                        if(d>e):
                                print('d is big')
                        else:
                                print('e is big')

# this topic is called ledder if
marks= int(input('enter a number:'))
p = [33]

if(marks>90):
        print('You got grade A')
elif(marks>75):
        print('You got grade B')
elif(marks>60):
        print('You got grade C')
elif(marks>45):
        print('You got grade D')
elif(marks>33):
        print('You got grade E')
elif(marks<33):
        print('You got grade F, You are failed.')