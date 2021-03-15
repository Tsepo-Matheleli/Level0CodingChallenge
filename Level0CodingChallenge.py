# Task 0.1
x = 0
y = 0
print(x)
print(y)

x = x + 3
y = y + x
print(x)
print(y)

# Task 0.2
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + (1 * 2)
a = 1 + 1 * 2 / 2
b = (1 + 1 * 2) / 2

print(str(x) + ', ' + str(y) + ', ' + str(z) + ', ' + str(a) + ', ' + str(b))


# Task 0.3
def hello(name):
    print('Hello ' + name + '!')


hello("Tsepo")


# Task 0.4
def even_or_odd(value):
    if value % 2 == 0:
        print('even')
    else:
        print('odd')


even_or_odd(5)
even_or_odd(10)


# Task 0.5
def area_of_triangle(side_one, side_two, side_three):
    semiperimeter = 0.5 * (side_one + side_two + side_three)
    return (semiperimeter * (semiperimeter - side_one) * (semiperimeter - side_two) * (semiperimeter - side_three)) // 2


area_one = area_of_triangle(5.0, 3.0, 4.0)

print('Triangle area: ' + str(area_one))


# Task 0.6
def maximum(first_value, second_value, third_value):
    if first_value > second_value and first_value > third_value:
        return first_value
    elif second_value > first_value and second_value > third_value:
        return second_value
    else:
        return third_value


max_value = maximum(3, 5, 25)
print('Maximum: ' + str(max_value))


# Must do bonus
def bonus_maximum(*bonus_values):       # Unpack parameter list
    maximum_value = 0
    for item in bonus_values:
        if maximum_value < item:
            maximum_value = item
    return maximum_value


bonus_value = bonus_maximum(2, 5, 4, 6, 14, 258, 5, 1000)
print('Bonus Maximum Value: ' + str(bonus_value))


# Task 0.7
def fahrenheit(celsius_value):
    return celsius_value * 1.8 + 32


def celsius(fahrenheit_value):
    return (fahrenheit_value - 32) / 1.8


print('Celsius: ' + str(celsius(37)))
print('Fahrenheit: ' + str(fahrenheit(54)))


# Task 0.8
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


# Task 0.9
def vowels(word):
    new_word_list = list(word)
    vowel_list = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')
    common_vowels = ''
    for character in new_word_list:
        if character in vowel_list:
            common_vowels += character + ', '
    print('Vowels: ' + common_vowels)


vowels('Umuzi')


# Task 0.10
def common_letters(first_word, second_word):
    first_word_list = list(first_word)
    second_word_list = list(second_word)
    common_words = ''
    for character in first_word_list:
        if character in second_word_list:
            common_words += character + ', '
    print('Common Letters: ' + common_words)


common_letters('house', 'mouse')
