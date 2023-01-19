'''printing 0 to 10'''
n=int(input('enter the value of n:'))#10
for i in range(0,n+1):
    print(i,end=' ')#0 1 2 3 4 5 6 7 8 9 10
    '''printing squares and cubes'''
for i in range(1,5):
    print(i*i,end=' ')#1 4 9 16
    print(i**i,end=' ')# 1 4 27 256
    print(i*i*i,end=' ')#1 8 27 64
    '''printing 10 to 0'''
for i in range(10,-1,-1):
    print(i,end=' ')  #10 9 8 7 6 5 4 3 2 1 0
    '''printing even and odd numbers'''
n=int(input('enter the value of n:'))#10
for i in range(2,n,2):
    print(i)#2 4 6 8
for i in range(1,n,2):
    print(i,end=" ") #1 3 5 7 9
    '''printing 10 to 1'''
for i in range(10,0,-1):
    print(i)#10 9 8 7 6 5 4 3 2 1
    '''reversing the given list'''
n=['p',1,5.4]
for i in n[::-1]:
    print(i)#5.4
            # 1
            # 'p'
print(n[::-1]) #[5.4.1.'p']
'''slicing in range'''
k='krishna pooja'
print(k[::2]) #kihapoa 
for i in k[::2]:
    print(i,end='')#kihapoa
    '''if else program'''
b=int(input('enter the value of b:'))#9
if(b%2==0):
    print(f'{b} is even number')
else:
    print(f'{b} is odd number')  #9 is odd number  
b=int(input('enter the value of b:'))#6
if(b%2==0):
    print(f'{b} is even number')# 8 is even number
else:
    print(f'{b} is odd number') 
n= int(input('enter the value of n:'))
'''while program'''
while(n<10):
    print('hi',str(n))
    n+=2# hi  5
        # hi 7
        #hi 9
i=int(input('enter the value of i:'))
while(i<10):
    print('hi',str(i),end=' ')
    i+=1#hi 5   hi 6   hi 7  hi 8  hi 9  
while(1<10):
    print('hi')#hi--------------------infinite times