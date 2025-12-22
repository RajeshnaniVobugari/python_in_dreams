def addition(a,b):
    return a+b 

def subtraction(a,b):
    return a - b


def multiplication(a,b):
    return a * b 


def division(a,b):
    if b==0:
        raise ValueError('cannot be zero because the result will be undefined')
    return a/b

def calculation(a,b,operator):
    operators = {
        '+' : addition,
        '-': subtraction,
        '*' : multiplication,
        '/' : division
    }

    if operator not in operators:
        raise ValueError['invalid operator']
    
    return operators[operator](a,b)

if __name__ == '__main__':
    try:
        num1 = float(input('Enter the first number : '))
        num2 = float(input('Enter the second number : '))
        op = input('Enter the operator to calculate : ')

        result = calculation(operator=op, a=num1,b=num2)

        print(f'Result for the given problem : {result}')

    except ValueError as e:
        print(f'Error {e}')


