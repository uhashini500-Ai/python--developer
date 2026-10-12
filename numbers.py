def format_number(number, character):
    return format(number, character)


result = format_number(145, 'o')
print("Formatted number:", result)

radius = 84
pi = 3.14
water_per_square_meter = 1.4

area = pi * radius ** 2
total_water = area * water_per_square_meter

print("\nPond Area:", area, "square meters")
print("Total Water:", int(total_water), "liters")

distance = 490
time_minutes = 7

time_seconds = time_minutes * 60
speed = distance / time_seconds

print("\nDistance:", distance, "meters")
print("Time:", time_seconds, "seconds")
print("Speed:", int(speed), "m/s")