import sys

def get_fuel(mass):
    return mass // 3 - 2

with open('advent-input.txt') as f:
    a = f.readlines()


    total_fuel = 0
    for i in a:
        i = int(i)
        total_fuel += get_fuel(i)

print(total_fuel)
# print(get_fuel(1969))
# print(get_fuel(100756))