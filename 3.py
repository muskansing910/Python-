'''3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000'''

income = float(input("Enter annual income: "))
if income<=250000:
    print("NO Tax Payable")
elif income<=500000 and income>250000:
    a=income-250000
    x=a*0.5
    print("Tax Payable: ₹",x)
elif income<=1000000:
    a=income-250000
    x=a*0.20
    print("Tax Payable: ₹",x)

else:
    a=income-250000
    income>1000000
    x=income*0.30
    print("Tax Payable: ₹",x)
