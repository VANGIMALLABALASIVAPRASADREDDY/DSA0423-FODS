import pandas as pd

data = {'Product': ['Laptop','Phone','Laptop','Tablet','Phone','Phone','Tablet','Laptop']}
df = pd.DataFrame(data)

top_products = df['Product'].value_counts().head(5)

print(top_products)
