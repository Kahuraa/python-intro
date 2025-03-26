# files
# create , read and open file
from importlib.metadata import files
from types import ClassMethodDescriptorType

from PIL.ImageMorph import MorphOp

file = open("test.txt", "a")

file.write("Hello World\n")

file.close()



# r= read
try:
    file = open("test.txt", "r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("File not found")

# TODO CHECK HOW TO READ AND CREATE CSV FILES
# TODO Class
# TODO OOP
# TODO INHERITANCE

data = [9, 10]
x = data[0]
y = data[1]
x, y = data
print(x)
print(y)



def population():
    return "Nairobi", 40000000



name, pp = population()
print(name)
print(pp)




