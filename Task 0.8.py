def time(number):
    if number >= 60:
        hour = number // 60
        if number % 60 > 0:
            minute = number % 60
            if hour > 1 and minute > 1:
                print(str(hour) + ' hours, ' + str(minute) + " minutes")

            elif hour == 1 and minute > 1:
                print(str(hour) + ' hour, ' + str(minute) + " minutes")
            elif hour == 1 and minute == 1:
                print(str(hour) + ' hour, ' + str(minute) + " minute")
            else:
                print(str(hour) + ' hours, ' + str(minute) + " minute")
        else:
            if hour == 1:
                print(str(hour) + ' hour')
            else:
                print(str(hour) + ' hours')
    else:
        if number == 1:
            print(str(number) + ' minute')
        else:
            print(str(number) + ' minutes')


time(75)
time(105)
time(59)
time(250)