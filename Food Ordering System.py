# Build a System
# Food Ordering: Aunty Chua's Online Order

# MAIN PAGE (HEADER)
print("    ___     _   _   __   _   _______   __    __  ")
print("   / _ \   | | | | |  \ | | |__   __|  | |__| |  ")
print("  / /_\ \  | |_| | | \ \| |    | |     |____  |  ")
print(" /_/   \_\ |_____| |_|\___|    |_|     |______|  ")
print("  ______   _    _   _   _     ___    _   ______  ")
print(" |  ____| | |__| | | | | |   / _ \  |_| |   ___| ")
print(" |  |___  |  __  | | |_| |  / /_\ \      \_|___  ")
print(" |______| |_|  |_| |_____| /_/   \_\    |______\ ")

# WELCOME NOTE
print("\n        WELCOME TO AUNTY CHUA'S!            ")
print("We hope to make your experience a great one.")
tble = int(input("\nPlease enter your table number (e.g. 08): "))  # TABLE NUMBER INPUT
print("\nWelcome to Table No. {}! \nPlease make yourself at home, fellow friend. ".format(tble))  # WELCOMES CUSTOMER TO TABLE

from tabulate import tabulate

# PRINTS AUNTY CHUA'S SPECIALTIES
data = [["A01", "Aunty Chua's Signature Fried Rice", "RM 12.90"],
        ["A02", "Aunty Chua's Signature Fried Seafood Noodles", "RM 16.90"],
        ["A03", "Aunty Chua's Signature Fish n' Chips", "RM 11.10"]]

menu1 = {'A01': {'name': "Aunty Chua's Signature Fried Rice", 'price': '12.90'},
         'A02': {'name': "Aunty Chua's Signature Fried Seafood Noodles", 'price': '16.90'},
         'A03': {'name': "Aunty Chua's Signature Fish n' Chips", 'price': '11.10'}}

# PRINTS SECTION LIST
data2 = [["1", "BREAKFAST"],
         ["2", "BRUNCH"],
         ["3", "LUNCH"],
         ["4", "DINNER"],
         ["5", "SIDE DISHES"],
         ["6", "DESSERTS"],
         ["7", "BEVERAGES"],
         ["8", "AUNTY CHUA'S SPECIALTIES"]]

# PRINTS BREAKFAST
brkfstdt = [["B01", "French Toast (2 / 4 pax)", "RM 3.60 / RM 7.20"],
            ["B02", "Nasi Lemak", "RM 4.90"],
            ["B03", "Nasi Minyak (Fried Chicken Leg)", "RM 5.90"],
            ["B04", "Nasi Minyak (Curry Chicken Leg)", "RM 5.60"],
            ["B05", "Roti Canai Kosong", "RM6.70"],
            ["B06", "Roti Canai Telur", "RM 7.60"],
            ["B07", "Big Breakfast Set", "RM 10.70"]]

menu2 = {'B01': {'name': "French Toast (2 / 4 pax)", 'price': '3.60 / 7.20'},
         'B02': {'name': "Nasi Lemak", 'price': '4.90'},
         'B03': {'name': "Nasi Minyak (Fried Chicken Leg)", 'price': '5.90'},
         'B04': {'name': "Nasi Minyak (Curry Chicken Leg)", 'price': '5.60'},
         'B05': {'name': "Roti Canai Kosong", 'price': '6.70'},
         'B06': {'name': "Roti Canai Telur", 'price': '7.60'},
         'B07': {'name': "Big Breakfast Set", 'price': '10.70'}}

# PRINTS BRUNCH
brnchdt = [["C01", "Scrambled Eggs", "RM 2.50"],
           ["C02", "Scones", "RM 5.70"],
           ["C03", "Pancakes (2 / 4 pax)", "RM 6.20 / RM 12.40"],
           ["C04", "Mashed Potatoes", "RM 5.70"]]

menu3 = {'C01': {'name': "Scrambled Eggs", 'price': '2.50'},
         'C02': {'name': "Scones", 'price': '5.70'},
         'C03': {'name': "Pancakes (2 / 4 pax)", 'price': '6.20 / 12.40'},
         'C04': {'name': "Mashed Potatoes", 'price': '5.70'}}

