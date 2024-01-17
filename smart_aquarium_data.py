# -*- coding: utf-8 -*-

import csv
import random
import pandas as pd

# Function to generate random data within realistic ranges
def generate_data(sensor):
    if sensor == "Temperature (°C)":
        return round(random.uniform(20, 28), 2)  # Celsius
    elif sensor == "pH":
        return round(random.uniform(6.5, 8.5), 2)
    elif sensor == "Oxygen (mg/L)":
        return round(random.uniform(4, 8), 2)  # in mg/L
    elif sensor == "Ammonia-Nitrogen (mg/L)":
        return round(random.uniform(0, 0.5), 3)  # in mg/L
    elif sensor == "Water_Level (%)":
        return round(random.uniform(0, 100), 2)  # Percentage

# Function to generate abnormal values for specific sensors
def generate_abnormal_data(sensor):
    if sensor == "Temperature (°C)":
        return round(random.uniform(35, 40), 2)  # Abnormal high temperature
    elif sensor == "pH":
        return round(random.uniform(4, 5), 2)  # Abnormal low pH
    elif sensor == "Oxygen (mg/L)":
        return round(random.uniform(0, 2), 2)  # Abnormal low oxygen level
    elif sensor == "Ammonia-Nitrogen (mg/L)":
        return round(random.uniform(1, 5), 3)  # Abnormal high ammonia-nitrogen content
    elif sensor == "Water_Level (%)":
        return round(random.uniform(95, 110), 2)  # Abnormal high water level

# Define sensor types
sensors = ["Temperature (°C)", "pH", "Oxygen (mg/L)", "Ammonia-Nitrogen (mg/L)", "Water_Level (%)"]
data = {sensor: [] for sensor in sensors}

# Generate synthetic data for each sensor
for sensor in sensors:
    # Generate normal data
    for _ in range(95):
        data[sensor].append(generate_data(sensor))

    # Generate abnormal data for specific sensors
    if sensor in ["Temperature (°C)", "pH", "Oxygen (mg/L)", "Ammonia-Nitrogen (mg/L)", "Water_Level (%)"]:
        for _ in range(5):
            data[sensor].append(generate_abnormal_data(sensor))
    else:
        for _ in range(5):
            data[sensor].append(None)  # For sensors without abnormal values, append None

# Write data to CSV
with open("./nodered/aquarium_sensor_data.csv", "w", newline="") as csvfile:
    fieldnames = sensors
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Write data row by row
    for i in range(max(len(data[sensor]) for sensor in sensors)):
        row_data = {sensor: data[sensor][i] for sensor in sensors}
        writer.writerow(row_data)

# data = pd.read_csv("aquarium_sensor_data.csv")
