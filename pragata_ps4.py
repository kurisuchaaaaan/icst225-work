import geometry

data = input("Enter the side lengths of a triangle: ")
splitted_data = data.split(",")
perimeter = geometry.triangle_perimeter(float(splitted_data[0]),float(splitted_data[1]),float(splitted_data[2]))
area = geometry.triangle_heronsarea(float(splitted_data[0]),float(splitted_data[1]),float(splitted_data[2]))
print("Perimeter: %.2f" %perimeter)
print("Area: %.2f" %area)