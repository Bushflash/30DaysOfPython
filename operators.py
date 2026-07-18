# #day 3 learning operators and more math related
# # age = 10
# # height = 150.0
# # complex = 1 + 1j
# # print(type(complex))
# # tria_height = input("Enter height: ")
# # t_h = float(tria_height)
# # tria_base = input("Enter base: ")
# # t_b = float(tria_base)
# # area = 0.5 * t_h * t_b
# # print('The area of triangle is ', area)
# # side_a = float(input("Enter side a: "))
# # side_b = float(input("Enter side b: "))
# # side_c = float(input("Enter side c: "))
# # perimeter_tria = side_a + side_b + side_c
# # print(perimeter)
# import math
#
# # length = int(input("Enter length: "))
# # width = int(input("Enter width: "))
# # area_rec  = length * width
# # perimeter_rec = (length+width) * 2
# # print(area_rec)
# # print(perimeter_rec)
#
# # pi = 3.14
# # cir_radius = float(input("Enter radius: "))
# # cir_area = pi * cir_radius * cir_radius
# # cir_circumference = 2 * pi * cir_radius
#
# # y=2x-2
# # m = 2
# # b = -2
# # slope = m
# # y_intercept = b
# # if m!=0:
# #     x_intercept = -b/m
# # else:
# #     x_intercept = None
# #
# # print(f"Slope (m): {slope}")
# # print(f"Y-intercept: {y_intercept}")
# # print(f"X-intercept: {x_intercept}")
# #
# # #task 9
# # x1,y1 = 2,2
# # x2,y2 = 6,10
# # slope = (y2-y1)/(x2-x1)
# # euclidean_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# #
# # #taks10
# # print(euclidean_distance>slope)
#
# #t11
# # x = int(input("Enter a number: "))
# # y = x^2+6*x + 9
# # print(y)
#
# # print(len('python')>len('dragon'))
#
# #task 13
# # if 'on' in 'python' and 'dragon':
# #     print(True)
# # else:
# #     print(False)
#
# # if 'jargon' in 'I hope this course is not full of jargon.':
# #     print(True)
# # else:
# #     print(False)
# #
#
# # if not 'on' in 'python' and 'dragon':
# #     print(True)
# # else:
# #     print(False)
#
#
# # len_python = len('python')
# # to_float = float(len_python)
# # print(to_float)
# # to_string = str(to_float)
# # print(type(to_string))
#
# #check if even or not
# # a = input("Enter first number: ")
# # if a%2 != 0:
# #     print("odd")
# # else:
# #     print("even")
#
# # a = 7//3
# # b = int(2.7)
# # print(a==b)
#
#
# # print(type('10')==type(10))
#
# #Check if int('9.8') is equal to 10
# # not possible will get error or am just wrong
#
# # hours = int(input("Enter hours: "))
# # rate_per_hour = int(input("Enter rate per hour: "))
# # print('Your weekly earning is,', rate_per_hour * hours)
#
# # years = int(input("Enter number of years: "))
# #
# # second_per_minute = 60
# # minutes_per_hour = 60
# # hour_per_day = 24
# # days_per_year = 365
# # seconds_per_year = second_per_minute*minutes_per_hour*hour_per_day*days_per_year
# #
# # total_secoonds = years*seconds_per_year
# # print(total_secoonds)
#
# #23print(1,1,1,1,1)
# # print(2,1,2,4,8)
# # print(3,1,3,9,27)
# # print(4,1,4,16,24)
# # print(5,1,5,25,125)
# #
# for i in range(1,6):
#     values = [i,i**0,i**1,i**2,i**3]
#     print(*values)
