street = "Redhill Road"
city = "Nairobi"
country = "Kenya"
address = f"{street}, {city}, {country}"
address_2 = street + ", " + city + ", " + country
print(address)
# Output: Redhill Road, Nairobi, Kenya
print(address_2)
# Output: Redhill Road, Nairobi, Kenya

geo_fact = "The Earth revolves around the sun."
print(geo_fact[10:18])
# Output: revolves
print(geo_fact[-4:-1])
# Output: sun

fruits = 5
veggies = 6
print(f"I eat {fruits} fruits and {veggies} veggies daily.")
# Output: I eat 5 fruits and 6 veggies daily.

string = "maine 200 banana khaye"
string = string.replace("banana", "samosa")
print(string)
# Output: maine 200 samosa khaye
