#calc
from conditions import password

x = input('Enter first number: ')
y = input('Enter second number: ')



# convert to numbers
try:
     int_x = int(x)
     int_y = int(y)
     print(int_x / int_y)
except:
    print(" Invalid input") #for an error

#
# alt
# except:
#       pass
#
# def add (a, b):
#     pass
#
# if 10 > 5:
#     pass



# convert to float
# int_x = float(int_x)
# int_y = float(int_y)



# convert to string
# int_x = str(x)
# int_y = str(y)


# TODO hello, put something

# pip freeze > requirements.txt
