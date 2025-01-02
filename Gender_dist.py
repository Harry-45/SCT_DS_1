import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv('Task1/Population of India.csv')
plt.figure(figsize=(8,6))
plt.bar(['Male','Female'],[data['Male'].values[0],data['Female'].values[0]],color=['blue','pink'])
plt.xlabel('Gender')
plt.ylabel('Population')
plt.title('Gender distribution in india')
plt.show()
