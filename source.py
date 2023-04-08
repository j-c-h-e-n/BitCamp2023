from datetime import datetime

now = datetime.now()

def get_busyness_percentage(nameOfDiner, maximumCapacity):
    time_list = get_time_info()

    if nameOfDiner == "Yahentamitsi":

        #Sunday 10am - 9pm (9pm not included)
        if time_list[1] == 6:
            if time_list[0] == 10:
                amountOfPeople = 77
            elif time_list[0] == 11:
                amountOfPeople = 113
            elif time_list[0] == 12:
                amountOfPeople = 257
            elif time_list[0] == 13:
                amountOfPeople = 430
            elif time_list[0] == 14:
                amountOfPeople = 500
            elif time_list[0] == 15:
                amountOfPeople = 528
            elif time_list[0] == 16:
                amountOfPeople = 487
            elif time_list[0] == 17:
                amountOfPeople = 371
            elif time_list[0] == 18:
                amountOfPeople = 529
            elif time_list[0] == 19:
                amountOfPeople = 674
            elif time_list[0] == 20:
                amountOfPeople = 599

        #Monday 7am - 9pm (9pm not included)
        elif time_list[1] == 0:
            if time_list[0] == 7:
                amountOfPeople = 75
            elif time_list[0] == 8:
                amountOfPeople = 115
            elif time_list[0] == 9:
                amountOfPeople = 253
            elif time_list[0] == 10:
                amountOfPeople = 485
            elif time_list[0] == 11:
                amountOfPeople = 536
            elif time_list[0] == 12:
                amountOfPeople = 699
            elif time_list[0] == 13:
                amountOfPeople = 750
            elif time_list[0] == 14:
                amountOfPeople = 732
            elif time_list[0] == 15:
                amountOfPeople = 668
            elif time_list[0] == 16:
                amountOfPeople = 501
            elif time_list[0] == 17:
                amountOfPeople = 491
            elif time_list[0] == 18:
                amountOfPeople = 687
            elif time_list[0] == 19:
                amountOfPeople = 959
            elif time_list[0] == 20:
                amountOfPeople = 888

        #Tuesday 7am - 9pm (9pm not included)
        elif time_list[1] == 1:
            if time_list[0] == 7:
                amountOfPeople = 69
            elif time_list[0] == 8:
                amountOfPeople = 120
            elif time_list[0] == 9:
                amountOfPeople = 243
            elif time_list[0] == 10:
                amountOfPeople = 388
            elif time_list[0] == 11:
                amountOfPeople = 505
            elif time_list[0] == 12:
                amountOfPeople = 676
            elif time_list[0] == 13:
                amountOfPeople = 799
            elif time_list[0] == 14:
                amountOfPeople = 750
            elif time_list[0] == 15:
                amountOfPeople = 502
            elif time_list[0] == 16:
                amountOfPeople = 466
            elif time_list[0] == 17:
                amountOfPeople = 473
            elif time_list[0] == 18:
                amountOfPeople = 681
            elif time_list[0] == 19:
                amountOfPeople = 800
            elif time_list[0] == 20:
                amountOfPeople = 522

        #Wednesday 7am - 9pm (9pm not included)
        elif time_list[1] == 2:
            if time_list[0] == 7:
                amountOfPeople = 68
            elif time_list[0] == 8:
                amountOfPeople = 134
            elif time_list[0] == 9:
                amountOfPeople = 225
            elif time_list[0] == 10:
                amountOfPeople = 396
            elif time_list[0] == 11:
                amountOfPeople = 528
            elif time_list[0] == 12:
                amountOfPeople = 798
            elif time_list[0] == 13:
                amountOfPeople = 841
            elif time_list[0] == 14:
                amountOfPeople = 784
            elif time_list[0] == 15:
                amountOfPeople = 555
            elif time_list[0] == 16:
                amountOfPeople = 416
            elif time_list[0] == 17:
                amountOfPeople = 447
            elif time_list[0] == 18:
                amountOfPeople = 623
            elif time_list[0] == 19:
                amountOfPeople = 759
            elif time_list[0] == 20:
                amountOfPeople = 645

        #Sunday 10am - 9pm
        if time_list[1] == 6:
            if time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Monday 7am - 9pm
        elif time_list[1] == 0:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Tuesday 7am - 9pm
        elif time_list[1] == 1:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Wednesday 7am - 9pm
        elif time_list[1] == 2:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Thursday 7am - 9pm
        elif time_list[1] == 3:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Friday 7am - 9pm
        elif time_list[1] == 4:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Saturday 10am - 9pm
        elif time_list[1] == 5:
            if time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

    elif nameOfDiner == "South":
        #Sunday 10am - 9pm
        if time_list[1] == 6:
            if time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Monday 7am - 9pm
        elif time_list[1] == 0:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Tuesday 7am - 9pm
        elif time_list[1] == 1:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Wednesday 7am - 9pm
        elif time_list[1] == 2:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Thursday 7am - 9pm
        elif time_list[1] == 3:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Friday 7am - 9pm
        elif time_list[1] == 4:
            if time_list[0] == 7:
                amountOfPeople = 10
            elif time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10

        #Saturday 10am - 9pm
        elif time_list[1] == 5:
            if time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
            elif time_list[0] == 21:
                amountOfPeople = 10
    
    elif nameOfDiner == "251North":
        #Sunday 8am - 7pm
        if time_list[1] == 6:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10

        #Monday 8am - 7pm
        elif time_list[1] == 0:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10

        #Tuesday 8am - 7pm
        elif time_list[1] == 1:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10

        #Wednesday 8am - 7pm
        elif time_list[1] == 2:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10

        #Thursday 8am - 7pm
        elif time_list[1] == 3:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10

        #Friday 8am - 7pm
        elif time_list[1] == 4:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10

        #Saturday 8am - 7pm
        elif time_list[1] == 5:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 10
            elif time_list[0] == 10:
                amountOfPeople = 10
            elif time_list[0] == 11:
                amountOfPeople = 10
            elif time_list[0] == 12:
                amountOfPeople = 10
            elif time_list[0] == 13:
                amountOfPeople = 10
            elif time_list[0] == 14:
                amountOfPeople = 10
            elif time_list[0] == 15:
                amountOfPeople = 10
            elif time_list[0] == 16:
                amountOfPeople = 10
            elif time_list[0] == 17:
                amountOfPeople = 10
            elif time_list[0] == 18:
                amountOfPeople = 10
            elif time_list[0] == 19:
                amountOfPeople = 10
            elif time_list[0] == 20:
                amountOfPeople = 10
    

    return str(int(float(amountOfPeople) / float(maximumCapacity) * 100))

def get_time_info():
    current_hour = now.strftime("%H")
    current_weekday = now.today().weekday()
    timeList = [current_hour, current_weekday]
    return timeList
