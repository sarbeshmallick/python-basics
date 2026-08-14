
# 4th exercise, Mini calc 

# Build a calculator that can perform the following operations:

# a + b
# a - b
# a * b
# a % b
# a ** b



a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Enter operator (+, -, *, /, %, **): ")


if op == '+':
    print("Result:" , a+b)


elif op == '-':
    print("Result:" , a-b)


elif op == '*':
    print("Result:" , a*b)


elif op == '/':
    print("Result:" , a/b)


elif op == '%':
    print("Result:" , a%b)


elif op == '**':
    print("Result:" , a**b )


else:
    print("INVALID OPERATION")


