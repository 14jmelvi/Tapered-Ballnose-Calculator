import math
from decimal import Decimal, ROUND_UP

def calculate_hypotenuse(radius):
    return Decimal(radius) * Decimal(math.sqrt(2))

def adjust_angles(user_angle):
    angle_a = Decimal(45)  # Angle A remains unchanged
    angle_c = Decimal(90) + Decimal(user_angle)  # Adjusted right angle C
    angle_b = angle_a - Decimal(user_angle)  # Adjusted angle B

    return angle_a, angle_b, angle_c

def calculate_length_b(hypotenuse, angle_b):
    angle_b_rad = Decimal(math.radians(angle_b))
    length_b = hypotenuse * Decimal(math.sin(angle_b_rad))
    return length_b

def format_decimal(value, places=4):
    return str(Decimal(value).quantize(Decimal(f'0.{"0"*places}'), rounding=ROUND_UP))

def calculate_outer_diameter(radius, user_angle, adjusted_loc):
    angle_rad = Decimal(math.radians(user_angle))
    # New formula for outer diameter calculation
    back_od = (Decimal(math.tan(angle_rad)) * 2 * adjusted_loc) + (Decimal(radius) * 2)
    return back_od

def calculate_side_a(side_b, angle_a, angle_b):
    angle_a_rad = Decimal(math.radians(angle_a))
    angle_b_rad = Decimal(math.radians(angle_b))
    side_a = side_b * (Decimal(math.sin(angle_a_rad)) / Decimal(math.sin(angle_b_rad)))
    return side_a

def calculate_side_c(side_b, angle_c, angle_b):
    angle_c_rad = Decimal(math.radians(angle_c))
    angle_b_rad = Decimal(math.radians(angle_b))
    side_c = side_b * (Decimal(math.sin(angle_c_rad)) / Decimal(math.sin(angle_b_rad)))
    return side_c

def calculate_od_at_tangency(radius, side_b):
    # The OD at the tangency point is measured from side_b and involves the radius.
    od_tangency = Decimal(radius) + side_b
    return od_tangency

def calculate_final_value(radius, od_tangency, radius_minus_side_b):
    return (Decimal(radius) * 2) - (od_tangency + radius_minus_side_b)

def main():
    radius = float(input("Enter the radius of the ball (in inches): "))
    
    hypotenuse = calculate_hypotenuse(radius)
    #print(f"The hypotenuse of the triangle with equal sides of length {radius:.5f} inches is: {format_decimal(hypotenuse, 6)} inches")

    user_angle = float(input("Enter the taper angle (in degrees): "))
    
    angle_a, angle_b, angle_c = adjust_angles(user_angle)

    if angle_a is not None:
        side_b = calculate_length_b(hypotenuse, angle_b)

        loc1 = float(input("Enter where you want to measure the first length of cut (in inches): "))
        loc2 = float(input("Enter where you want to measure the second length of cut (in inches): "))

        # Adjust LOC values by subtracting side_b
        adjusted_loc1 = Decimal(loc1) - side_b
        adjusted_loc2 = Decimal(loc2) - side_b

        # Calculate the outer diameters using the adjusted LOCs
        back_od1 = calculate_outer_diameter(radius, user_angle, adjusted_loc1)
        back_od2 = calculate_outer_diameter(radius, user_angle, adjusted_loc2)

        # New output for radius - side_b
        radius_minus_side_b = Decimal(radius) - side_b

        # Calculate OD at tangency point
        od_tangency = calculate_od_at_tangency(radius, side_b)

        # Adjusted decimal value for rounding output
        adjusteddecimal = (radius_minus_side_b) / 10

        # Output results with rounded up values
        print(f"The OD at {loc1} is: {format_decimal(back_od1 - adjusteddecimal, 5)} inches.")
        print(f"The OD at {loc2} is: {format_decimal(back_od2 - adjusteddecimal, 5)} inches.")

if __name__ == "__main__":
    main()
