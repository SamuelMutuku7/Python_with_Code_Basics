india = ["Mumbai", "Banglore", "Chennai", "Delhi"]
pakistan = ["Lahore", "Karachi", "Islamabad"]
bangladesh = ["Dhaka", "Khulna", "Rangpur"]

city = input("Enter city name: ")

if city in india:
    print(city, "is in India")
elif city in pakistan:
    print(city, "is in Pakistan")
elif city in bangladesh:
    print(city, "is in Bangladesh")
else:
    print(city, "is not in India, Pakistan or Bangladesh")

# The above code is a solution to the exercise. It is a simple if-elif-else statement.

city_1 = input("Enter city 1: ")
city_2 = input("Enter city 2: ")

if city_1 in india and city_2 in india:
    print("Both cities are in India.")
elif city_1 in pakistan and city_2 in pakistan:
    print("Both cities are in Pakistan.")
elif city_1 in bangladesh and city_2 in bangladesh:
    print("Both cities are in Bangladesh.")
else:
    print("They don't belong to the same country.")

# The above code is a solution to the exercise. It is a simple if-elif-else statement.

sugar_level = int(input("Enter sugar level: "))

if sugar_level < 80:
    print("Your sugar level is low.")
elif sugar_level > 100:
    print("Your sugar level is high.")
else:
    print("Your sugar level is normal.")
