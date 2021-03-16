def maximum(*bonus_values):
    maximum_value = 0
    for item in bonus_values:
        if maximum_value < item and item >= 0:
            maximum_value = item
        else:
            maximum_value = item
            for negative_value in bonus_values:
                if maximum_value < negative_value:
                    maximum_value = negative_value
    return maximum_value


bonus_value = maximum(1, 22, 3, 2)
bonus_negative_value = maximum(-1000, -1, -10, -100)
print('Bonus Maximum Value: ' + str(bonus_value))
print('Bonus Maximum Negative Value: ' + str(bonus_negative_value))
