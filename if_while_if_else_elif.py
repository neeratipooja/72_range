a,b=[int(x) for x in input().split()]# 3 7
if(a>b):print('a is greater than b')#output doesnot execute anythimg
a,b=[int(x) for x in input().split()]#5 2
if(a>b):print('a is greater than b')# a is greater than b
a,b=[int(x) for x in input().split()]# 2 3
if(a>b):
    print(f'{a}>{b} is {a>b}')
else:
    print({f'{a}={b} is {a==b}'})    #{2=3 is false}
a,b=[int(x) for x in input().split()]#5 3 
if(a>b):print('a is greater than b')#a is greater than b
if(a<b):print('a is less than b')
if(a>=b):print('a is greater than or equal to b')#a is greater than or equal to b
if(a<=b):print('a is less than or equal to b')
if(a!=b):print('a is not equal to b')#a is not equal to b
if(a==b):print('a is equal to b')
a,b=[int(x) for x in input().split()]#2 5
if(a==b):print('a is equal to b')
elif(a>b): print('a is greater than b')
elif(a!=b): print('a is not equal to b')# a is not equal to b
elif(a<b): print('a is less than b')
elif(a>=b): print('a is greater than or equal to b')
elif(a<=b): print('a is less than or equal to b') 
a,b=[int(x) for x in input().split()]  #3 9 
while(a<=b):
    print(a)
    a+=1 #3 4 5 6 7 8 9 (in vertically)
while(a!=b):# 10 0
    print(a)
    a-=1   #10 9 8 7 6 5 4 3 2 1 (in vertically) 