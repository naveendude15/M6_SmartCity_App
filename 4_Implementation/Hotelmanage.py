import random


name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

i = 0


def hotel():
    from mainsmartcity import inti
    print("\t\t HAPPY TO SEE YOU IN OUR HOTEL\n")
    print("\t\t\t 1 Reservation\n")
    print("\t\t\t 2 Rooms Details\n")
    print("\t\t\t 3 Service Provided & Menu Card\n")
    print("\t\t\t 4 Payments\n")
    print("\t\t\t 5 Customer Details\n")
    print("\t\t\t 6 Exit\n")
    print("\t\t\t 7 Return to Smart City\n")

    inp = int(input("Enter Your Choice->"))

    if inp == 1:
        print(" ")
        Booking()

    elif inp == 2:
        print(" ")
        Rooms_Details()

    elif inp == 3:
        print(" ")
        menu()

    elif inp == 4:
        Payment()

    elif inp == 5:
        CustDetail()

    elif inp == 6:
        inti()

    else:
        inti()


def Booking():

    global i
    print(" BOOKING ROOMS")
    print(" ")

    while 1:
        n = str(input("Name: "))
        p1 = str(input("Mobile No: "))
        a = str(input("Address: "))

        # checks if any field is not empty
        if n != "" and p1 != "" and a != "":
            name.append(n)
            add.append(a)
            break

        else:
            print("\tName, Mobile no. & Address cannot be empty..!!")

    print("----Select the type of room you want----")
    print(" 1. Normal Non-AC - Rs. 2100")
    print(" 2. Normal AC - Rs. 2600")
    print(" 3. 4-Bed Non-AC - Rs. 3500")
    print(" 4. 4-Bed AC - Rs. 4000")
    print(" 5. 5-Bed AC - Rs. 4500")
    print(" 6. 5-Bed Non-AC - Rs. 3500")
    print(" 7. 6-Bed AC - Rs. 7500")
    print(" 8. 6-Bed Non-AC - Rs. 6500")

    print("\t\tPress 0 for Room Prices")

    ch = int(input("->"))

    # if-conditions to display alloted room
    # type and it's price
    if ch == 0:
        print(" 1. Normal Non-AC - Rs. 2100")
        print(" 2. Normal AC - Rs. 2600")
        print(" 3. 4-Bed Non-AC - Rs. 3500")
        print(" 4. 4-Bed AC - Rs. 4000")
        print(" 5. 5-Bed AC - Rs. 4500")
        print(" 6. 5-Bed Non-AC - Rs. 3500")
        print(" 7. 6-Bed AC - Rs. 7500")
        print(" 8. 6-Bed Non-AC - Rs. 6500")

        ch = int(input("->"))
    if ch == 1:
        room.append('Normal Non-AC')
        print("Room Type- Normal Non-AC")
        price.append(2100)
        print("Price- 2100")
    elif ch == 2:
        room.append(' Normal AC')
        print("Room Type-  Normal AC")
        price.append(2600)
        print("Price- 2600")
    elif ch == 3:
        room.append('4-Bed Non-AC')
        print("Room Type- 4-Bed Non-AC")
        price.append(3500)
        print("Price- 3500")
    elif ch == 4:
        room.append('4-Bed AC')
        print("Room Type- 4-Bed AC")
        price.append(4000)
        print("Price- 4000")
    elif ch == 5:
        room.append('5-Bed AC')
        print("Room Type- 5-Bed AC")
        price.append(4500)
        print("Price- 4500")
    elif ch == 6:
        room.append('5-Bed Non-AC')
        print("Room Type- 5-Bed Non-AC")
        price.append(3500)
        print("Price- 3500")
    elif ch == 7:
        room.append('6-Bed AC')
        print("Room Type- 6-Bed AC")
        price.append(7500)
        print("Price- 7500")
    elif ch == 8:
        room.append(' 6-Bed Non-AC')
        print("Room Type-  6-Bed Non-AC")
        price.append(6500)
        print("Price- 6500")
    else:
        print(" Choose different choice..!!")

    # randomly generating room no. and customer
    # id for customer
    rn = random.randrange(40) + 300
    cid = random.randrange(40) + 10

    # checks if alloted room no. & customer
    # id already not alloted
    while rn in roomno or cid in custid:
        rn = random.randrange(60) + 300
        cid = random.randrange(60) + 10

    rc.append(0)
    p.append(0)

    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 1:
                    phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 0:
                    print("\tPhone no. already exists and payment yet not done..!!")
                    name.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()
    print("")
    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
    print("Room No. - ", rn)
    print("Customer Id - ", cid)
    roomno.append(rn)
    custid.append(cid)
    i = i + 1
    n = int(input("0-BACK\n ->"))
    if n == 0:
        hotel()
    else:
        exit()


