speed_of_light = 299792458

mass = float(input("Enter mass in kg "))

energy = mass * speed_of_light ** 2

momentum = energy / speed_of_light

print(f"Energy (E) = {energy} joules")
print(f"Momentum (p) = {momentum} kg*m/s")
