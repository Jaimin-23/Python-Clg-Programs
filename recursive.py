#Recursive function- function that call itself
'''
#factorial
def fact(num):  #num=5 num=4 num=3 num=2 num=1 num=0= 5*4*3*2*1
    if(num<0):
        return "not possible"
    elif(num==0 or num==1):
        return 1
    else:
        return num*fact(num-1)
           
val=int(input("Enter no.:"))
result=fact(val)
print(f"Factorial of {val} is : {result}")
'''

#fibonnaci series
def fibo(num):
    if(num<0):
        return "not possible"
    elif(num==0 or num==1):
        return 1
