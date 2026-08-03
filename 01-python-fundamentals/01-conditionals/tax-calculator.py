# Q1
# salary
# . Write a program that takes  as input. Using conditional statements, 
# calculate the  
# final tax rate
# based on these rules:
# • 
# If salary < 30,000 → 5%
# • 
# If salary is 30,000–70,000 → 15%
# • 
# If salary > 70,000 → 25%
def calcTax(salary):
    if salary <30000:
        return 0.05*salary
    elif 30000 <= salary >= 70000:
        return 0.15*salary
    else:
        return 0.25*salary

salary = float(input("Enter salary (₹) : "))
finalTaxRate = calcTax(salary)

print(f"Salary       : {salary}")
print(f"Tax          : {finalTaxRate}")
print(f"Gross income : {salary - finalTaxRate}")