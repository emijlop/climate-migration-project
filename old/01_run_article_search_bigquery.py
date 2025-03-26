# %%
import pandas as pd

# %%
from google.cloud import bigquery

# %%
client = bigquery.Client()

# %%

# Define a query to get the latest events related to "climate change"
query = """
SELECT 
    DATE(PARSE_DATE('%Y%m%d', CAST(SQLDATE AS STRING))) AS Date,
    SOURCEURL,
    AvgTone,
    EventRootCode
FROM `gdelt-bq.gdeltv2.events`
WHERE (Actor1CountryCode = 'SOM' OR Actor2CountryCode = 'SOM')
AND DATE(PARSE_DATE('%Y%m%d', CAST(SQLDATE AS STRING))) 
    BETWEEN DATE '2023-01-01' AND DATE '2023-12-31'
ORDER BY Date DESC
LIMIT 1000
"""

# Run the query and store the result in a DataFrame
df = client.query(query).to_dataframe()

print(df.head())

# %%
df['Date'] = pd.to_datetime(df['Date'])

# %%
df.groupby('Date').count().plot(y='AvgTone', kind='bar')

# %%
min_date_str = df['Date'].min().strftime('%Y-%m-%d')
max_date_str = df['Date'].max().strftime('%Y-%m-%d')


df.to_csv(f'data/somalia_climate_change_from_{min_date_str}_to_{max_date_str}.csv', index=False)


