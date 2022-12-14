import pandas as pd

df=pd.read_csv('online_retail.csv')
df.head() #print the first n rows in dataframe

print(df)

df['LinePrice'] = df['Quantity'] * df['UnitPrice']
df.head()

print(df)

df_customers=df.groupby('CustomerID').agg(
    orders=('InvoiceNo','nunique'),
    skus=('StockCode','nunique'),
    quantity=('Quantity','sum'),
    revenue=('LinePrice','sum'),
).reset_index()

df_customers.head()

print(df-customers)




