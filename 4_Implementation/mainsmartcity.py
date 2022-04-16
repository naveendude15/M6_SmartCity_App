import Hotelmanage
import trainbooking
import busbooking


def inti():
    print("\t\n\n ***Your are in Smart City***\n Choose the Services you are in need\n\n")
    print("\t 1 Hotel Services \n")
    print("\t 2 Train Ticket Booking\n")
    print("\t 3 Bus Ticket Reservation\n")
    print("\t 4 Tourist Places\n")
    print("\t 5 Exit")
    ch = int(input("Enter Your Choice->"))
    if ch == 1:
        print(" ")
        Hotelmanage.hotel()

    if ch == 2:
        print("")
        trainbooking.train()

    if ch == 3:
        print("")
        busbooking.bus()

    if ch == 4:
        print("")

    if ch == 5:
        print("")
        exit(0)

    else:
        inti()


inti()
