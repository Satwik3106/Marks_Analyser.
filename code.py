import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Read the Excel file (replace 'filename.xlsx' with your actual file name)
df = pd.read_excel("Marks_secC.xlsx")
# print(df)
# Add a percentage column
df['Percentage'] = (df['marks'] / 15) * 100
var ='name','library id','marks','percentage'
# Categorize students
above_75 = df.var
between_60_75 = df[(df['Percentage'] >= 60) & (df['Percentage'] <= 75)].var
below_60 = df[df['Percentage'] < 60].var
# Print categories
print("Students with >75% marks:\n", above_75, "\n")
print("Students with 60%-75% marks:\n", between_60_75, "\n")
print("Students with <60% marks:\n", below_60, "\n")
# Histogram Plot
plt.figure(figsize=(10, 5))
plt.hist(df['Percentage'], bins=np.arange(0, 105, 5), edgecolor='black', color='blue')
plt.xlabel("Percentage")
plt.ylabel("Number of Students")
plt.title("Histogram Plot")
plt.grid(True)
plt.show()
# Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(df['name'], df['Percentage'], color='blue', edgecolors='black')
plt.xticks(rotation=90)
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.title("Scatter Plot")
plt.grid(True)
plt.tight_layout()
plt.show()
