#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from IPython.display import display, HTML
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


dt=pd.read_csv(r"C:\Users\anwes\Downloads\population-2030-2040-1.csv",encoding='unicode_escape')


# In[4]:


dt.shape


# In[71]:


dt.head(6)


# In[70]:


dt['Time']=dt['Time'].astype('int')


# In[6]:


dt.info()


# In[7]:


pd.isnull(dt).sum()


# In[8]:


dt.shape


# In[9]:


dt.dropna()


# In[10]:


pd.isnull(dt).sum()


# In[11]:


rows_with_nulls = dt[dt.isnull().any(axis=1)]


# In[12]:


print(rows_with_nulls)


# In[13]:


dt.dropna(inplace=True)


# In[14]:


dt.columns


# In[15]:


dt.rename(columns={'PopMale':'Male_population','PopFemale':'Female_population'},inplace=True)


# In[16]:


dt.columns


# In[17]:


description = dt[['Male_population','Female_population','PopTotal']].describe()
display(HTML("<h3>\nDescriptive statistics for specified columns:</h3>"))
print(description)


# In[18]:


dt.head


# In[19]:


dt['Male_population'].dtypes


# In[20]:


dt['Female_population'].dtypes


# In[21]:


dt['PopTotal'].dtypes


# In[22]:


dt['Male_population'] = pd.to_numeric(dt['Male_population'], errors='coerce')
dt['PopTotal'] = pd.to_numeric(dt['PopTotal'], errors='coerce')


# In[23]:


dt['Male_population'] = dt['Male_population'].astype('float64')
dt['PopTotal'] = dt['PopTotal'].astype('float64')


# In[25]:


description = dt[['Male_population','Female_population','PopTotal']].describe()
print("\nDescriptive statistics for specified columns:")
print(description)


# In[26]:


# Melting the DataFrame to have a single column for population type
dt_melted = dt.melt(value_vars=['Male_population', 'Female_population'],
                    var_name='Population_Type', 
                    value_name='Population_Value')

# Create a bar plot for the melted DataFrame
fig, ax = plt.subplots()
a=sns.barplot(x='Population_Type', y='Population_Value', data=dt_melted, ax=ax,errorbar=None, hue='Population_Type')
ax.set_title('Bar Plot of Male and Female Populations')

# Add labels to each bar
for container in a.containers:
    for bar in container:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, f'{height:.0f}', ha='center', va='bottom')

plt.show()


# In[29]:


#Distribution og population by year
year_population = dt.groupby('Time')['PopTotal'].sum()

# Plotting the pie chart
plt.figure(figsize=(8, 6))
year_population.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution by Year')
plt.ylabel('')  # Hide the y-label as it's unnecessary for the pie chart
plt.show()


# In[35]:


dt.columns


# In[32]:


# Group data by Time and calculate the mean male population
average_male_population = dt.groupby('Time')['Male_population'].mean()

# Normalize the time data to range between 0 and 1
norm = plt.Normalize(average_male_population.index.min(), average_male_population.index.max())

# Choose a colormap
cmap = plt.cm.viridis

# Map the normalized data to the colormap
colors = cmap(norm(average_male_population.index))

# Plotting the bar chart with the colormap
plt.figure(figsize=(10, 6))
average_male_population.plot(kind='bar', color=colors)
plt.title('Average Male Population for Each Year')
plt.xlabel('Year')
plt.ylabel('Average Male Population')
plt.grid(axis='y')
plt.show()


# In[55]:


# Group data by Time and calculate the mean female population
average_female_population = dt.groupby('Time')['Female_population'].mean()

# Normalize the time data to range between 0 and 1
norm = plt.Normalize(average_male_population.index.min(), average_female_population.index.max())

# Choose a colormap
cmap = plt.cm.viridis

# Map the normalized data to the colormap
colors = cmap(norm(average_female_population.index))

# Plotting the bar chart with the colormap
plt.figure(figsize=(10, 6))
average_male_population.plot(kind='bar', color=colors)
plt.title('Average Female Population for Each Year')
plt.xlabel('Year')
plt.ylabel('Average Female Population')
plt.grid(axis='y')
plt.show()


# In[50]:


# Group data by Year and calculate the total male and female population for each age group
grouped_data = dt.groupby('Time').agg({'Male_population': 'sum', 'Female_population': 'sum'}).reset_index()

# Set the positions and width for the bars
bar_width = 0.35
r1 = np.arange(len(grouped_data['Time']))
r2 = [x + bar_width for x in r1]

# Plotting the bar chart
plt.figure(figsize=(14, 8))
plt.bar(r1, grouped_data['Male_population'], color='grey', width=bar_width, edgecolor='grey', label='Male')
plt.bar(r2, grouped_data['Female_population'], color='brown', width=bar_width, edgecolor='grey', label='Female')

# Adding titles and labels
plt.title('Male and Female Population for Each Year')
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Population', fontweight='bold')
plt.xticks([r + bar_width / 2 for r in range(len(grouped_data['Time']))], grouped_data['Time'])
plt.legend()

# Show the plot
plt.show()


# In[66]:


# Group data by Time and Location, and calculate the total population for each group
grouped_data = dt.groupby(['Time', 'Location']).agg({'PopTotal': 'sum'}).reset_index()

