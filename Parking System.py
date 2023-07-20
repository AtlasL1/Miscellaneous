# Build a System
# Parking Payment: Cars, Lorrys, Motorcycles, Vans

d1a = input("\nPlease choose your vehicle: \n A) Car B) Lorry C) Motorcycle D) Van \n [A/B/C/D]?: ")  # 1ST STEP: TYPE OF VEHICLE
if d1a == "A":  # 2ND STEP: PLATE NUMBER OF VEHICLE
    plte = str(input("\nPlease enter the plate number of your vehicle: "))
elif d1a == "B":
    plte = str(input("\nPlease enter the plate number of your vehicle: "))
elif d1a == "C":
    plte = str(input("\nPlease enter the plate number of your vehicle: "))
elif d1a == "D":
    plte = str(input("\nPlease enter the plate number of your vehicle: "))

from tabulate import tabulate
data = [['Car', 'RM 1.00', 'RM 0.50'],
        ['Lorry', 'RM 3.00', 'RM 1.00'],
        ['Motorcycle', 'RM 0.50', 'RM 0.20'],
        ['Van', 'RM 2.00', 'RM 1.00']]
print(tabulate(data, headers=["Vehicle", "Price for the 1st Hour", "Price for Every Following Hour"], tablefmt="simple_outline"))

print(f"\nPLEASE NOTE THAT:")  # TO EASE THE PROCESS OF GENERATING THE PARKING COST ACCORDING TO PARKING DURATION
print(f"The time that has exceeded the previous hour is counted as an hour more.")
print(f"For example, if you entered at 7.30, please enter time of arrival = 7.00; if you are leaving at 17.45, please enter time of departure = 18.00. Thank you!")

entry = float(input("\nPlease enter time of arrival: "))  # 3RD STEP: INPUT TIME OF ARRIVAL
departure = float(input("Please enter time of departure: "))  # 4TH STEP: INPUT TIME OF DEPARTURE

prkgdrtn = departure - entry  # FORMULA FOR PARKING DURATION

if d1a == "A":  # PARKING PRICE FOR CARS
    cost = (((prkgdrtn - 1) * 0.50) + 1)
    print(f"\nPlease pay RM ", cost)
elif d1a == "B":  # PARKING PRICE FOR LORRIES
    cost = (((prkgdrtn - 1) * 1) + 3)
    print(f"\nPlease pay RM", cost)
elif d1a == "C":  # PARKING PRICE FOR MOTORCYCLES
    cost = (((prkgdrtn - 1) * 0.20) + 0.50)
    print(f"\nPlease pay RM", cost)
elif d1a == "D":  # PARKING PRICE FOR VANS
    cost = (((prkgdrtn - 1) * 1) + 2)
    print(f"\nPlease pay RM", cost)

print(f"We only take 5.00, 2.00, 1.00, 0.50, 0.20 or 0.10.")  # TO PREVENT COMPLICATIONS
cash = [5.00, 2.00, 1.00, 0.50, 0.20, 0.10]

payment = input("\nEnter a payment amount: ")

if payment not in cash:
    while True:
        print(f"\nSorry, we only accept 5.00, 2.00, 1.00, 0.50, 0.20 or 0.10.")
        print(f"Please redo your transaction correctly.")
        payment = input("Enter a payment amount: ")
        required_amount = cost
        payment_amount = payment
        while payment_amount < required_amount:
            payment2 = input("Enter a payment amount: ")
            payment2 = float(payment2)
            payment_amount += payment2
            remaining_amount = required_amount - payment_amount
            print(f"Remaining amount: {remaining_amount}")
        print("Your transaction was successful, {}!".format(plte))
        print("Thank you and please come again!")
        if payment_amount > required_amount:
            change = payment_amount - required_amount
            print("Your Change: ", change)
            print("Thank you and please come again!")
elif payment in cash:
    required_amount = cost
    payment_amount = payment
    while payment_amount < required_amount:
        payment2 = input("Enter a payment amount: ")
        payment2 = float(payment2)
        payment_amount += payment2
        remaining_amount = required_amount - payment_amount
        print(f"Remaining amount: {remaining_amount}")
    print("Your transaction was successful, {}!".format(plte))
    print("Thank you and please come again!")
    if payment_amount > required_amount:
        change = payment_amount - required_amount
        print("Your Change: ", change)
        print("Thank you and please come again!")