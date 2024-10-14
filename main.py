# Project 0
# Estimating Monarch Butterfly Population
# Hiba Mirza
# CS 111, Fall 2022, Reckinger
# Keeps track of the eastern population of the monarch butterflies

# TODO: Write the program that estimates the monarch butterfly population.
# TODO: Comment your program appropriately
# TODO: Use appropriate variable names

print()
print("Monarch Butterfly Population Estimation App.")
print()

date = input("Enter date: ")
date = str(date)
width = input("Enter width in km: ")
width = float(width)
length = input("Enter length in km: ")
length = float(length)

area = (length * width) * 100
population = area * 21100000

print()
print("Report made on", date + ".")
print("Total area occupied: {0:.2f}".format(area), "hectares")

print("Estimated population: {0:.2e}".format(population), "monarch butterflies")
print()