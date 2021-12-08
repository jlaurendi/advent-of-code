import sys

def get_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + get_fuel(fuel)

with open('advent-input.txt') as f:
    a = f.readlines()


    total_fuel = 0
    for i in a:
        i = int(i)
        total_fuel += get_fuel(i)

print(total_fuel)
# print(get_fuel(1969))
# print(get_fuel(100756))