string_data = input("Enter a comma seperated list of numbers: ")
splitted_data = string_data.split(",")

toprint = 0.00
for elem in splitted_data:
    num = float(elem)
    if elem == "" | elem.find(",,") | type(elem) != "float":
        print("ERROR!")
    square = num * num
    toprint += square

print(toprint)
