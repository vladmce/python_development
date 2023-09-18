"""
LONGITUDINAL and LATERAL distance calculator
This software calculates the lateral and longitudinal distance between:
    - an obstacle of known coordinates
    - the centerline of a runway given:
        - the magnetic orientation
        - the length
        - coordinates for one of the thresholds
"""

import math
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

print("The following data targets the area:")
magnetic_runway_angle = numeric_input_with_boundaries("Provide the magnetic orientation of the runway (Westernmost Threshold): ", 0, 180)
var = numeric_input_with_boundaries("Provide the magnetic declination of the area (decimal degrees +N/E -S/W): ", -25, 25)

print("\nThe following data targets the EASTERN threshold of the runway:")
x_e = numeric_input_with_boundaries("Provide the latitude coordinates (decimal degrees): ", 0, 90)
y_e = numeric_input_with_boundaries("Provide the longitude coordinates (decimal degrees): ", 0, 180)
h_e = numeric_input_with_boundaries("Provide the elevation (feet): ", 0, 40000)

print("\nThe following data targets the WESTERN threshold of the runway:")
x_w = numeric_input_with_boundaries("Provide the latitude coordinates (decimal degrees): ", 0, 90)
y_w = numeric_input_with_boundaries("Provide the longitude coordinates (decimal degrees): ", 0, 180)
h_w = numeric_input_with_boundaries("Provide the elevation (feet): ", 0, 40000)

i = 0
while True:
    i += 1
    print(f"\nThe following data targets the Obstacle number {i}:")
    x_o = numeric_input_with_boundaries("Provide the latitude coordinates (decimal degrees): ", 0, 90)
    y_o = numeric_input_with_boundaries("Provide the longitude coordinates (decimal degrees): ", 0, 180)
    h_o = numeric_input_with_boundaries("Provide the height (feet): ", 0, 40000)

    # Calculations
    true_runway_angle = magnetic_runway_angle + var
    alpha = abs(90 - true_runway_angle)
    slope = math.tan(math.radians(alpha))

    ae = slope
    be = -1
    ce = y_e - slope * x_e

    aw = slope
    bw = -1
    cw = y_w - slope * x_w

    lateral_distance = abs((ae * x_o + be * y_o + ce) / math.sqrt(ae ** 2 + be ** 2) * 60)
    total_distance_east = math.sqrt((x_o - x_e) ** 2 + (y_o - y_e) ** 2) * 60
    total_distance_west = math.sqrt((x_o - x_w) ** 2 + (y_o - y_w) ** 2) * 60
    longitudinal_distance_east = math.sqrt(total_distance_east ** 2 - lateral_distance ** 2)
    longitudinal_distance_west = math.sqrt(total_distance_west ** 2 - lateral_distance ** 2)
    elevation_difference_east = h_o - h_e
    elevation_difference_west = h_o - h_w

    print(f"\nResults for the Eastern Threshold ({(magnetic_runway_angle+180):.0f} degrees)")
    print(f"The total distance: {total_distance_east:.2f} NM")
    print(f"The lateral distance: {lateral_distance:.2f} NM")
    print(f"The longitudinal distance: {longitudinal_distance_east:.2f} NM")
    print(f"The elevation difference: {elevation_difference_east:.2f} feet")

    print(f"\nResults for the Western Threshold ({magnetic_runway_angle:.0f} degrees)")
    print(f"The total distance: {total_distance_west:.2f} NM")
    print(f"The lateral distance: {lateral_distance:.2f} NM")
    print(f"The longitudinal distance: {longitudinal_distance_west:.2f} NM")
    print(f"The elevation difference: {elevation_difference_west:.2f} feet")






