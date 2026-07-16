#day 2 learning variables
#exercise 1
import math
from ast import compare

first_name = input("Enter 1st_name")
last_name = input("Enter last_name")
full_name = last_name + " " + first_name
country = input("Enter country: ")
city = "HCM"
age = input("Enter age: ")
age_int = int(age)
year = 2007
is_married = False
is_true = False
is_light = True
phone, pc, laptop = "Xiaomi", "Dont have one", "Dell G15"

#Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age_int))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(phone))
print(type(pc))
print(type(laptop))

len(first_name)
len(last_name)
num_one= 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division  = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_two // num_one
in_radius = input("Enter radius: ")
radius = float(in_radius)
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2*math.pi * radius
print(area_of_circle)
print(circum_of_circle)

help('keywords')