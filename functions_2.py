def volume_cylinder(radius, height):
    v = 22/7 *radius **2 *height
   '''Calculate volume cylinder'''
    return v

print(volume_cylinder(7, 10))
print(volume_cylinder(10.65, 32.33))


# key - value pairs args
v1 = volume_cylinder(height=17, radius=10)


# optional parameters
def volume_cone(radius, height, decimal=2):
    v = 1/3 * 22/7 *radius **2 *height
    v = round(v, decimal)
    return v



print(volume_cone(20, 15, decimal=3))
print(volume_cone(20, 15,))