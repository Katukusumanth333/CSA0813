#Tax calculation
def calculate_tax(income):
    if income <= 150000:
        return 0
    elif income <= 300000:
        return (income - 150000) * 0.10
    elif income <= 500000:
        return (150000 * 0.10) + (income - 300000) * 0.20
    else:
        return (150000 * 0.10) + (200000 * 0.20) + (income - 500000) * 0.30
income = float(input("Enter the income: "))
tax = calculate_tax(income)
print("Tax= ", tax)
