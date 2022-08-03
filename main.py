# Author: Fransiskus Agapa

# =======================
# simple program of inputting information of car and motorcycle
# the idea is to practice sending object as an argument in function
# =======================

from vehicle import Vehicle
from design import brand
from design import color
from design import country_origin


print("\n== Vehicle Database ==")
print("1. Car")
print("2. Motorcycle")
print("e. Exit")
choice = input("choice: ").lower()  # make user input to lower case to make while-loop condition easier

while choice != 'e':
    if choice == '1':
        print("\nBuilding Car ... Car built\n")
        the_brand = input("Name of the brand: ").upper()                                                          # wording format
        car = Vehicle()
        if the_brand.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            the_color = input("Input color: ").capitalize()                                                       # wording format
            if the_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                the_place = input("Name of the country, where the vehicle was originally from: ").capitalize()    # wording format
                if the_place.isdigit():
                    print("\n[ Invalid input - string only ]")
                else:
                    brand(car, the_brand)
                    color(car, the_color)
                    country_origin(car, the_place)
                    print("\nThe brand of the car is " + str(car.brand))
                    print("The color of the car is " + str(car.color))
                    print("The car was originally from " + str(car.origin_country))

    elif choice == '2':
        print("\nBuilding Motorcycle ... Motorcycle built\n")
        motorcycle = Vehicle()
        the_brand = input("Name of the brand: ").upper()
        if the_brand.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            the_color = input("Input color: ").capitalize()
            if the_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                the_place = input("Name of the country, where the vehicle was originally from:  ").capitalize()
                if the_place.isdigit():
                    print("\n[ Invalid input - string only ]")
                else:
                    brand(motorcycle, the_brand)
                    color(motorcycle, the_color)
                    country_origin(motorcycle, the_place)
                    print("\nThe brand of the motorcycle is " + str(motorcycle.brand))
                    print("The color fo the motorcycle is " + str(motorcycle.color))
                    print("The motorcycle was originally from " + str(motorcycle.origin_country))

    else:
        print("\n[ Invalid choice ]")

    print("\n== Vehicle Database ==")
    print("1. Car")
    print("2. Motorcycle")
    print("e. Exit")
    choice = input("choice: ").lower()  # make user input to lower case to make while-loop condition easier

print("\n== Exit Program ==")
