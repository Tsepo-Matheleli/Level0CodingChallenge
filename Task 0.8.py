def time(number):
    hour = number // 60
    minute = number % 60
    if hour > 1 and minute >= 0:
        print(str(hour) + ' hours, ' + str(minute) + " minutes")

    elif hour == 1 and minute >= 0:
        print(str(hour) + ' hour, ' + str(minute) + " minutes")
    elif hour == 1 and minute == 1:
        print(str(hour) + ' hour, ' + str(minute) + " minute")
    elif hour == 1 and minute == 1:
        print(str(hour) + ' hours, ' + str(minute) + " minute")
    else:
        if number == 1:
            print(str(number) + ' minute')
        else:
            print(str(number) + ' minutes')


time(75)
time(105)
time(120)
time(50)
time(250)
