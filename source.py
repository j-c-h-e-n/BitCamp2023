from datetime import datetime

now = datetime.now()

def get_busyness_percentage(nameOfDiner, maximumCapacity):
    time_list = get_time_info()
    amountOfPeople = 0
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

        #Thursday 7am - 9pm
        elif time_list[1] == 3:
            if time_list[0] == 7:
                amountOfPeople = 62
            elif time_list[0] == 8:
                amountOfPeople = 104
            elif time_list[0] == 9:
                amountOfPeople = 246
            elif time_list[0] == 10:
                amountOfPeople = 469
            elif time_list[0] == 11:
                amountOfPeople = 534
            elif time_list[0] == 12:
                amountOfPeople = 685
            elif time_list[0] == 13:
                amountOfPeople = 724
            elif time_list[0] == 14:
                amountOfPeople = 711
            elif time_list[0] == 15:
                amountOfPeople = 624
            elif time_list[0] == 16:
                amountOfPeople = 489
            elif time_list[0] == 17:
                amountOfPeople = 534
            elif time_list[0] == 18:
                amountOfPeople = 743
            elif time_list[0] == 19:
                amountOfPeople = 867
            elif time_list[0] == 20:
                amountOfPeople = 586

        #Friday 7am - 9pm
        elif time_list[1] == 4:
            if time_list[0] == 7:
                amountOfPeople = 65
            elif time_list[0] == 8:
                amountOfPeople = 168
            elif time_list[0] == 9:
                amountOfPeople = 279
            elif time_list[0] == 10:
                amountOfPeople = 346
            elif time_list[0] == 11:
                amountOfPeople = 579
            elif time_list[0] == 12:
                amountOfPeople = 713
            elif time_list[0] == 13:
                amountOfPeople = 865
            elif time_list[0] == 14:
                amountOfPeople = 679
            elif time_list[0] == 15:
                amountOfPeople = 495
            elif time_list[0] == 16:
                amountOfPeople = 345
            elif time_list[0] == 17:
                amountOfPeople = 357
            elif time_list[0] == 18:
                amountOfPeople = 516
            elif time_list[0] == 19:
                amountOfPeople = 621
            elif time_list[0] == 20:
                amountOfPeople = 547

        #Saturday 10am - 9pm
        elif time_list[1] == 5:
            if time_list[0] == 10:
                amountOfPeople = 103
            elif time_list[0] == 11:
                amountOfPeople = 214
            elif time_list[0] == 12:
                amountOfPeople = 299
            elif time_list[0] == 13:
                amountOfPeople = 316
            elif time_list[0] == 14:
                amountOfPeople = 954
            elif time_list[0] == 15:
                amountOfPeople = 479
            elif time_list[0] == 16:
                amountOfPeople = 401
            elif time_list[0] == 17:
                amountOfPeople = 368
            elif time_list[0] == 18:
                amountOfPeople = 471
            elif time_list[0] == 19:
                amountOfPeople = 542
            elif time_list[0] == 20:
                amountOfPeople = 468

    elif nameOfDiner == "South":
        #Sunday 10am - 9pm
        if time_list[1] == 6:
            if time_list[0] == 10:
                amountOfPeople = 76
            elif time_list[0] == 11:
                amountOfPeople = 153
            elif time_list[0] == 12:
                amountOfPeople = 245
            elif time_list[0] == 13:
                amountOfPeople = 268
            elif time_list[0] == 14:
                amountOfPeople = 271
            elif time_list[0] == 15:
                amountOfPeople = 354
            elif time_list[0] == 16:
                amountOfPeople = 286
            elif time_list[0] == 17:
                amountOfPeople = 405
            elif time_list[0] == 18:
                amountOfPeople = 498
            elif time_list[0] == 19:
                amountOfPeople = 531
            elif time_list[0] == 20:
                amountOfPeople = 364

        #Monday 7am - 9pm
        elif time_list[1] == 0:
            if time_list[0] == 7:
                amountOfPeople = 62
            elif time_list[0] == 8:
                amountOfPeople = 267
            elif time_list[0] == 9:
                amountOfPeople = 421
            elif time_list[0] == 10:
                amountOfPeople = 678
            elif time_list[0] == 11:
                amountOfPeople = 854
            elif time_list[0] == 12:
                amountOfPeople = 976
            elif time_list[0] == 13:
                amountOfPeople = 863
            elif time_list[0] == 14:
                amountOfPeople = 714
            elif time_list[0] == 15:
                amountOfPeople = 542
            elif time_list[0] == 16:
                amountOfPeople = 341
            elif time_list[0] == 17:
                amountOfPeople = 356
            elif time_list[0] == 18:
                amountOfPeople = 378
            elif time_list[0] == 19:
                amountOfPeople = 415
            elif time_list[0] == 20:
                amountOfPeople = 374

        #Tuesday 7am - 9pm
        elif time_list[1] == 1:
            if time_list[0] == 7:
                amountOfPeople = 75
            elif time_list[0] == 8:
                amountOfPeople = 142
            elif time_list[0] == 9:
                amountOfPeople = 335
            elif time_list[0] == 10:
                amountOfPeople = 612
            elif time_list[0] == 11:
                amountOfPeople = 756
            elif time_list[0] == 12:
                amountOfPeople = 916
            elif time_list[0] == 13:
                amountOfPeople = 872
            elif time_list[0] == 14:
                amountOfPeople = 634
            elif time_list[0] == 15:
                amountOfPeople = 514
            elif time_list[0] == 16:
                amountOfPeople = 427
            elif time_list[0] == 17:
                amountOfPeople = 465
            elif time_list[0] == 18:
                amountOfPeople = 578
            elif time_list[0] == 19:
                amountOfPeople = 413
            elif time_list[0] == 20:
                amountOfPeople = 398

        #Wednesday 7am - 9pm
        elif time_list[1] == 2:
            if time_list[0] == 7:
                amountOfPeople = 76
            elif time_list[0] == 8:
                amountOfPeople = 184
            elif time_list[0] == 9:
                amountOfPeople = 364
            elif time_list[0] == 10:
                amountOfPeople = 578
            elif time_list[0] == 11:
                amountOfPeople = 769
            elif time_list[0] == 12:
                amountOfPeople = 800
            elif time_list[0] == 13:
                amountOfPeople = 789
            elif time_list[0] == 14:
                amountOfPeople = 654
            elif time_list[0] == 15:
                amountOfPeople = 521
            elif time_list[0] == 16:
                amountOfPeople = 341
            elif time_list[0] == 17:
                amountOfPeople = 358
            elif time_list[0] == 18:
                amountOfPeople = 579
            elif time_list[0] == 19:
                amountOfPeople = 628
            elif time_list[0] == 20:
                amountOfPeople = 514

        #Thursday 7am - 9pm
        elif time_list[1] == 3:
            if time_list[0] == 7:
                amountOfPeople = 71
            elif time_list[0] == 8:
                amountOfPeople = 164
            elif time_list[0] == 9:
                amountOfPeople = 378
            elif time_list[0] == 10:
                amountOfPeople = 534
            elif time_list[0] == 11:
                amountOfPeople = 679
            elif time_list[0] == 12:
                amountOfPeople = 713
            elif time_list[0] == 13:
                amountOfPeople = 742
            elif time_list[0] == 14:
                amountOfPeople = 679
            elif time_list[0] == 15:
                amountOfPeople = 641
            elif time_list[0] == 16:
                amountOfPeople = 453
            elif time_list[0] == 17:
                amountOfPeople = 574
            elif time_list[0] == 18:
                amountOfPeople = 678
            elif time_list[0] == 19:
                amountOfPeople = 561
            elif time_list[0] == 20:
                amountOfPeople = 479

        #Friday 7am - 9pm
        elif time_list[1] == 4:
            if time_list[0] == 7:
                amountOfPeople = 63
            elif time_list[0] == 8:
                amountOfPeople = 211
            elif time_list[0] == 9:
                amountOfPeople = 364
            elif time_list[0] == 10:
                amountOfPeople = 699
            elif time_list[0] == 11:
                amountOfPeople = 875
            elif time_list[0] == 12:
                amountOfPeople = 968
            elif time_list[0] == 13:
                amountOfPeople = 852
            elif time_list[0] == 14:
                amountOfPeople = 587
            elif time_list[0] == 15:
                amountOfPeople = 349
            elif time_list[0] == 16:
                amountOfPeople = 234
            elif time_list[0] == 17:
                amountOfPeople = 340
            elif time_list[0] == 18:
                amountOfPeople = 561
            elif time_list[0] == 19:
                amountOfPeople = 574
            elif time_list[0] == 20:
                amountOfPeople = 490

        #Saturday 10am - 9pm
        elif time_list[1] == 5:
            if time_list[0] == 10:
                amountOfPeople = 84
            elif time_list[0] == 11:
                amountOfPeople = 131
            elif time_list[0] == 12:
                amountOfPeople = 210
            elif time_list[0] == 13:
                amountOfPeople = 132
            elif time_list[0] == 14:
                amountOfPeople = 96
            elif time_list[0] == 15:
                amountOfPeople = 345
            elif time_list[0] == 16:
                amountOfPeople = 81
            elif time_list[0] == 17:
                amountOfPeople = 237
            elif time_list[0] == 18:
                amountOfPeople = 349
            elif time_list[0] == 19:
                amountOfPeople = 445
            elif time_list[0] == 20:
                amountOfPeople = 399

    
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
    timeList = [int(current_hour), current_weekday]
    return timeList
