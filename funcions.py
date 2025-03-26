# functions
from tkinter.font import names


def area(radius):
    result = 22/7 * radius ** 2
    return result



def sayHi():
    print("Good morning", names)




# TODO hello, put something

print(area(7)) #called
print(area(6.5))
print(area(89.345))
sayHi("Geo")
sayHi("Terry")

a1 = area(66.7)
print(round(a1, 2))