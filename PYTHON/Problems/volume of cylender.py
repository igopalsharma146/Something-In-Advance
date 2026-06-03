# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs. 
import math

def volume_of_cylinder(radius, height):
    return math.pi * radius**2 * height

def cost_of_milk(volume_liters, cost_per_liter):
    return volume_liters * cost_per_liter

# Example usage
radius = 5
height = 10
cost_per_liter = 40

volume = volume_of_cylinder(radius, height)
cost = cost_of_milk(volume, cost_per_liter)

print(f"Volume of the cylinder: {volume:.2f} liters")
print(f"Cost of milk: Rs. {cost:.2f}")