file = open("wind_farms_uk.csv", "r")

result = []
i = 0
for row in file:
    if i != 0:
        row = row.strip("\n")
        parts = row.split(";")
        name = parts[0]
        coordinate = parts[2]
        coordinate = coordinate.split(",\xa0")
        coordinate[0] = float(coordinate[0])
        coordinate[1] = float(coordinate[1])
        capacity = parts[3]
        wind_turbines = parts[4]
        result.append([name, coordinate, capacity, wind_turbines])
    i += 1

print(f"wind farms = {result}")