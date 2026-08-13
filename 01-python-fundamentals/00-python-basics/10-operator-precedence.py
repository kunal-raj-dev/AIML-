# 10. Operator Precedence in Python
# Order of execution (PEMDAS / Operator Priority):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor Div //, Modulo % (left to right)
# 4. Addition +, Subtraction - (left to right)
# 5. Relational operators (==, !=, <, >, <=, >=)
# 6. Logical operators (not -> and -> or)

result1 = 5 + 3 * 2 ** 2
# Step 1: 2 ** 2 = 4
# Step 2: 3 * 4 = 12
# Step 3: 5 + 12 = 17
print(f"5 + 3 * 2 ** 2 = {result1}")

result2 = (5 + 3) * (2 ** 2)
# Step 1: (5 + 3) = 8, (2 ** 2) = 4
# Step 2: 8 * 4 = 32
print(f"(5 + 3) * (2 ** 2) = {result2}")

# Logical precedence: 'not' before 'and', 'and' before 'or'
cond = True or False and not True
# not True -> False; False and False -> False; True or False -> True
print(f"True or False and not True = {cond}")
