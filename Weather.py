import pandas as pd
df = pd.read_csv("Weather Data.csv")
# Find all the unique "Wind Speed" values in the data.
wind = df["Wind Speed_km/h"].nunique()
print(f'Amount of unique "Wind Speed" value:{wind}')
# Find the number of times when the "Weather is exactly Clear"
clear = df[df.Weather == "Clear"]
print(f"Times when the weather is exactly Clear: {len(clear)}")
# Find the number of times when the "Wind Speed was exactly 4 km/h".
wind_4 = df[df["Wind Speed_km/h"] == 4]
print(f"Times when the 'Wind Speed' was exactly 4km/h: {len(wind_4)}")
# Find out all the null (Missing) values in the dataset.
null = df.isnull().sum()
print(f"Null values in the dataset:{null}", sep="\n")
# Rename the column name "Weather" to "Weather Condition".
df.rename(columns={"Weather": "Weather Condition"}, inplace=True)
print(df.head(2))
# What is the mean "Visibility" ?
mean_vis = df["Visibility_km"].mean()
print(f"Mean visibility {mean_vis}")
# What is the Standard Deviation of "Pressure" in this dataset ?
std_pressure = df["Press_kPa"].std()
print(f"Stadard Deviation of Pressure: {std_pressure}")
# What is the Variance of "Relative Humidity" in this dataset ?
var_humidity = df["Rel Hum_%"].var()
print(f"Variance of Relative Humidity: {var_humidity}")
# Find all instances when "Snow" was recorded.
snow = df["Weather Condition"] == "Snow"
print(f"Instances when 'Snow was recorded: {snow.sum()}")
# Find all instances when "Wind Speed is above 24" and "Visibility is 25".
wind_vis = (df["Wind Speed_km/h"] > 24) & (df["Visibility_km"] == 25)
print(
    f"Instances when 'Wind Speed is above 24' and 'Visibility is 25': {wind_vis.sum()}"
)
# What is the Mean value of each column against each "Weather Condition"?
mean_weather = df.groupby("Weather Condition").mean("numeric_only")
print(mean_weather)
# What is the Minimum & Maximum value of each column against each "Weather Condition"?
min_weather = df.groupby("Weather Condition").min("numeric_only")
max_weather = df.groupby("Weather Condition").max("numeric_only")
print(min_weather, max_weather, sep="\n\n")
# Show all the Records where Weather Condition is FOg
fog = df["Weather Condition"] == "Fog"
print(f"Records where Weather Condition is Fog: {fog.sum()}")
# Find all instances when "Weather is Clear" or "Visibility is above 40"
clear_or_vis = (df["Weather Condition"] == "Clear") | (
    df["Visibility_km"] > 40)
# Find all instances when:
# A. Weather is CLear and Relative Humidity is greater than 50
# B. Visibility is above 40
clear_and_humidity = (df["Weather Condition"] ==
                      "Clear") & (df["Rel Hum_%] . 50"])
vis_above_40 = df["Visibility_km"] > 40
print(
    f"Instances when 'Weather is Clear' or 'Visibility is above 40': {clear_or_vis.sum()}"
)
