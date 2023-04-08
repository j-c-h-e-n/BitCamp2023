from datetime import datetime

now = datetime.now()

def get_busyness_percentage(nameOfDiner, maximumCapacity):
    listaa = get_time_info()

    if nameOfDiner == "Yahentamitsi":
        #Sunday 10am - 9pm (9pm not included)
        if listaa[1] == 6:
            if listaa[0] == 10:
                amountOfPeople = 77
            elif listaa[0] == 11:
                amountOfPeople = 113
            elif listaa[0] == 12:
                amountOfPeople = 257
            elif listaa[0] == 13:
                amountOfPeople = 430
            elif listaa[0] == 14:
                amountOfPeople = 500
            elif listaa[0] == 15:
                amountOfPeople = 528
            elif listaa[0] == 16:
                amountOfPeople = 487
            elif listaa[0] == 17:
                amountOfPeople = 371
            elif listaa[0] == 18:
                amountOfPeople = 529
            elif listaa[0] == 19:
                amountOfPeople = 674
            elif listaa[0] == 20:
                amountOfPeople = 599

        #Monday 7am - 9pm (9pm not included)
        elif listaa[1] == 0:
            if listaa[0] == 7:
                amountOfPeople = 75
            elif listaa[0] == 8:
                amountOfPeople = 115
            elif listaa[0] == 9:
                amountOfPeople = 253
            elif listaa[0] == 10:
                amountOfPeople = 485
            elif listaa[0] == 11:
                amountOfPeople = 536
            elif listaa[0] == 12:
                amountOfPeople = 699
            elif listaa[0] == 13:
                amountOfPeople = 750
            elif listaa[0] == 14:
                amountOfPeople = 732
            elif listaa[0] == 15:
                amountOfPeople = 668
            elif listaa[0] == 16:
                amountOfPeople = 501
            elif listaa[0] == 17:
                amountOfPeople = 491
            elif listaa[0] == 18:
                amountOfPeople = 687
            elif listaa[0] == 19:
                amountOfPeople = 959
            elif listaa[0] == 20:
                amountOfPeople = 888

        #Tuesday 7am - 9pm (9pm not included)
        elif listaa[1] == 1:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Wednesday 7am - 9pm (9pm not included)
        elif listaa[1] == 2:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Thrusday 7am - 9pm (9pm not included)
        elif listaa[1] == 3:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Friday 7am - 9pm (9pm not included)
        elif listaa[1] == 4:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Saturday 10am - 9pm (9pm not included)
        elif listaa[1] == 5:
            if listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

    elif nameOfDiner == "South":
        #Sunday 10am - 9pm (9pm not included)
        if listaa[1] == 6:
            if listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Monday 7am - 9pm (9pm not included)
        elif listaa[1] == 0:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Tuesday 7am - 9pm (9pm not included)
        elif listaa[1] == 1:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Wednesday 7am - 9pm (9pm not included)
        elif listaa[1] == 2:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Thrusday 7am - 9pm (9pm not included)
        elif listaa[1] == 3:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Friday 7am - 9pm (9pm not included)
        elif listaa[1] == 4:
            if listaa[0] == 7:
                amountOfPeople = 10
            elif listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10

        #Saturday 10am - 9pm (9pm not included)
        elif listaa[1] == 5:
            if listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
            elif listaa[0] == 21:
                amountOfPeople = 10
    
    elif nameOfDiner == "251North":
        #Sunday 8am - 8pm (8pm not included)
        if listaa[1] == 6:
            if listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10

        #Monday 8am - 8pm (8pm not included)
        elif listaa[1] == 0:
            if listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10

        #Tuesday 8am - 8pm (8pm not included)
        elif listaa[1] == 1:
            if listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10

        #Wednesday 8am - 8pm (8pm not included)
        elif listaa[1] == 2:
            if listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10

        #Thrusday 8am - 8pm (8pm not included)
        elif listaa[1] == 3:
            if listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10

        #Friday 8am - 8pm (8pm not included)
        elif listaa[1] == 4:
            if listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10

        #Saturday 8am - 8pm (8pm not included)
        elif listaa[1] == 5:
            if listaa[0] == 8:
                amountOfPeople = 10
            elif listaa[0] == 9:
                amountOfPeople = 10
            elif listaa[0] == 10:
                amountOfPeople = 10
            elif listaa[0] == 11:
                amountOfPeople = 10
            elif listaa[0] == 12:
                amountOfPeople = 10
            elif listaa[0] == 13:
                amountOfPeople = 10
            elif listaa[0] == 14:
                amountOfPeople = 10
            elif listaa[0] == 15:
                amountOfPeople = 10
            elif listaa[0] == 16:
                amountOfPeople = 10
            elif listaa[0] == 17:
                amountOfPeople = 10
            elif listaa[0] == 18:
                amountOfPeople = 10
            elif listaa[0] == 19:
                amountOfPeople = 10
            elif listaa[0] == 20:
                amountOfPeople = 10
    

    return str(int(float(amountOfPeople) / float(maximumCapacity) * 100))

def get_time_info():
    current_hour = now.strftime("%H")
    current_weekday = now.today().weekday()
    timeList = [current_hour, current_weekday]
    return timeList
