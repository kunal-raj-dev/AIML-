    # Q8. Let's create a Simple Calculator that performs arithmetic operations. Create
# a function calculator(a, b, operation) that performs addition, subtraction,
# multiplication, or division based on the operation parameter.
# [ operation parameter can have values + - * /

def calculator(a, b, operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        return (a/b) if b!=0 else "Division by Zero NOT pssible"
        

def calculator_via_eval(a, b, operation):
    try :
        ans = eval(f"{a}{operation}{b}")
    except ZeroDivisionError:
        return "Division by Zero NOT pssible"
    return ans

print(calculator(10, 0, '/'))
print(calculator_via_eval(10, 0, '/'))