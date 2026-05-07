'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''

vehicle = input("Enter vehicle type: ").lower()
hours = int(input("Enter hours parked: "))

if vehicle == "bike":
    x = 10 * hours
    if hours > 5:
        x += 100
    print("Total Parking Fee: ₹", x)

elif vehicle == "car":
    x = 20 * hours
    if hours > 5:
        x += 100
    print("Total Parking Fee: ₹", x)

elif vehicle == "bus":
    x = 50 * hours
    if hours > 5:
        x += 100
    print("Total Parking Fee: ₹", x)

else:
    print("Invalid vehicle type")