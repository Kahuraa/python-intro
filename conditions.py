#conditional (statements
from idlelib.query import HelpSource

#variables == store value
x = 10
y = 50

print(x)
 # snake casing use underscore
my_city ="Nairobi"
my_favorite_sport = "Hockey"

# camel casing
myOldestCar = "Chevrolet"

# classes
name = "Kevin"
age = 30

# types of data
# numbers
height = 3  #(integer)
weight = 60.45 #(float)


full_name = "Daniel Terrence"
distance = 45

# boolean (True/False)
is_listen = True
is_disabled = False

# conditional statements
password = "123456" #(string="")
db_password = "654321"

#if statements
if password == db_password:
    print("Success")
else:
    print("Failed")



score= 64
if score >= 90:
    print("A")
elif score >= 80 and score <=89:
    print("A-")
elif score >= 75 and score <=79:
    print("B+")
elif score >= 70 and score <= 74:
    print("B")
elif score >= 65 and score <= 69:
    print("B-")
elif score >= 60 and score <= 64:
    print("C+")
elif score >= 55 and score <= 59:
    print("C")
elif score >= 50 and score <= 54:
    print("C-")
elif score >= 45 and score <= 49:
    print("D+")
elif score >= 40 and score <= 44:
    print("D")
elif score >= 35 and score <= 39:
    print("D-")
elif score >= 30 and score <= 34:
    print("E")
else:
    print("F")












