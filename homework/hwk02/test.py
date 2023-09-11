import pandas as pd
import matplotlib.pyplot as plt

pepsi = pd.read_csv('q5_pepsi.csv')
coke = pd.read_csv('q5_coke.csv')

# scatter plot
plt.scatter(pepsi['Adj Close'], coke['Adj Close'])
plt.title('Scatterplot of Pepsi vs. Coke Stock Prices last 3 months')
plt.ylabel('Pepsi Stock Adjusted Closing Price ($)')
plt.xlabel('Coca Cola Stock Adjusted Closing Price ($)')

# plot regression line
from scipy import stats

m, b, r_value, p_value, std_err = stats.linregress(pepsi['Adj Close'], coke['Adj Close'])
plt.plot(pepsi['Adj Close'], m*pepsi['Adj Close'] + b, color='red')

plt.show()