# PRINTS LUNCH
lnchdt = [["D01", "Chicken Rice", "RM 7.80"],
          ["D02", "Duck Rice", "RM 8.90"],
          ["D03", "Kai Si Hor Fun", "RM 7.90"],
          ["D04", "Fried Sin Chew Bee Hoon", "RM 7.00"],
          ["D05", "Hokkien Mee", "RM 8.50"],
          ["D06", "Wat Tan Hor", "RM 9.90"]]

menu4 = {'D01': {'name': "Chicken Rice", 'price': '7.80'},
         'D02': {'name': "Duck Rice", 'price': '8.90'},
         'D03': {'name': "Kai Si Hor Fun", 'price': '7.90'},
         'D04': {'name': "Fried Sin Chew Bee Hoon", 'price': '7.00'},
         'D05': {'name': "Hokkien Mee", 'price': '8.50'},
         'D06': {'name': "Wat Tan Hor", 'price': '9.90'}}

# PRINTS DINNER
dnnrdt = [["E01", "Chicken Porridge", "RM 6.70"],
          ["E02", "Mackerel Porridge", "RM 12.10"],
          ["E03", "Homemade Pizza (2 / 4 pax)", "RM 4.60 / RM 9.10"],
          ["E04", "Fried Chicken Chop", "RM 10.20"],
          ["E05", "Grilled Chicken Chop", "RM 10.10"],
          ["E06", "Creamy Spaghetti Carbonara", "RM 11.00"],
          ["E07", "Bacon Spaghetti Aglio Olio", "RM 12.20"]]

menu5 = {'E01': {'name': "Chicken Porridge", 'price': '6.70'},
         'E02': {'name': "Mackerel Porridge", 'price': '12.10'},
         'E03': {'name': "Homemade Pizza (2 / 4 pax)", 'price': '4.60 / 9.10'},
         'E04': {'name': "Fried Chicken Chop", 'price': '10.20'},
         'E05': {'name': "Grilled Chicken Chop", 'price': '10.10'},
         'E06': {'name': "Creamy Spaghetti Carbonara", 'price': '11.00'},
         'E07': {'name': "Bacon Spaghetti Aglio Olio", 'price': '12.20'}}

# PRINTS SIDE DISHES
sddt = [["F01", "Garlic Bread & Mushroom Soup", "RM 5.00"],
        ["F02", "Coleslaw", "RM 4.40"],
        ["F03", "Caesar Salad", "RM 4.40"],
        ["F04", "French Fries", "RM 5.20"],
        ["F05", "Pigs in Blankets", "RM 6.00"]]

menu6 = {'F01': {'name': "Garlic Bread & Mushroom Soup", 'price': '5.00'},
         'F02': {'name': "Coleslaw", 'price': '4.40'},
         'F03': {'name': "Caesar Salad", 'price': '4.40'},
         'F04': {'name': "French Fries", 'price': '5.20'},
         'F05': {'name': "Pigs in Blankets", 'price': '6.00'}}

# PRINTS DESSERTS
dssrtsdt = [["G01", "Banana Split", "RM 6.70"],
            ["G02", "Chocolate Cream Cake", "RM 7.80"],
            ["G03", "Vanilla Cream Cake", "RM 7.80"],
            ["G04", "Burnt Butter Cake", "RM 7.80"],
            ["G05", "Walnut Brownies with Whipped Cream", "RM 7.80"]]

menu7 = {'G01': {'name': "Banana Split", 'price': '6.70'},
         'G02': {'name': "Chocolate Cream Cake", 'price': '7.80'},
         'G03': {'name': "Vanilla Cream Cake", 'price': '7.80'},
         'G04': {'name': "Burnt Butter Cake", 'price': 'RM 7.80'},
         'G05': {'name': "Walnut Brownies with Whipped Cream", 'price': 'RM 7.00'}}