def Rooms_Details():
    print("		 ------ HOTEL ROOMS INFO ------ ")
    print("")
    print("Normal Non-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached restroom with hot/ cold water.\n")
    print("Normal AC ")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Table with 2 sofa, Balcony and")
    print("an attached restroom with hot/ cold water + Window/Split AC.\n")
    print("4-Bed Non-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 3 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("an attached restroom with hot/ cold water.\n")
    print("4-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 4 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("an attached restroom with hot/ cold water + Window/Split AC.\n\n")
    print("5-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 5 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("an attached restroom with hot/ cold water + Window/Split AC.\n\n")
    print("5-Bed Non-AC ")
    print("---------------------------------------------------------------")
    print("Room amenities include: 4 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print("6-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 4 Double Bed + 2 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print("6-Bed Non-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 5 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n = int(input("0-BACK\n ->"))
    if n == 0:
        hotel()
    else:
        exit()


# RESTAURANT FUNCTION
def menu():
    ph = int(input("Customer Id: "))
    global i
    f = 0
    r = 0
    for n in range(0, i):
        if custid[n] == ph and p[n] == 0:
            f = 1
            print("-------------------------------------------------------------------------")
            print("						 Hotel MayFlower")
            print("-------------------------------------------------------------------------")
            print("						 Menu Card")
            print("-------------------------------------------------------------------------")
            print("\n DRINKS							 26 Dal Fry................ 140.00")
            print("----------------------------------	 27 Dal Makhan............ 150.00")
            print(" 1 Regular Tea............. 20.00	 28 Dal Tanka.............. 150.00")
            print(" 2 Masala Tea.............. 25.00")
            print(" 3 Coffee.................. 25.00	 ROTI")
            print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
            print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
            print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
            print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
            print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
            print(" 9 Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00	 RICE")
            print("									 ----------------------------------")
            print(" SOUPS								 33 Plain Rice.............. 90.00")
            print("----------------------------------	 34 Jeera Rice.............. 90.00")
            print(" 11 Tomato Soup............ 100.00	 35 Veg Pulao.............. 110.00")
            print(" 12 Hot & Sour............. 220.00	 36 Peas Pulao............. 110.00")
            print(" 13 Veg. Noodle Soup....... 200.00")
            print(" 14 Sweet Corn............. 120.00	 SOUTH INDIAN")
            print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
            print("									 37 Plain Dosa............. 100.00")
            print(" MAIN COURSE						 38 Onion Dosa............. 110.00")
            print("----------------------------------	 39 Masala Dosa............ 130.00")
            print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
            print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
            print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
            print(" 19 Palak Paneer........... 120.00")
            print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
            print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
            print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
            print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
            print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
            print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
            print("Press 0 -to end ")
            ch = 1
            while ch != 0:

                ch = int(input(" Select your preferred recipe-> "))

                # if-elif-conditions to assign item
                # prices listed in menu card
                if ch == 1 or ch == 31 or ch == 32:
                    rs = 20
                    r = r + rs
                elif 4 >= ch >= 2:
                    rs = 25
                    r = r + rs
                elif 6 >= ch >= 5:
                    rs = 30
                    r = r + rs
                elif 8 >= ch >= 7:
                    rs = 50
                    r = r + rs
                elif 10 >= ch >= 9:
                    rs = 70
                    r = r + rs
                elif (17 >= ch >= 11) or ch == 35 or ch == 36 or ch == 38:
                    rs = 110
                    r = r + rs
                elif 19 >= ch >= 18:
                    rs = 120
                    r = r + rs
                elif (26 >= ch >= 20) or ch == 42:
                    rs = 140
                    r = r + rs
                elif 28 >= ch >= 27:
                    rs = 150
                    r = r + rs
                elif 30 >= ch >= 29:
                    rs = 15
                    r = r + rs
                elif ch == 33 or ch == 34:
                    rs = 90
                    r = r + rs
                elif ch == 37:
                    rs = 100
                    r = r + rs
                elif 41 >= ch >= 39:
                    rs = 130
                    r = r + rs
                elif 46 >= ch >= 43:
                    rs = 60
                    r = r + rs
                elif ch == 0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ", r)

            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        hotel()
    else:
        exit()


def Payment():
    ph = str(input("Moblie Number: "))
    global i
    f = 0
    for n in range(0, i):
        if ph == phno[n]:

            # checks if payment is
            # not already done
            if p[n] == 0:
                f = 1
                print(" --------------------------------")
                print(" MODE OF PAYMENT")
                print(" --------------------------------")

                print(" 1- Credit/Debit Card")
                print(" 2- Paytm/PhonePe")
                print(" 3- Using UPI")
                print(" 4- Cash")
                x = int(input("-> "))
                print("\n Amount: ", (price[n]))
                print("\n		 Pay the Hotel Bill")
                print(" (y/n)")
                ch = str(input("->"))

                if ch == 'y' or ch == 'Y':
                    print("\n\n --------------------------------")
                    print("		 Hotel Bill")
                    print(" --------------------------------")
                    print(" Name: ", name[n], "\t\n Phone No: ", phno[n], "\t\n Address: ", add[n], "\t")
                    # print("\n Check-In: ", checkin[n], "\t\n Check-Out: ", checkout[n], "\t")
                    # print("\n Room Type: ", room[n], "\t\n Room Charges: ", price[n] * day[n], "\t")
                    print(" Restaurant Charges: \t", rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ", (price[n]) + rc[n], "\t")
                    print(" --------------------------------")
                    print("		 Thank You")
                    print("		 Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n, 1)

                    # pops room no. and customer id from list and
                    # later assigns zero at same position
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n, 0)
                    custid.insert(n, 0)

            else:

                for j in range(n + 1, i):
                    if ph == phno[j]:
                        if p[j] == 0:
                            pass

                        else:
                            f = 1
                            print("\n\tPayment has been Made :)\n\n")
    if f == 0:
        print("Invalid Customer Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        hotel()
    else:
        exit()



def CustDetail():
    if phno != []:
        print("	 *** HOTEL RECORD ***\n")
        print("| Name	 | Phone No. | Address	 | Room Type	 | Price	 |")
        print(
            "----------------------------------------------------------------------------------------------------------------------")

        for n in range(0, i):
            print("|", name[n], "\t |", phno[n], "\t|", add[n], "\t|", room[n], "\t|", price[n], "\t|")

        print(
            "----------------------------------------------------------------------------------------------------------------------")

    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        hotel()

    else:
        exit()
