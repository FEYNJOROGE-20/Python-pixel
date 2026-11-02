def greet():
    print("Welcome to pixel class!")
greet()
#function with parameters
def student(name,age):
    print(f"My name is {name} and im {age} years old")
student("Mercy",28)

#function using inputoutput
def add_numbers(a,b):
    return a+b
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

result=add_numbers(num1,num2)
print(f"The sum is{result}")

def add(x,y):
    return x+y
result=add(6,23)
print(result)

#creat a program that gives a 10% discount
def calculate_discount(price):
    discount=price*0.10
    final_price=price-discount
    return final_price
price=int(input("Enter product price:"))
total=calculate_discount(price)
print(f"Price after discount :{total}")