# Create an empty DataFrame to store the top 5 locations for each year
top_5_locations_per_year = pd.DataFrame()

# Iterate over each year to get the top 5 locations by population
for year in grouped_data['Time'].unique():
    # Filter data for the current year
    year_data = grouped_data[grouped_data['Time'] == year]
    
    # Sort data by population in descending order and select the top 5 locations
    top_5 = year_data.sort_values(by='PopTotal', ascending=False).head(5)
    
    # Append the top 5 locations to the DataFrame
    top_5_locations_per_year = pd.concat([top_5_locations_per_year, top_5])

# Reset the index of the final DataFrame
top_5_locations_per_year = top_5_locations_per_year.reset_index(drop=True)

# Display the resulting DataFrame with a heading
display(HTML("<h3>5 Locations with Highest Population for Each Year</h3>"))
display(top_5_locations_per_year)


# In[61]:


#Plotting the Population spending according to Age group
#custom_palette=sns.color_palette("viridis",len(dataset['Age Group'].unique()))
plt.figure(figsize=(120, 25))
a=sns.barplot(x='Location', y='PopTotal', data=dt, hue='AgeGrp',errorbar=None)
plt.title('Population Distribution by Age Group')
plt.xlabel('Location')
plt.ylabel('Total Population')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# for bars in a.containers:
#     a.bar_label(bars)
plt.show()


# In[36]:


#Plotting the Population spending according to Age group
#custom_palette=sns.color_palette("viridis",len(dataset['Age Group'].unique()))
plt.figure(figsize=(10, 5))
a=sns.barplot(x='AgeGrp', y='PopTotal', data=dt, hue='AgeGrp',errorbar=None)
plt.title('Population Distribution by Age Group')
plt.xlabel('AgeGrp')
plt.ylabel('Total Population')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# for bars in a.containers:
#     a.bar_label(bars)
plt.show()


# In[38]:


#Plotting the Male Population spending according to Age group
#custom_palette=sns.color_palette("viridis",len(dataset['Age Group'].unique()))
plt.figure(figsize=(10, 5))
a=sns.barplot(x='AgeGrp', y='Male_population', data=dt, hue='AgeGrp',errorbar=None)
plt.title(' Distribution of male population by Age Group')
plt.xlabel('AgeGrp')
plt.ylabel('Male population')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# for bars in a.containers:
#     a.bar_label(bars)
plt.show()


# In[39]:


#Plotting the Female Population spending according to Age group
#custom_palette=sns.color_palette("viridis",len(dataset['Age Group'].unique()))
plt.figure(figsize=(10, 5))
a=sns.barplot(x='AgeGrp', y='Female_population', data=dt, hue='AgeGrp',errorbar=None)
plt.title(' Distribution of Female population by Age Group')
plt.xlabel('AgeGrp')
plt.ylabel('Female population')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# for bars in a.containers:
#     a.bar_label(bars)
plt.show()


# In[51]:


# Group data by AgeGrp and calculate the total male and female population for each age group
grouped_data = dt.groupby('AgeGrp').agg({'Male_population': 'sum', 'Female_population': 'sum'}).reset_index()

# Sort the data by AgeGrp
grouped_data = grouped_data.sort_values(by='AgeGrp')

# Set the positions and width for the bars
bar_width = 0.35
r1 = np.arange(len(grouped_data['AgeGrp']))
r2 = [x + bar_width for x in r1]

# Plotting the bar chart
plt.figure(figsize=(14, 8))
plt.bar(r1, grouped_data['Male_population'], color='grey', width=bar_width, edgecolor='grey', label='Male')
plt.bar(r2, grouped_data['Female_population'], color='brown', width=bar_width, edgecolor='grey', label='Female')

# Adding titles and labels
plt.title('Male and Female Population for Each Year')
plt.xlabel('AgeGrp', fontweight='bold')
plt.ylabel('Population', fontweight='bold')
plt.xticks([r + bar_width / 2 for r in range(len(grouped_data['AgeGrp']))], grouped_data['AgeGrp'])
plt.legend()

# Show the plot
plt.show()


# In[69]:


# Group data by AgeGrp and Location, and calculate the total population for each age group
grouped_data = dt.groupby(['AgeGrp', 'Location']).agg({'PopTotal': 'sum'}).reset_index()

# Create an empty DataFrame to store the top 5 locations for each age group
top_5_locations_per_agegrp = pd.DataFrame()

# Iterate over each age group to get the top 5 locations by population
for age_group in grouped_data['AgeGrp'].unique():
    # Filter data for the current age group
    agegrp_data = grouped_data[grouped_data['AgeGrp'] == age_group]
    
    # Sort data by population in descending order and select the top 5 locations
    top_5 = agegrp_data.sort_values(by='PopTotal', ascending=False).head(5)
    
    # Append the top 5 locations to the DataFrame
    top_5_locations_per_agegrp = pd.concat([top_5_locations_per_agegrp, top_5])

# Reset the index of the final DataFrame
top_5_locations_per_agegrp = top_5_locations_per_agegrp.reset_index(drop=True)

# Display the resulting DataFrame with a heading
display(HTML("<h3>Top 5 Locations with Highest Population for Each Age Group</h3>"))
display(top_5_locations_per_agegrp)