# PRINTS BEVERAGES
bvrgsdt = [["H01", "Milo (Hot / Cold)", "RM 1.20 / RM 1.30"],
           ["H02", "Teh O (Hot / Cold)", "RM 1.20 / RM 1.30"],
           ["H03", "Teh C (Hot / Cold)", "RM 1.20 / RM 1.30"],
           ["H04", "Lemon Tea (Hot / Cold)", "RM 1.20 / RM 1.30"],
           ["H05", "Honey Lemon (Hot / Cold)", "RM 1.20 / RM 1.30"],
           ["H06", "Lime Plum (Hot / Cold)", "RM 1.20 / RM 1.30"],
           ["H07", "Passionfruit Plum (Hot / Cold)", "RM 1.20 / RM 1.30"],
           ["H08", "Hot Chocolate", "RM 3.20"],
           ["H09", "Milk Tea", "RM 3.20"],
           ["H10", "Lemongrass Tea", "RM 3.20"],
           ["H11", "Barley (Hot / Cold)", "RM 3.20 / RM 3.30"],
           ["H12", "Coconut Water", "RM 3.20"],
           ["H13", "100Plus", "RM 3.20"],
           ["H14", "CocaCola", "RM 3.20"]]

menu8 = {'H01': {'name': "Milo (Hot / Cold)", 'price': '1.20 / 1.30'},
         'H02': {'name': "Teh O (Hot / Cold)", 'price': '1.20 / 1.30'},
         'H03': {'name': "Teh C (Hot / Cold)", 'price': '1.20 / 1.30'},
         'H04': {'name': "Lemon Tea (Hot / Cold)", 'price': '1.20 / 1.30'},
         'H05': {'name': "Honey Lemon (Hot / Cold)", 'price': '1.20 / 1.30'},
         'H06': {'name': "Lime Plum (Hot / Cold)", 'price': '1.20 / 1.30'},
         'H07': {'name': "Passionfruit Plum (Hot / Cold)", 'price': '1.20 / 1.30'},
         'H08': {'name': "Hot Chocolate", 'price': '3.20'},
         'H09': {'name': "Milk Tea", 'price': '3.20'},
         'H10': {'name': "Lemongrass Tea", 'price': '3.20'},
         'H11': {'name': "Barley (Hot / Cold)", 'price': '3.20 / 3.30'},
         'H12': {'name': "Coconut Water", 'price': '3.20'},
         'H13': {'name': "100Plus", 'price': '3.20'},
         'H14': {'name': "CocaCola", 'price': '3.20'}}

# AUNTY CHUA'S FREE WIFI
wifi = [["WiFi Name", "Aunty Chua's WiFi_Guest"],
        ["Password", "prettyauntychua"]]

