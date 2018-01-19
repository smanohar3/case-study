
# coding: utf-8

# In[58]:


#import pandas package
import pandas as pd

#import matplotlib package
import matplotlib.pyplot as plt

#creating a dataframe, and reading the csv file : df
df = pd.read_csv('Downloads/Air_Traffic_Landings.csv')

#Print the head of dataframe : df
df.head()


# In[78]:


##Using .value_counts() for ranking
# Select the 'Operating Airline' column of df: Operating Airline
Operating_Airline = df['Operating Airline']

# Count the number of planes in each airline: air_counts
air_counts = Operating_Airline.value_counts()

# Print top 15 airlines ranked by no of planes: 
print(air_counts.head(15))


# In[42]:


#using pivot_table() to count GEO Region
# Construct the pivot table: counted
counted = df.pivot_table(index='Aircraft Manufacturer',
                         columns='Aircraft Body Type',
                          values='GEO Region',
                        aggfunc='count')

print(counted)


# In[79]:


#using fillna() to handle NaN values : 
counted.fillna(counted.mean())


# In[52]:


#Using .nunique() to rank by distinct GEO Summary:
# group df by Aircraft Model : Airline_grouped
Airline_grouped = df.groupby('Aircraft Model')

# Compute the number of distinct Operating Airline for each Aircraft Model: Gsum
Gsum = Airline_grouped['Operating Airline'].nunique()

# Sort the values of Nsports in descending order
Gsum = Gsum.sort_values(ascending=False)

#print top10 rows:
print(Gsum.head(10))

