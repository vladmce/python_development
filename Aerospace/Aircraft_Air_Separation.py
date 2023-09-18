"""
AIRBORNE COLLISION PROBABILITY CALCULATOR FOR TWO AIRCRAFT
- Due to ICAO standards and EASA regulation, the vertical minimum separation (100 FT VERT / 5 NM HOR)
- Provided the 3 - coordinates positions of each aircraft
"""

import math
import numpy as np
import simple_colors

# Constant: Earth radius [in nautical miles]
R = 3440

# Variables: Vertical and horizontal distances of separations required by the competent authority [in feet and nautical miles]
def numeric_input(text_value: str) -> float:
    while True:
        number = input(text_value)
        try:
            number = float(number)
            break
        except ValueError:
            print("Invalid format.")
    return number

def numeric_input_with_boundaries(text_value: str, left_bound: int, right_bound: int) -> float:
    while True:
        number = input(text_value)
        try:
            number = float(number)
            if number >= left_bound and number <= right_bound:
                break
            else:
                print("Invalid format.")
        except ValueError:
            print("Invalid format.")
    return number

vsep = numeric_input("Input the vertical separation (in feet): ")
hsep = numeric_input("Input the horizontal separation (in nautical miles): ")


# Variable: Possible error range [in feet]
err = numeric_input("Input the error range margin (in feet): ")

# Variables: Data for airplane 1: altitude [in feet], latitude [in decimal degrees], longitude [in decimal degrees]
print("\nThe following data targets Airplane 1: ")
lat_j = numeric_input_with_boundaries("Provide the latitude of the first airplane (in decimal degrees): ", -90, 90)
long_j = numeric_input_with_boundaries("Provide the longitude of the first airplane (in decimal degrees): ", -180, 180)
alt_j = numeric_input_with_boundaries("Provide the altitude of the first airplane (in feet): ", 0, 10 ** 4)

# Variables: Data for airplane 2: altitude [in feet], latitude [in decimal degrees], longitude [in decimal degrees]
print("\nThe following data targets Airplane 2: ")
lat_k = numeric_input_with_boundaries("Provide the latitude of the first airplane (in decimal degrees): ", -90, 90)
long_k = numeric_input_with_boundaries("Provide the longitude of the first airplane (in decimal degrees): ", -180, 180)
alt_k = numeric_input_with_boundaries("Provide the altitude of the first airplane (in feet): ", 0, 10 ** 4)

# The parameters calculation
a = (math.pi * R) / 100
b = (lat_j - lat_k) ** 2
c = (long_j - long_k) ** 2
d = math.cos((lat_j + lat_k)/2) ** 2

# Calculating the vertical separation:
ver_jk = abs(alt_j - alt_k)

# Calculating the horizontal separation:
hor_jk = a * math.sqrt(b + c * d)

# Conditions for separation loss probability calculation
if ver_jk < vsep:
    if hor_jk < hsep:
        p = (1 - np.sign(ver_jk - vsep + 2 * c)) / (2 * (np.exp(1)) ** hor_jk) * 100
        if p % 10 == 0:
            p = int(p)
        else:
            p = p
        if p >= 60:
            print(simple_colors.red(f"\nThe probability for the two airctaft to collide is {p} %."))
        elif p >= 30 and p < 60:
            print(simple_colors.yellow(f"\nThe probability for the two airctaft to collide is {p} %."))
        elif p > 0 and p < 30:
            print(simple_colors.blue(f"\nThe probability for the two airctaft to collide is {p} %."))

if ver_jk >= vsep or hor_jk >= hsep:
    print(simple_colors.green(f"\n The probability for the two airctaft to collide is 0 %."))

