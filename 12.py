'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
'''

bill = float(input("Enter bill amount: "))

if bill <= 1000:
    gst = 0.05 * bill
    final_amount=bill+gst
    print("Final Bill Amount: ₹", int(final_amount))
elif bill <= 5000:
    gst = 0.12 * bill
    if bill>3000:
       service_charge=200
       final_amount=bill+service_charge+gst
       print("Final Bill Amount: ₹", int(final_amount))
    else:
        final_amount=bill+gst
        print("Final Bill Amount: ₹", int(final_amount))
 
else:
    gst = 0.18 * bill
    if bill>3000:
       service_charge=200
       final_amount=bill+service_charge+gst
       print("Final Bill Amount: ₹", int(final_amount))
    else:
        final_amount=bill+gst
        print("Final Bill Amount: ₹", int(final_amount))
 