d1a = input("\nA) Start Order B) My Orders \n[A/B]?: ")  # CUSTOMER CHOOSES TO START NEW ORDER OR TO VIEW CART
if d1a == "A":  # CUSTOMER STARTS NEW ORDER
    print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
    d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
    if d2a == "0":  # CUSTOMER WANTS SOMETHING ELSE INSTEAD OF SPECIALTIES
        print("\n\nCheck these out!\n")
        print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
        d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
        while True:
            if d3a == "1":  # CUSTOMER VIEWS BREAKFAST SECTION
                print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                if d4a == "0":  # CUSTOMER CHECKS OUT OTHER SECTIONS (BACK TO SECTION LIST)
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                    if d3a == "1":  # CUSTOMER VIEWS BREAKFAST SECTION
                        print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                        d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:  # CUSTOMER CHOOSES FROM BREAKFAST
                            quantity2 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "2":  # CUSTOMER VIEWS BRUNCH SECTION
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:  # CUSTOMER CHOOSES FROM BRUNCH
                            quantity3 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "3":  # CUSTOMER VIEWS LUNCH SECTION
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:  # CUSTOMER CHOOSES FROM LUNCH
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":  # CUSTOMER VIEWS DINNER SECTION
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:  # CUSTOMER CHOOSES FROM DINNER
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":  # CUSTOMER VIEWS SIDE DISHES SECTION
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:  # CUSTOMER CHOOSES FROM SIDE DISHES
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":  # CUSTOMER VIEWS DESSERTS SECTION
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:  # CUSTOMER CHOOSES FROM DESSERTS
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":  # CUSTOMER VIEWS BEVERAGES SECTION
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0]? ( 0 = I Would Like To Check Out Other Sections): ")
                        if not flag:  # CUSTOMER CHOOSES FROM BEVERAGES
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":  # CUSTOMER VIEWS SPECIALTIES SECTION
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                        if not flag:  # CUSTOMER CHOOSES FROM SPECIALTIES
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity2 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
            elif d3a == "2":  # CUSTOMER VIEWS BRUNCH SECTION
                print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                d4a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                if d4a == "0":
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                if d3a == "1":
                    print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                    d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                    if not flag:
                        quantity2 = int(input("\nQuantity: "))
                        print("Your order has been added to cart successfully!")
                    elif d3a == "2":
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity3 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "3":
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
                        if not flag:
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                        if not flag:
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity3 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
            elif d3a == "3":  # CUSTOMER VIEWS LUNCH SECTION
                print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                d5a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                if d5a == "0":
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                    if d3a == "1":
                        print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                        d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity2 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "2":
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity3 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "3":
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
                        if not flag:
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                        if not flag:
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity4 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
            elif d3a == "4":  # CUSTOMER VIEWS DINNER SECTION
                print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                flag = False
                if d7a == "0":
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                    if d3a == "1":
                        print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                        d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity2 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "2":
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity3 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "3":
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
                        if not flag:
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                        if not flag:
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity5 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
            elif d3a == "5":  # CUSTOMER VIEWS SIDE DISHES SECTION
                print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                if d8a == "0":
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                    if d3a == "1":
                        print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                        d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity2 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "2":
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                    if not flag:
                        quantity3 = int(input("\nQuantity: "))
                        print("Your order has been added to cart successfully!")
                    elif d3a == "3":
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
                        if not flag:
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                        if not flag:
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity6 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
            elif d3a == "6":  # CUSTOMER VIEWS DESSERTS SECTION
                print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                if d9a == "0":
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                    if d3a == "1":
                        print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                        d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity2 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "2":
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity3 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "3":
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
                        if not flag:
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                        if not flag:
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity8 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
            elif d3a == "7":  # CUSTOMER VIEWS BEVERAGES SECTION
                print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
                if d0a == "0":
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                    if d3a == "1":
                        print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                        d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity2 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "2":
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity3 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "3":
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0]? ( 0 = I Would Like To Check Out Other Sections): ")
                        if not flag:
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Somethng Else): ")
                        if not flag:
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity9 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
            elif d3a == "8":  # CUSTOMER VIEWS SPECIALTIES SECTION
                print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                if d2a == "0":
                    print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
                    d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
                    if d3a == "1":
                        print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
                        d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity2 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "2":
                        print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
                        d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity3 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "3":
                        print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
                        d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity4 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "4":
                        print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
                        d7a = input("\n[E01 / E02 / 203 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity5 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "5":
                        print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
                        d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity6 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "6":
                        print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
                        d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
                        if not flag:
                            quantity7 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "7":
                        print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
                        d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
                        if not flag:
                            quantity8 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                    elif d3a == "8":
                        print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
                        d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
                        if not flag:
                            quantity1 = int(input("\nQuantity: "))
                            print("Your order has been added to cart successfully!")
                else:
                    quantity1 = int(input("\nQuantity: "))
                    print("Your order has been added to cart successfully!")
                    break
    else:  # CUSTOMER IMMEDIATELY ORDERS FROM SPECIALTIES
        quantity1 = int(input("\nQuantity: "))
        print("Your order has been added to cart successfully!")

flag = False
while True:
    extra = input("\nWould you like to order something else? \n[Yes / No]: ")  # CUSTOMER CHOOSES TO ORDER MORE OR TO STOP
    if extra == "Yes":  # CUSTOMER ORDERS MORE
        print(tabulate(data2, headers=["Index", "Section"], tablefmt="mixed_outline"))
        d3a = input("\n[1/2/3/4/5/6/7/8]?: ")
        if d3a == "1":  # CUSTOMER VIEWS BREAKFAST SECTION
            print(tabulate(brkfstdt, headers=["Index", "BREAKFAST", "Price"], tablefmt="fancy_grid"))
            d4a = input("\n[B01 / B02 / B03 / B04 / B05 / B06 / B07 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
            if not flag:  # CUSTOMER CHOOSES FROM BREAKFAST
                quantity2 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
        elif d3a == "2":  # CUSTOMER VIEWS BRUNCH SECTION
            print(tabulate(brnchdt, headers=["Index", "BRUNCH", "Price"], tablefmt="fancy_grid"))
            d5a = input("\n[C01 / C02 / C03 / C04 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
            if not flag:  # CUSTOMER CHOOSES FROM BRUNCH
                quantity3 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
        elif d3a == "3":  # CUSTOMER VIEWS LUNCH SECTION
            print(tabulate(lnchdt, headers=["Index", "LUNCH", "Price"], tablefmt="fancy_grid"))
            d6a = input("\n[D01 / D02 / D03 / D04 / D05 / D06 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
            if not flag:  # CUSTOMER CHOOSES FROM LUNCH
                quantity4 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
        elif d3a == "4":  # CUSTOMER VIEWS DINNER SECTION
            print(tabulate(dnnrdt, headers=["Index", "DINNER", "Price"], tablefmt="fancy_grid"))
            d7a = input("\n[E01 / E02 / E03 / E04 / E05 / E06 / E07 / 0 ( 0 = I Would Like to Check Out Other Sections): ")
            if not flag:  # CUSTOMER CHOOSES FROM DINNER
                quantity5 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
        elif d3a == "5":  # CUSTOMER VIEWS SIDE DISHES SECTION
            print(tabulate(sddt, headers=["Index", "SIDE DISHES", "Price"], tablefmt="fancy_grid"))
            d8a = input("\n[F01 / F02 / F03 / F04 / F05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
            if not flag:  # CUSTOMER CHOOSES FROM SIDE DISHES
                quantity6 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
        elif d3a == "6":  # CUSTOMER VIEWS DESSERTS SECTION
            print(tabulate(dssrtsdt, headers=["Index", "DESSERTS", "Price"], tablefmt="fancy_grid"))
            d9a = input("\n[G01 / G02 / G03 / G04 / G05 / 0]? ( 0 = I Would Like to Check Out Other Sections): ")
            if not flag:  # CUSTOMER CHOOSES FROM DESSERTS
                quantity7 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
        elif d3a == "7":  # CUSTOMER VIEWS BEVERAGES SECTION
            print(tabulate(bvrgsdt, headers=["Index", "BEVERAGES", "Price"], tablefmt="fancy_grid"))
            d0a = input("\n[H01 / H02 / H03 / H04 / H05 / H06 / H07 / H08 / H09 / H10 / H11 / H12 / H13 / H14 / 0 ( 0 = i Would Like To Check Out Other Sections): ")
            if not flag:  # CUSTOMER CHOOSES FROM BEVERAGES
                quantity8 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
        elif d3a == "8":  # CUSTOMER VIEWS SPECIALTIES SECTION
            print(tabulate(data, headers=["Index", "AUNTY CHUA'S SPECIALTIES", "Price"], tablefmt="outline"))
            d2a = input("\n[A01 / A02 / A03 / 0 ]? ( 0 = Want Something Else): ")
            if not flag:  # CUSTOMER CHOOSES FROM SPECIALTIES
                quantity1 = int(input("\nQuantity: "))
                print("Your order has been added to cart successfully!")
    elif extra == "No":  # CUSTOMER DOES NOT WANT TO ORDER ANYTHING ELSE
        opt = input("\nWould you like to proceed to checkout? [Yes (Proceed to Checkout) / No (Go Back to Cart)]: ")
        if opt == "No":
            print("\nYOUR CART")
            print("_________\n")

            try:
                item_name1 = menu1[d2a]['name']
                item_price1 = menu1[d2a]['price']
                item_price1_str = float(item_price1)
                total_price1 = item_price1_str * quantity1
            except KeyError as e:
                total_price1 = 0
            except NameError as e:
                total_price1 = 0
            else:
                print(f'Item name: {item_name1}')
                print(f'Item price: RM {item_price1}')
                print(f'Quantity: {quantity1}')
                print(f'Total price: RM {total_price1} \n')

            try:
                item_name2 = menu2[d4a]['name']
                item_price2 = menu2[d4a]['price']
                item_price2_str = float(item_price2)
                total_price2 = item_price2_str * quantity2
            except KeyError as e:
                total_price2 = 0
            except NameError as e:
                total_price2 = 0
            else:
                print(f'Item name: {item_name2}')
                print(f'Item price: RM {item_price2}')
                print(f'Quantity: {quantity2}')
                print(f'Total price: RM {total_price2} \n')

            try:
                item_name3 = menu3[d5a]['name']
                item_price3 = menu3[d5a]['price']
                item_price3_str = float(item_price3)
                total_price3 = item_price3_str * quantity3
            except KeyError as e:
                total_price3 = 0
            except NameError as e:
                total_price3 = 0
            else:
                print(f'Item name: {item_name3}')
                print(f'Item price: RM {item_price3}')
                print(f'Quantity: {quantity3}')
                print(f'Total price: RM {total_price3} \n')

            try:
                item_name4 = menu4[d6a]['name']
                item_price4 = menu4[d6a]['price']
                item_price4_str = float(item_price4)
                total_price4 = item_price4_str * quantity4
            except KeyError as e:
                total_price4 = 0
            except NameError as e:
                total_price4 = 0
            else:
                print(f'Item name: {item_name4}')
                print(f'Item price: RM {item_price4}')
                print(f'Quantity: {quantity4}')
                print(f'Total price: RM {total_price4} \n')

            try:
                item_name5 = menu5[d7a]['name']
                item_price5 = menu5[d7a]['price']
                item_price5_str = float(item_price5)
                total_price5 = item_price5_str * quantity5
            except KeyError as e:
                total_price5 = 0
            except NameError as e:
                total_price5 = 0
            else:
                print(f'Item name: {item_name5}')
                print(f'Item price: RM {item_price5}')
                print(f'Quantity: {quantity5}')
                print(f'Total price: RM {total_price5} \n')

            try:
                item_name6 = menu6[d8a]['name']
                item_price6 = menu6[d8a]['price']
                item_price6_str = float(item_price6)
                total_price6 = item_price6_str * quantity6
            except KeyError as e:
                total_price6 = 0
            except NameError as e:
                total_price6 = 0
            else:
                print(f'Item name: {item_name6}')
                print(f'Item price: RM {item_price6}')
                print(f'Quantity: {quantity6}')
                print(f'Total price: RM {total_price6} \n')

            try:
                item_name7 = menu7[d9a]['name']
                item_price7 = menu7[d9a]['price']
                item_price7_str = float(item_price7)
                total_price7 = item_price7_str * quantity7
            except KeyError as e:
                total_price7 = 0
            except NameError as e:
                total_price7 = 0
            else:
                print(f'Item name: {item_name7}')
                print(f'Item price: RM {item_price7}')
                print(f'Quantity: {quantity7}')
                print(f'Total price: RM {total_price7} \n')

            try:
                item_name8 = menu8[d0a]['name']
                item_price8 = menu8[d0a]['price']
                item_price8_str = float(item_price1)
                total_price8 = item_price8_str * quantity8
            except KeyError as e:
                total_price8 = 0
            except NameError as e:
                total_price8 = 0
            else:
                print(f'Item name: {item_name8}')
                print(f'Item price: RM {item_price8}')
                print(f'Quantity: {quantity8}')
                print(f'Total price: RM {total_price8} \n')
        elif opt == "Yes":
            print("\n                                YOUR CART")
            print("_______________________________________________________________________________\n")

            try:
                item_name1 = menu1[d2a]['name']
                item_price1 = menu1[d2a]['price']
                item_price1_str = float(item_price1)
                total_price1 = item_price1_str * quantity1
            except KeyError as e:
                total_price1 = 0
            except NameError as e:
                total_price1 = 0
            else:
                print(f'Item name: {item_name1}')
                print(f'Item price: RM {item_price1}')
                print(f'Quantity: {quantity1}')
                print(f'Total price: RM {total_price1} \n')

            try:
                item_name2 = menu2[d4a]['name']
                item_price2 = menu2[d4a]['price']
                item_price2_str = float(item_price2)
                total_price2 = item_price2_str * quantity2
            except KeyError as e:
                total_price2 = 0
            except NameError as e:
                total_price2 = 0
            else:
                print(f'Item name: {item_name2}')
                print(f'Item price: RM {item_price2}')
                print(f'Quantity: {quantity2}')
                print(f'Total price: RM {total_price2} \n')

            try:
                item_name3 = menu3[d5a]['name']
                item_price3 = menu3[d5a]['price']
                item_price3_str = float(item_price3)
                total_price3 = item_price3_str * quantity3
            except KeyError as e:
                total_price3 = 0
            except NameError as e:
                total_price3 = 0
            else:
                print(f'Item name: {item_name3}')
                print(f'Item price: RM {item_price3}')
                print(f'Quantity: {quantity3}')
                print(f'Total price: RM {total_price3} \n')

            try:
                item_name4 = menu4[d6a]['name']
                item_price4 = menu4[d6a]['price']
                item_price4_str = float(item_price4)
                total_price4 = item_price4_str * quantity4
            except KeyError as e:
                total_price4 = 0
            except NameError as e:
                total_price4 = 0
            else:
                print(f'Item name: {item_name4}')
                print(f'Item price: RM {item_price4}')
                print(f'Quantity: {quantity4}')
                print(f'Total price: RM {total_price4} \n')

            try:
                item_name5 = menu5[d7a]['name']
                item_price5 = menu5[d7a]['price']
                item_price5_str = float(item_price5)
                total_price5 = item_price5_str * quantity5
            except KeyError as e:
                total_price5 = 0
            except NameError as e:
                total_price5 = 0
            else:
                print(f'Item name: {item_name5}')
                print(f'Item price: RM {item_price5}')
                print(f'Quantity: {quantity5}')
                print(f'Total price: RM {total_price5} \n')

            try:
                item_name6 = menu6[d8a]['name']
                item_price6 = menu6[d8a]['price']
                item_price6_str = float(item_price6)
                total_price6 = item_price6_str * quantity6
            except KeyError as e:
                total_price6 = 0
            except NameError as e:
                total_price6 = 0
            else:
                print(f'Item name: {item_name6}')
                print(f'Item price: RM {item_price6}')
                print(f'Quantity: {quantity6}')
                print(f'Total price: RM {total_price6} \n')

            try:
                item_name7 = menu7[d9a]['name']
                item_price7 = menu7[d9a]['price']
                item_price7_str = float(item_price7)
                total_price7 = item_price7_str * quantity7
            except KeyError as e:
                total_price7 = 0
            except NameError as e:
                total_price7 = 0
            else:
                print(f'Item name: {item_name7}')
                print(f'Item price: RM {item_price7}')
                print(f'Quantity: {quantity7}')
                print(f'Total price: RM {total_price7} \n')

            try:
                item_name8 = menu8[d0a]['name']
                item_price8 = menu8[d0a]['price']
                item_price8_str = float(item_price1)
                total_price8 = item_price8_str * quantity8
            except KeyError as e:
                total_price8 = 0
            except NameError as e:
                total_price8 = 0
            else:
                print(f'Item name: {item_name8}')
                print(f'Item price: RM {item_price8}')
                print(f'Quantity: {quantity8}')
                print(f'Total price: RM {total_price8} \n')
            plspay = total_price1 + total_price2 + total_price3 + total_price4 + total_price5 + total_price6 + total_price7 + total_price8
            plspayy = round(plspay, 2)
            print("Your total payment: ", plspayy)
            print("_______________________________________________________________________________")
            print(f"\nFor now, we only accept cash.")
            print(f"We are hoping to improve our service by enabling payment through online wallet and credit cards in the future. Please be considerate!")
            print(f"We only take 200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20 or 0.10.")
            cash = [200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10]
            plspay2 = float(input("Please enter a payment amount: "))
            required_amount = plspay
            if plspay2 in cash:
                while plspay2 < required_amount:
                    plspay3 = input("Please enter a payment amount: ")
                    plspay3 = float(plspay3)
                    plspay3 += plspay2
                    remaining_amount = required_amount - plspay3
                    print(f"Remaining amount: RM {remaining_amount}")
                if plspay2 > required_amount:
                    change = plspay2 - required_amount
                    print("\nYour Change: RM", change)
                    print("Thank you and please come again!")
                    break
                elif plspay2 == required_amount:
                    print("\nYour "
                          "transaction was successful!")
                    print("Thank you and please come again!")
                    break
            else:
                print(f"\nSorry, we only accept 200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20 or 0.10.")
                print(f"Please redo your transaction correctly.")
                plspay2 = float(input("Please enter a payment amount: "))
                while plspay2 < required_amount:
                    plspay3 = input("Please enter a payment amount: ")
                    plspay3 = float(plspay3)
                    plspay3 += plspay2
                    remaining_amount = required_amount - plspay3
                    print(f"Remaining amount: RM {remaining_amount}")
                if plspay2 > required_amount:
                    change = plspay2 - required_amount
                    print("\nYour Change: RM", change)
                    print("Thank you and please come again!")
                    break
                elif plspay2 == required_amount:
                    print("\nYour transaction was successful!")
                    print("Thank you and please come again!")
                    break
                break