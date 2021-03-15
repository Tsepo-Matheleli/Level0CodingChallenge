def convert_to_fahrenheit(celsius_value):
    return celsius_value * 1.8 + 32


def convert_to_celsius(fahrenheit_value):
    return (fahrenheit_value - 32) / 1.8


print('Celsius: ' + str(convert_to_celsius(37)))
print('Fahrenheit: ' + str(convert_to_fahrenheit(54)))
