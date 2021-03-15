import math


def area_of_triangle(side_one, side_two, side_three):
    semi_perimeter = (side_one + side_two + side_three)/2
    print(semi_perimeter)
    return math.sqrt(semi_perimeter * (semi_perimeter - side_one) * (semi_perimeter - side_two) * (semi_perimeter - side_three))


area_one = area_of_triangle(5.0, 3.0, 4.0)

print('Triangle area: ' + str(area_one))
