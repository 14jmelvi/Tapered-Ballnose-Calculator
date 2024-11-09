import math
import decimal
import time
from time import sleep
from decimal import Decimal, ROUND_UP, getcontext
from math import sqrt, tan, cos, sin, degrees, radians

def safe_decimal_input(prompt):
    while True:
        try:
            return Decimal(input(prompt))
        except decimal.InvalidOperation:
            print("Invalid input. Please enter a number.")

def calculate_od():
    # Assign values
    radius = safe_decimal_input("Input the radius of the ball in inches: " ) # the radius will be sides a and b for our triangle
    side_a = radius
    side_b = radius

    # Calculate hypotenuse
    side_c = sqrt(side_a ** 2 + side_b ** 2)

    # Assign angles of triangle
    angle_a = Decimal(45)
    angle_b = Decimal(45)
    angle_c = Decimal(90)

    # Ask user for taper angle
    taper_angle = safe_decimal_input("Input taper angle: ")

    # Adjust angles of triangle for side b (LOC of the tangency point of ball taper)
    angle_a2 = angle_a - taper_angle 
    angle_b2 = angle_b  
    angle_c2 = angle_c + taper_angle 

    # Convert angles to radians for trigonometric functions
    angle_a2_rad = radians(angle_a2)
    angle_c2_rad = radians(angle_c2)

    # Calculate length of side a (LOC of the tangency point of ball taper) using Law of sines
    tangency_loc = side_c * sin(angle_a2_rad) / sin(angle_c2_rad)

    # Calculate tangency height (half od) of new triangle using tangency_loc and taper angle
    half_angle = taper_angle / 2
    angle_a3 = angle_a + half_angle
    angle_b3 = angle_b - half_angle
    angle_c3 = angle_c

    # Convert angles to radians for trigonometric functions
    angle_a3_rad = radians(angle_a3)
    angle_b3_rad = radians(angle_b3)
    angle_c3_rad = radians(angle_c3)

    tangency_height = tangency_loc * sin(angle_a3_rad) / sin(angle_b3_rad)

    # Round up to 5 decimal places
    tangency_height_rounded = Decimal(math.ceil(tangency_height * 100000) / 100000)

    # Double tangency height to get OD size at the tangency point
    tangency_size_od = tangency_height_rounded * Decimal(2)

    # Calculate OD at various points (LOC) of a taper
    loc_front = safe_decimal_input("Input LOC at front of the tool in inches: ")
    loc_back = safe_decimal_input("Input LOC at back of the tool in inches: ")

    # Convert tan(taper_angle) result to Decimal
    taper_angle_rad = radians(float(taper_angle))  # Convert taper_angle to float, then to radians
    tan_taper_angle = Decimal(math.tan(taper_angle_rad))  # Calculate the tangent and convert to Decimal

    # Calculate OD front and back, keeping all values as Decimal
    loc_tangent = Decimal(tangency_loc)
    od_front = tan_taper_angle * Decimal(2) * (loc_front - loc_tangent) + tangency_size_od
    od_back = tan_taper_angle * Decimal(2) * (loc_back - loc_tangent) + tangency_size_od

    # Format and print results
    def format_decimal(value, places=4):
        return str(Decimal(value).quantize(Decimal(f'0.{"0"*places}'), rounding=ROUND_UP))

    print(f"The OD at {loc_front} is: {format_decimal(od_front, 5)}")
    print(f"The OD at {loc_back} is: {format_decimal(od_back, 5)}")

# Main loop to allow rerun
while True:
    calculate_od()
    repeat = input("Press any key to start new calculation or 'n' to quit: ")
    if repeat.lower() == 'n':
        print("Goodbye!")
        break

sleep(2)
