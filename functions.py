#functions program python3
def square(x):
    return x*x

#default values for fucntion
def sayhello(name="bobo"):
    print("Hello, {}".format(name))

# x_sqr = square(4)
# print(x_sqr)
# sayhello("marc")

# for x in range(10):
#     #print(x, square(x))
#     print("{}**2 -- {}".format(x, square(x)))

# sayhello()
# sayhello("matalino")
# sayhello(name="patal")

import math
def area_circle(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    sayhello("POGI")

#easier imports: from math import pi
#pi

#import <name_of_module>
# from <name_of_module>
# import <func>