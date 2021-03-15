def maximum(*bonus_values):       # Unpack parameter list
    maximum_value = 0
    for item in bonus_values:
        if maximum_value < item:
            maximum_value = item
    return maximum_value


bonus_value = maximum(1,22,3,2)
print('Bonus Maximum Value: ' + str(bonus_value))
