#!/usr/bin/env python3
# Created By: Enoch Amedjrovi
# 24 february 24 2025
# This program displays area and volume of a hexagonal pyramid


def main():
    print("Hello, i will calculator the volume and area of a hexagonal pyramid")
    print("Would you like me to calculate the volume and area of a hexagonal pyramid")


import math

edge = float(input("what is the edge? "))
height = float(input("what is the height? "))

volume = ((math.sqrt(3)) / 2) * ((edge**2) * height)

area = ((((3 * (math.sqrt(3)))) / (2)) * (edge**2)) + (3 * edge) * (
    math.sqrt((height**2) + ((3 * (edge**2)) / 4))
)

print("{:.2f}".format(area))
print("{:.2f}".format(volume))
