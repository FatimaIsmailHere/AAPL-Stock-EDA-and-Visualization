import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/python3/pythonProject/data/AAPL_stock_data.csv")


df.columns = ['Price Ticker Date','Close AAPL','High AAPL','Low AAPL','Open AAPL','Volume AAPL']
df = df[2:]
df.reset_index(drop=True, inplace=True)

df['Price Ticker Date'] = pd.to_datetime(df['Price Ticker Date'], errors='coerce')
for col in ['Close AAPL','High AAPL','Low AAPL','Open AAPL','Volume AAPL']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.dropna(inplace=True)

print("SUMMARY:\n", df.describe())
print("\nMISSING VALUES:\n", df.isnull().sum())
print("\nDUPLICATES:", df.duplicated().sum())

plt.figure(figsize=(10, 4))
plt.plot(df['Price Ticker Date'], df['Close AAPL'], label='Close Price')
plt.title('AAPL Close Price Over Time')
plt.xlabel('Price Ticker Date')
plt.ylabel('Close AAPL')
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 4))
plt.plot(df['Price Ticker Date'], df['Volume AAPL'], label='Volume', color='orange')
plt.title('AAPL Volume Traded')
plt.xlabel('Price Ticker Date')
plt.ylabel('Volume AAPL')
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.heatmap(df[['Close AAPL', 'High AAPL', 'Low AAPL', 'Open AAPL', 'Volume AAPL']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
sns.boxplot(data=df[['Close AAPL', 'High AAPL', 'Low AAPL', 'Open AAPL', 'Volume AAPL']])
plt.title("Outlier Detection")
plt.tight_layout()
plt.show()


df['MA20'] = df['Close AAPL'].rolling(20).mean()
plt.figure(figsize=(10, 4))
plt.plot(df['Price Ticker Date'], df['Close AAPL'], label='Close Price', alpha=0.5)
plt.plot(df['Price Ticker Date'], df['MA20'], label='20-Day MA', color='green')
plt.title('20-Day Moving Average of Closing Price')
plt.xlabel('Price Ticker Date')
plt.ylabel('Price AAPL')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
