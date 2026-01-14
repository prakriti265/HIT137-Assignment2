import os

import csv

yearly_temperatures = {}
all_temperatures = []

temperature_folder = "temperatures"

for filename in os.listdir(temperature_folder):
    if filename.endswith(".csv"):
        year = filename.split("_")[1].split(".")[0]
        yearly_temperatures[year] = []

        file_path = os.path.join(temperature_folder, filename)

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                temperature = row[-1]

                if temperature != "NaN":
                    temp_value = float(temperature)
                    yearly_temperatures[year].append(temp_value)
                    all_temperatures.append(temp_value)

with open("yearly_temperature_stats.txt", "w") as file:
    for year in sorted(yearly_temperatures):
        temps = yearly_temperatures[year]

        average = sum(temps) / len(temps)
        maximum = max(temps)
        minimum = min(temps)

        file.write(f"Year: {year}\n")
        file.write(f"Average Temperature: {average:.2f}\n")
        file.write(f"Maximum Temperature: {maximum:.2f}\n")
        file.write(f"Minimum Temperature: {minimum:.2f}\n\n")

overall_average = sum(all_temperatures) / len(all_temperatures)
overall_max = max(all_temperatures)
overall_min = min(all_temperatures)

with open("overall_temperature_stats.txt", "w") as file:
    file.write("Overall Temperature Statistics\n")
    file.write(f"Average Temperature: {overall_average:.2f}\n")
    file.write(f"Maximum Temperature: {overall_max:.2f}\n")
    file.write(f"Minimum Temperature: {overall_min:.2f}\n")


