#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Nov 2019
# This is program cube surface area


def surface_area(side):
    # This'll calculate the surface area of a cube with side as a parameter

    # process
    area = (side * side) * 6
    return area


def main():
    # This is asks for the user input and runs surface_area()

    # Welcomes user
    print("Hi, this is CUBE SURFACE AREA CALCULATOR 3001")
    input("Press ENTER to continue.\n")

    while True:
        try:
            # input
            side = float(input("What is the side: "))
            # runs surface_area()
            area = surface_area(side)
            # output
            print("\nThe area is " + str(area) + " units squared.")
            break
        except ValueError:
            print("\nInvalid input.")
            print("Try again.\n")


if __name__ == "__main__":
    main()
