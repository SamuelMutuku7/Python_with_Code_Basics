country_population = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}


def print_all():
    for country, population in country_population.items():
        print(f"{country}==>{population}")


def add():
    country = input("Enter the country name to add: ")
    country = country.lower()
    if country in country_population:
        print("The country already exists in our dataset. Terminating...")
        return
    else:
        population = int(input(f"Enter the population for {country}: "))
        country_population[country] = population
        print_all()


def remove():
    country = input("Enter the country name to remove: ")
    country = country.lower()
    if country not in country_population:
        print("The country doesn't exist in our dataset. Terminating...")
        return
    else:
        del country_population[country]
        print_all()


def query():
    country = input("Enter the country name to query: ")
    country = country.lower()
    if country not in country_population:
        print("The country doesn't exist in our dataset. Terminating...")
        return
    else:
        print(f"The population of {country} is: {country_population[country]} crores.")


def main():
    operation = input("Enter the operation (add, remove, query, or print): ")
    if operation.lower() == "add":
        add()
    elif operation.lower() == "remove":
        remove()
    elif operation.lower() == "query":
        query()
    elif operation.lower() == "print":
        print_all()


if __name__ == "__main__":
    main()

# user_input = ""
#
# if user_input == "print":
#     for country, population in country_pop.items():
#         print(f"{country}==>{population}")
# elif user_input == "add":
#     user_input_country = input("Enter the country name: ")
#     if user_input_country in country_pop:
#         print("The country exists in our dataset.")
#     elif user_input_country not in country_pop:
#         user_input_population = input("Enter the population: ")
#         country_pop[user_input_country] = user_input_population
#         print(
#             f"The country {user_input_country} has been added to the dataset and has a population of "
#             f"{user_input_population} million people."
#         )
# elif user_input == "remove":
#     user_input_remove = input("Enter the country name you want to remove: ")
#     if user_input_remove in country_pop:
#         country_pop.pop(user_input_remove)
#         print(f"The country {user_input_remove} has been removed from the dataset.")
#         for country, population in country_pop.items():
#             print(f"{country}==>{population}")
# elif user_input == "query":
#     user_input_query = input("Enter the country name you want to query: ")
#     if user_input_query in country_pop:
#         print(
#             f"The population of {user_input_query} is {country_pop[user_input_query]} million people."
#         )
#     else:
#         print("The country does not exist in our dataset.")
