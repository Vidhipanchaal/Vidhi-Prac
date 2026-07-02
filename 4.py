# Electricity Bill Calculator

previous = int(input("Enter previous meter reading: "))
present = int(input("Enter present meter reading: "))

energy = float(input("Enter energy charges: "))
fppas = float(input("Enter FPPAS charges: "))
govt = float(input("Enter government duty: "))
fixed = float(input("Enter fixed charges: "))
adjustment = float(input("Enter adjustment (+/-): "))

units = present - previous

bill = energy + fppas + govt + fixed + adjustment

print("\n------ BILL SUMMARY ------")
print("Units Consumed :", units)
print("Total Bill     : ₹", round(bill, 2))