import random

def train():
    from mainsmartcity import inti
    print("\n\nTicket Booking System\n")
    restart = 'Y'

    while restart != ('N', 'NO', 'n', 'no'):
        print("1.Check PNR status")
        print("2.Ticket Reservation")
        print("3.Return to Smart City")
        option = int(input("\nEnter your option : "))

        if option == 1:
            number = random.randint(10000, 99999)
            print("Your PNR status is :", number)
            print("Press 0 to go to smart city")
            option1 = int(input())
            if option1 == 0:
                inti()
            else:
                exit(0)

        elif option == 2:
            people = int(input("\nEnter no. of Ticket you want : "))
            name_li = []
            age_li = []
            gender_li = []
            proof_li = []
            for p in range(people):
                name = str(input("\nName : "))
                name_li.append(name)
                age = int(input("\nAge  : "))
                age_li.append(age)
                gender = str(input("\nMale or Female : "))
                gender_li.append(gender)
                proof = str(input("\n Give any id proof details\n 1.Aadhar Number \n 3.Pan Number \n 3.Driving "
                                  "Licence \n 4. Passport Number : "))
                proof_li.append(proof)

            restart = str(input("\nDid you forgot someone? y/n: "))
            if restart in ('y', 'YES', 'yes', 'Yes'):
                restart = 'Y'
            else:
                x = 0
                print("\nTotal Ticket : ", people)
                for p in range(1, people + 1):
                    print("Ticket : ", p)
                    print("Name : ", name_li[x])
                    print("Age  : ", age_li[x])
                    print("Gender : ", gender_li[x])
                    print("Proof :", proof_li[x])
                    x += 1

        elif option == 3:
            inti()
