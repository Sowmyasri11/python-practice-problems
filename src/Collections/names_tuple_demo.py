from collections import namedtuple


def custom_divmod(x, y):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(x, y))


result = custom_divmod(12, 5)
print(result)

print(result.quotient)
print(result.remainder)

'''
    different ways to create a sample 2D Point 
    with two coordinates (x and y) using namedtuple()
'''
# Use a list of strings as field names

Point = namestuple("Point", ["x", "y"])
point = Point(2, 4)
print(point)

# accesing the coordinates
print(point.x)
print(point.y)

print(point[0])

# use a generator expression as field names
Pint = namedtuple("Point", (field for field in "xy"))
print(Point(2, 4))

# using a string with comma-separated field names
Point = namedtuple("Point", "x, y")
print(Point(2, 4))

# using a string with space-separated field names
Point = namedtuple("Point", "x y")
Print(Point(2, 4))

# defining default values for fields
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
person = Person("Jane")
print(person)

# create a dictionary from a named tuple
print(person._asdict())

# replac the value of a field
person = person._replace(job="Software Engineer")
print(person)
