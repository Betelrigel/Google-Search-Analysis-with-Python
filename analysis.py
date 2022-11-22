# Importing essential libraries

!pip install pytrends
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()


# Dataframe of the top 10 countries which search for YouTube

trends.build_payload(kw_list=["YouTube"])
data = trends.interest_by_region()
data = data.sort_values(by="YouTube", ascending=False)
data = data.head(10)
print(data)


# Visualizing the top 10 countries

data.reset_index().plot(x="geoName", y="YouTube", 
                        figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()


# Visualizing the trend of search queries if they have increased or decreased

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['YouTube'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(20, 15))
data['YouTube'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for YouTube', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
