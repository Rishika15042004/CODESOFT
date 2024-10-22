def add(num1,num2):
    return(num1+num2)
def subtract(num1,num2):
    return(num1-num2)
def multiply(num1,num2):
    return(num1*num2)
def divide(num1,num2):
    return(num1/num2)
print("what operation do you want?\n1.add\n2.subtract\n3.multiply\n4.divide")
use=int(input("select from 1,2,3,4:"))
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if(use==1):
    print(num1,"+",num2,"=",add(num1,num2))
elif(use==2):
    print(num1,"-",num2,"=",subtract(num1,num2))
elif(use==3): 
    print(num1,"*",num2,"=",multiply(num1,num2))
elif(use==4):
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("wrong input")