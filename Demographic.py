import pandas
import seaborn
import matplotlib.pyplot as plt

# Select first  rows with numeric data for plotting
pandas.set_option('display.max_columns', None) # снимаем ограничение на вывод столбцов
pandas.set_option('display.max_rows', None) # снимаем ограничение на вывод строк
data = pandas.read_csv('popage.csv', low_memory=False) # загружаем данные

# Select country name, year, and population columns
print("Table with Country, Year, and Population:")
selected_data = data[['Year', 'Economy Label', 'Absolute value in thousands']].head(5)
print(selected_data)

# Plot the population data
plt.figure(figsize=(15, 6))
plt.bar(range(len(selected_data)), selected_data['Absolute value in thousands'])
plt.title('Population Data - First 5 Rows')
plt.xlabel('Countries')
plt.ylabel('Population (in thousands)')
plt.xticks(range(len(selected_data)), [f"{row['Year']} - {row['Economy Label']}" for _, row in selected_data.iterrows()], rotation=45)
plt.tight_layout()
plt.show()