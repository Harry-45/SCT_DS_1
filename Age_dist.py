import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('Task1/India_Population_2024.csv')
data['Percentage(%)']=(data['Population (millions)']/data['Population (millions)'].sum())

colors=['yellow','blue','green','pink']
plt.figure(figsize=(10, 6))
plt.bar(data['Age Group'],data['Population (millions)'], color=colors)
plt.title("India's Population distribution Age in 2024.",fontsize=14)
plt.xlabel("Age Group",fontsize=12)
plt.ylabel("Population (millions)",fontsize=12)
plt.show()