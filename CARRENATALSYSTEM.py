from datetime import timedelta, datetime
print()

print("CAR RENTAL SYSTEM")

print()

def RentalDate():
    isValid = False
    while not isValid:
        RentalDate = input("Rental Date: mm/dd/yy: ")
        try:
            rd = datetime.strptime(RentalDate, "%m/%d/%y")
            isValid = True
        except:
            print("Invalid Format!\n")
            break
    return rd


# t = (RentalDate() - datetime.now()).total_seconds()
trd = (RentalDate())


# print(t)


def ReturnDate():
    isValid = False
    while not isValid:
        ReturnRental = input("Return Date: mm/dd/yy: ")
        try:
            rrl = datetime.strptime(ReturnRental, "%m/%d/%y")
            isValid = True
        except:
            print("Invalid Format!\n")
            break
    return rrl


# r = (ObtainDate() - datetime.now()).total_seconds()
rrd = (ReturnDate())


# print(rrd)

def main():

    print("Car Rental Program \n")

    totaldays = (ReturnDate() - RentalDate()).days

    x = (RentalDate())

    m = (ReturnDate())

    print("Total number of days for car rent: ",totaldays)

    print()

    tarriff = 65.00

    tax = 0.06 * 65.00

    if totaldays < 5:

        mytotal = tarriff * totaldays

        print(mytotal)
    else:
        mytotal = tarriff * tax * totaldays

        print("Total rent is: ", mytotal)

        print()

    print("RENTING DATE: ", x)

    print("RETURNING DATE: ", m)
    # print("TARIFF PER DAY: ", locale.currency(tariff), tariff_msg)
    print("TOTAL DAYS: ", totaldays)

    print()

    print("TOTAL COST: ", mytotal)

    print()
    print()


main()
