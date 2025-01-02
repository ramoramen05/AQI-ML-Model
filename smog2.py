import pandas as pd

# Specify the path to your CSV file
csv_file_path = '/content/newdata.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the DataFrame
print(df)

def calculate_aqi(concentration, pollutant):
    # Define concentration breakpoints and AQI categories
    conc_breakpoints = {
        'PM2.5': [(0, 12.0), (12.1, 35.4), (35.5, 55.4), (55.5, 150.4), (150.5, 250.4), (250.5, 350.4), (350.5, 500.4)],
        'PM10': [(0, 54), (55, 154), (155, 254), (255, 354), (355, 424), (425, 504), (505, 604)],
        'O3_8H' : [(0.000, 0.054), (0.055, 0.070), (0.071, 0.085), (0.086, 0.105), (0.106, 0.200)],
        'O3_1H' : [(0.125, 0.164), (0.165, 0.204), (0.205, 0.404), (0.405), (0.504), (0.505, 0.604)],
        'CO' : [(0.0, 4.4), (4.5, 9.4), (9.5, 12.4), (12.5, 15.4), (15.5, 30.4), (30.5, 40.4), (40.5, 50.4)],
        'SO2' : [(0, 35), (36, 75), (76, 185), (186, 304), (305, 604), (605, 804), (805, 1004)],
        'NO2' : [(0, 53), (54, 100), (101, 360), (361, 649), (650, 1249), (1250, 1649), (1650, 2049)]
    }

    # Define AQI breakpoints
    aqi_breakpoints = [0, 50, 100, 150, 200, 300, 500]

    try:
        # Validate input parameters
        if pollutant not in conc_breakpoints:
            raise ValueError("Invalid pollutant.")

        # Find the appropriate concentration range
        concentration_ranges = conc_breakpoints[pollutant]
        for index, (low, high) in enumerate(concentration_ranges):
            if low <= concentration <= high:
                conc_index = index
                break
        else:
            raise ValueError("Concentration value outside valid range.")

        # Calculate AQI
        low_aqi, high_aqi = aqi_breakpoints[conc_index], aqi_breakpoints[conc_index + 1]
        aqi = ((high_aqi - low_aqi) / (concentration_ranges[conc_index][1] - concentration_ranges[conc_index][0])) * (
                    concentration - concentration_ranges[conc_index][0]) + low_aqi

        # Assign AQI category based on the calculated AQI
        aqi_categories = ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy',
                          'Hazardous', 'Hazardous']
        aqi_category = aqi_categories[conc_index]

        return int(round(aqi)), aqi_category

    except ValueError as e:
        return None, str(e)


# FINAL OUTPUT

pollutant_input = input("Enter pollutant [PM2.5, PM10, O3_8H, O3_1H, CO, SO2, NO2 ]: ").upper()
concentration_input = float(input("Enter concentration: "))

result_aqi, result_category = calculate_aqi(concentration_input, pollutant_input)

if result_aqi is not None:
    print(f"The calculated AQI for {pollutant_input} with concentration {concentration_input} is: {result_aqi}")
    print(f"The corresponding AQI category is: {result_category}")
else:
    print(f"Error: {result_category}")
