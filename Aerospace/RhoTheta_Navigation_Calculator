"""
VOR Positioning System <---> RHO - THETA NAVIGATION CALCULATOR
A VOR-DME is a land-target for the radar of the airplane. The airplane computer calculates the position of the aircraft knowing:
    - the position of the VOR (Lat, Long, Elevation)
    - the flight level (altitude) of the airplane
    - the angular deviation between the airplane and the VOR <-> deviates in THETA
    - the distance between the airplane and the VOR <-> deviates in RHO
In this scenario, we need only one VOR in order to calculate the position of the aircraft.
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


# Constant: Earth radius [in nautical miles]
r_earth = 3440

# Input Variables: Data regarding the VOR-DME
print("\nThe following data concern the VOR-DME system: ")
lat_vor = numeric_input_with_boundaries("Provide the latitude of the VOR (in decimal degrees): ", -90, 90)
long_vor = numeric_input_with_boundaries("Provide the longitude of the VOR (in decimal degrees): ", -180, 180)
elev_vor = numeric_input_with_boundaries("Provide the elevation of the VOR (in feet): ", 0, 9000)

# Input Variables: Data Angles and Distances
print("\nThe following data concern the relation between the VOR-DME system and the airplane: ")
qdr = numeric_input_with_boundaries("Provide QDR (the airplane alignment with the VOR) (in decimal degrees): ", 0, 360)
rho_dme = numeric_input("Provide RHO-DME (the distance between the airplane and the VOR) (in nautical miles): ")

print("\nThe following data concern the airplane: ")
flight_level = numeric_input_with_boundaries("Provide the flight level of the airplane (in hundreds of feet): ", 0, 700) * 100

print("\nThe following data concern the area of interest: ")
var = numeric_input_with_boundaries("Provide the magnetic declination of the area (decimal degrees +N/E -S/W): ", -25, 25)

# Calculations
R = r_earth + flight_level * (0.2048/1852)
qte = qdr + var
theta = 90 - qte

if theta >= 0:
    theta = theta
else:
    theta = theta + 360

rho = math.sqrt(rho_dme ** 2 - ((flight_level-elev_vor) * 0.3048/1852) ** 2)
airplane_latitude = lat_vor + (rho * math.sin(math.radians(theta))/R) * (180 / math.pi)
average_latitude = (lat_vor + airplane_latitude) / 2
airplane_longitude = long_vor + (1 / math.cos(math.radians(average_latitude))) * (rho * math.cos(math.radians(theta))/R) * (180 / math.pi)

vor_data = f"\nVOR Data: \nVOR Latitude: {lat_vor:.4f} deg \nVOR Longitude: {long_vor:.4f} deg \nVOR Elevation {elev_vor:.0f} feet"
airplane_data = f"\nAirplane Data: \nAirplane Latitude: {airplane_latitude:.4f} deg \nAirplane Longitude: {airplane_longitude:.4f} deg \nAirplane Altitude {flight_level:.0f} feet"

print(vor_data)
print(airplane_data)
