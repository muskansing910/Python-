
balance = float(input("Enter account balance: "))

if balance>=1000:
    if balance>=1000 and balance<=5000:
        print("Maximum Withdrawal Limit: ₹1000")
    else:
        print("Maximum Withdrawal Limit: ₹5000")
else:
    print("Withdrawal Not Allowed!")