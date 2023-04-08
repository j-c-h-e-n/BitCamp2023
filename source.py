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
                amountOfPeople = 30
            elif time_list[0] == 9:
                amountOfPeople = 70
            elif time_list[0] == 10:
                amountOfPeople = 90
            elif time_list[0] == 11:
                amountOfPeople = 110
            elif time_list[0] == 12:
                amountOfPeople = 130
            elif time_list[0] == 13:
                amountOfPeople = 155
            elif time_list[0] == 14:
                amountOfPeople = 160
            elif time_list[0] == 15:
                amountOfPeople = 190
            elif time_list[0] == 16:
                amountOfPeople = 195
            elif time_list[0] == 17:
                amountOfPeople = 170
            elif time_list[0] == 18:
                amountOfPeople = 120
            elif time_list[0] == 19:
                amountOfPeople = 230
            elif time_list[0] == 20:
                amountOfPeople = 460

        #Monday 8am - 7pm
        elif time_list[1] == 0:
            if time_list[0] == 8:
                amountOfPeople = 100
            elif time_list[0] == 9:
                amountOfPeople = 185
            elif time_list[0] == 10:
                amountOfPeople = 210
            elif time_list[0] == 11:
                amountOfPeople = 240
            elif time_list[0] == 12:
                amountOfPeople = 360
            elif time_list[0] == 13:
                amountOfPeople = 380
            elif time_list[0] == 14:
                amountOfPeople = 355
            elif time_list[0] == 15:
                amountOfPeople = 295
            elif time_list[0] == 16:
                amountOfPeople = 250
            elif time_list[0] == 17:
                amountOfPeople = 355
            elif time_list[0] == 18:
                amountOfPeople = 460
            elif time_list[0] == 19:
                amountOfPeople = 400

        #Tuesday 8am - 7pm
        elif time_list[1] == 1:
            if time_list[0] == 8:
                amountOfPeople = 50
            elif time_list[0] == 9:
                amountOfPeople = 90
            elif time_list[0] == 10:
                amountOfPeople = 185
            elif time_list[0] == 11:
                amountOfPeople = 240
            elif time_list[0] == 12:
                amountOfPeople = 360
            elif time_list[0] == 13:
                amountOfPeople = 300
            elif time_list[0] == 14:
                amountOfPeople = 230
            elif time_list[0] == 15:
                amountOfPeople = 200
            elif time_list[0] == 16:
                amountOfPeople = 190
            elif time_list[0] == 17:
                amountOfPeople = 235
            elif time_list[0] == 18:
                amountOfPeople = 470
            elif time_list[0] == 19:
                amountOfPeople = 490

        #Wednesday 8am - 7pm
        elif time_list[1] == 2:
            if time_list[0] == 8:
                amountOfPeople = 100
            elif time_list[0] == 9:
                amountOfPeople = 180
            elif time_list[0] == 10:
                amountOfPeople = 200
            elif time_list[0] == 11:
                amountOfPeople = 240
            elif time_list[0] == 12:
                amountOfPeople = 280
            elif time_list[0] == 13:
                amountOfPeople = 300
            elif time_list[0] == 14:
                amountOfPeople = 290
            elif time_list[0] == 15:
                amountOfPeople = 260
            elif time_list[0] == 16:
                amountOfPeople = 210
            elif time_list[0] == 17:
                amountOfPeople = 205
            elif time_list[0] == 18:
                amountOfPeople = 400
            elif time_list[0] == 19:
                amountOfPeople = 480

        #Thursday 8am - 7pm
        elif time_list[1] == 3:
            if time_list[0] == 8:
                amountOfPeople = 100
            elif time_list[0] == 9:
                amountOfPeople = 195
            elif time_list[0] == 10:
                amountOfPeople = 280
            elif time_list[0] == 11:
                amountOfPeople = 370
            elif time_list[0] == 12:
                amountOfPeople = 390
            elif time_list[0] == 13:
                amountOfPeople = 385
            elif time_list[0] == 14:
                amountOfPeople = 300
            elif time_list[0] == 15:
                amountOfPeople = 210
            elif time_list[0] == 16:
                amountOfPeople = 200
            elif time_list[0] == 17:
                amountOfPeople = 300
            elif time_list[0] == 18:
                amountOfPeople = 400
            elif time_list[0] == 19:
                amountOfPeople = 390

        #Friday 8am - 7pm
        elif time_list[1] == 4:
            if time_list[0] == 8:
                amountOfPeople = 15
            elif time_list[0] == 9:
                amountOfPeople = 110
            elif time_list[0] == 10:
                amountOfPeople = 215
            elif time_list[0] == 11:
                amountOfPeople = 385
            elif time_list[0] == 12:
                amountOfPeople = 430
            elif time_list[0] == 13:
                amountOfPeople = 415
            elif time_list[0] == 14:
                amountOfPeople = 310
            elif time_list[0] == 15:
                amountOfPeople = 200
            elif time_list[0] == 16:
                amountOfPeople = 170
            elif time_list[0] == 17:
                amountOfPeople = 210
            elif time_list[0] == 18:
                amountOfPeople = 320
            elif time_list[0] == 19:
                amountOfPeople = 310

        #Saturday 8am - 7pm
        elif time_list[1] == 5:
            if time_list[0] == 8:
                amountOfPeople = 10
            elif time_list[0] == 9:
                amountOfPeople = 30
            elif time_list[0] == 10:
                amountOfPeople = 70
            elif time_list[0] == 11:
                amountOfPeople = 105
            elif time_list[0] == 12:
                amountOfPeople = 180
            elif time_list[0] == 13:
                amountOfPeople = 200
            elif time_list[0] == 14:
                amountOfPeople = 205
            elif time_list[0] == 15:
                amountOfPeople = 205
            elif time_list[0] == 16:
                amountOfPeople = 195
            elif time_list[0] == 17:
                amountOfPeople = 150
            elif time_list[0] == 18:
                amountOfPeople = 190
            elif time_list[0] == 19:
                amountOfPeople = 250
    

    return str(int(float(amountOfPeople) / float(maximumCapacity) * 100))

def get_time_info():
    current_hour = now.strftime("%H")
    current_weekday = now.today().weekday()
    timeList = [current_hour, current_weekday]
    return timeList
