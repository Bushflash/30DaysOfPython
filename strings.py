# thirty, days, of, python =  'Thirty', 'Days', 'Of', 'Python'
# connect = thirty + ' '+ days +' '+ of +' '+ python
# print(connect)
# string = ['Thirty', 'Days', 'Of', 'Python']
# result = ' '.join(string)
# print(result)
from idlelib.colorizer import prog_group_name_to_tag
from operator import index

# string = ['Coding', 'For' , 'All']
# # connect = string[0] + ' '+ string[1] + ' '+ string[2]
# result = ' '.join(string)
# print(type(string))


# company = "Coding For All"
# print(company)
# print(len(company))

# upper = company.upper()
# print(upper)

# lower = company.lower()
# print(lower)
#
# capitalize = company.capitalize()
# print(capitalize)
#
# title = company.title()
# swap = company.swapcase()
# print(swap)
# print(title)
#
# find = company.find("Coding")
# print(find)

# cut = company[0:7]
# print(cut)

# replace = company.replace("Coding","Python")
# print(replace)

# challenge = 'Coding For All'
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']


# challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(challenge.split(","))

# coding = "Coding For All."
#
# print(coding[0])
# print(coding[-2])
#
# print(coding[10])


name1 = 'Python For Everyone'
name2 = 'Coding For All'
sub2 = 'C'
abbreviation1 = name1[0] + name1[7] + name1[11]
abbreviation2 = name2[0] + name2[7] + name2[11]
print(abbreviation1)
print(abbreviation2)

print(name2.index(sub2))