import math


def circle_calc(radius):
    diameter = int(radius * 2)
    area = int(math.pi * (radius**2))
    circumference = int(math.pi * diameter)
    return area, diameter, circumference


if __name__ == "__main__":
    r = float(input("Enter the radius of a circle: "))
    a, d, c = circle_calc(r)
    print(
        f"The circle has an area of {a} with a diameter of {d} and a circumference of {c}."
    )
