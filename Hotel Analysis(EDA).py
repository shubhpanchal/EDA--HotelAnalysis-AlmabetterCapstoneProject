# -*- coding: utf-8 -*-
"""
Spyder Editor

Freelance Developer : Shubham Panchal 
Date: 11 Sept 2022
Last
This is a temporary script file.
"""
# importing required Libraries
import numpy as np
import pandas as pd
 
#Importing data viz libraries
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Ignore Warnings
import warnings
warnings.filterwarnings('ignore')

# imprting dataset
original_df = pd.read_csv('C:/Users/shubh/My python/Hotel Analysis - Capstone Project on EDA/Copy of Hotel Bookings.csv')

#Creating a copy of dataset to work with
hotel = original_df.copy()
hotel.head()

#understaning the data
hotel.info()

'''
Data Cleaning Procedures
'''
#Dropping the columns that we dont need
hotel.drop(hotel[['reservation_status_date','days_in_waiting_list','booking_changes','previous_bookings_not_canceled',
                   'previous_cancellations','arrival_date_week_number']], axis=1, inplace=True)
hotel.shape

'''
Dealing with Duplicate Values
'''
# Lets check the shape of the data and then check for duplicate data and remove them if any.
print('The shape of the data is :', hotel.shape)
print('The shape of the duplicated data is :',hotel[hotel.duplicated()].shape)
hotel.drop_duplicates(inplace = True)
print('The shape of the hotel data after removing duplicate entries is :', hotel.shape)

'''
Dealing with Missing Values
'''
# Checking for Missing Values
pd.concat([hotel.isnull().sum(),round(100*(hotel.isnull().sum()/len(hotel)),2)], axis=1, keys=['Missing Values', '% Missing Values'])
# Creating a dataframe that has number of missing values and % of missing values.

# Sorting the null values in a descending manner
hotel.isnull().sum().sort_values(ascending = False)[:5]

# Dropping the company columns and verifying it
hotel.drop(hotel[['company']], axis=1, inplace=True)
print('Company Column in Dataset : ','company' in hotel.columns) #Checking if we have successfully dropped company column from the dataset
print('_'*75)

#  Lets treat the missing values in agent column
hotel['agent'] = hotel['agent'].fillna(0) # Imputing 0 to represent that the bookings were not done through any agent.
hotel['agent'] = hotel['agent'].astype('int').astype('str') # Changing the datatype as its a categorical data.
print('The missing values in agent columns are : ',hotel['agent'].isnull().sum())
print('The dtype of agent column is : ', hotel['agent'].dtype)
print('_'*75)

# Lets treat the missing values in childrens column
hotel['children'] = hotel['children'].fillna(hotel['children'].median())
hotel['children'] = hotel['children'].astype('int') #Changing the dtype to int as childrens cant be in fractions.
print('The Missing Values in children column are : ', hotel['children'].isnull().sum())
print('The dtype of children column is : ', hotel['children'].dtype)
print('_'*75)

# Lets treat the missing values in country column
hotel['country'] = hotel['country'].fillna('OTH') #OTH Represents visitors from unknown countries.
print('The missing values in country column are : ', hotel['country'].isnull().sum())
print('The dtype of country column is : ', hotel['country'].dtype)
print('_'*75)

# Lets check if we still have any column with missing values
hotel.isnull().sum().sort_values(ascending=False)[:5]

'''
Data Preparation and Feature Engineering
'''
# Lets create a column by combining day, month and year column to create a new columns 'arrival_date'
from datetime import datetime as dt
hotel['arrival_date'] = hotel['arrival_date_year'].astype('str') + hotel['arrival_date_month'] + hotel['arrival_date_day_of_month'].astype('str')
hotel['arrival_date'] = hotel['arrival_date'].apply(lambda x : dt.strptime(x,'%Y%B%d'))

# Creating a Columns that represents if the customer was assingned the room that was originally booked
hotel['got_preferred_room'] = np.where((hotel['reserved_room_type']==hotel['assigned_room_type']),'1','0')

# Lets calculate length of stay by adding stays_in_weekend_nights and stays_in_week_nights, with that we can compute revenue by multiplying revenue to length of stay.
hotel['length_of_stay'] = hotel['stays_in_weekend_nights'] + hotel['stays_in_week_nights']
hotel['revenue'] = hotel['adr'] * hotel['length_of_stay']

# Calculating total number of guests by adding Adults, babies and childrens.And deleting the rows where total_guests = 0
hotel['total_guests'] = hotel['adults'] + hotel['children'] + hotel['babies']
hotel = hotel.loc[hotel['total_guests']>0]

# Creating a new column to know the season in Portugal.
def season(month):
  if (month == 'March'or month =='April' or month=='May'):
    return 'Spring'
  elif(month =='June' or month == 'July' or month == 'August' or month == 'September'):
    return 'Summer'
  elif(month =='October' or month == 'November' or month == 'December'):
    return 'Autumn'
  else:
    return 'Winter'
hotel['season'] = hotel['arrival_date_month'].apply(season)

# Creating a new column to see the family type.
def family_type(total_guest):
  if(total_guest<2):
    return 'Single'
  elif (total_guest==2):
    return 'Couple'
  else:
    return 'Family/Group'
hotel['family_type'] = hotel['total_guests'].apply(family_type)

# checking the info of the dataset
hotel.info()

'''
Changing the Column types to appropriate column types
'''
# Changing the numerical columns to categorical columns
change_to_object =  ['arrival_date_year','arrival_date_day_of_month','is_repeated_guest','is_canceled']
for col in change_to_object:
  hotel[col] = hotel[col].astype('str')
  print('Successfully changed the ' + col + ' dtype to :',hotel[col].dtype)
  
'''
Defining Numerical and Categorical Columns.
'''
print('Numerical Columns :-')
numerical = hotel.describe().columns
print(numerical)
print('_'*75)
print('Categorical Columns:-')
categorical = hotel.describe(include=['object','category']).columns
print(categorical)
print('_'*75)

'''
Exploratory Data Analysis
'''
# Checking the numerical description of the whole dataset
hotel.describe([0.25,0.50,0.75,0.90,0.95]).T

'''
Outlier Analysis.
'''
for col in numerical:
  sns.boxplot(x=hotel[col])
  plt.show()
  
# Outlier treatment
hotel = hotel.loc[hotel['lead_time']<300]
hotel = hotel.loc[hotel['length_of_stay'] <10]
hotel = hotel.loc[hotel['adults']<5]
hotel = hotel.loc[hotel['children']<5]
hotel = hotel.loc[hotel['babies']<5]
hotel = hotel.loc[hotel['adr'] <300]
hotel = hotel.loc[hotel['adr']>50]
hotel.shape

'''
Univariate Analysis.
'''
# plot bar chart for each numerical column with mean and median.
for col in numerical:
  fig = plt.figure(figsize=(9,6))
  ax = fig.gca()
  feature = hotel[col]
  feature.hist(bins=30, ax= ax)
  ax.axvline(feature.mean(), color= 'red', linestyle='dashed',linewidth=2)
  ax.axvline(feature.median(), color ='green', linestyle='dashed', linewidth=2)
  ax.set_title(col+'- Mean : '+str(feature.mean())+', Median : '+str(feature.median()))
plt.show()

'''
Lets Explore the Relationship of Columns and see how it affects revenue
Bivariate Analysis.
'''
for col in numerical.drop(['revenue']):
  fig = plt.figure(figsize = (9,6))
  ax = fig.gca()
  feature = hotel[col]
  label = hotel['revenue']
  correlation = feature.corr(label)
  plt.scatter(x=feature, y = label)
  plt.xlabel(col)
  plt.ylabel('Revenue')
  ax.set_title('revenue vs ' + col + ' correlation: ' + str(correlation))
  z = np.polyfit(hotel[col], hotel['revenue'],1)
  y_hat = np.poly1d(z)(hotel[col])

  plt.plot(hotel[col], y_hat, 'r--', lw=1)

plt.show()

'''
Multivariate Analysis
'''
# Plotting the correlation heatmap
plt.figure(figsize = (16,8))
correlation = hotel.corr()
sns.heatmap(correlation, annot=True, cmap ='coolwarm')

'''
Exploring the Categorical Variable
'''
for col in categorical:
  if hotel[col].nunique()<=20:
    counts = hotel[col].value_counts().sort_index()
    fig = plt.figure(figsize=(9,6))
    ax= fig.gca()
    counts.plot.bar(ax=ax, color='steelblue')
    ax.set_title(col + ' counts')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')
    plt.show()
  else:
    pass

# Lets check the top 5 agents that bring the most bookings
agents_data = hotel['agent'].value_counts().reset_index()
agents_data.rename(columns={'index':'Agent'}, inplace = True)
agents_data.rename(columns={'agent':'Count'}, inplace=True)
plt.figure(figsize=(10,5))
plt.title('Top 5 Agents')
sns.barplot(x= 'Agent', y ='Count', data= agents_data[:5])
plt.show()

# Finding top 3 months which highest number of bookings.
month_data = hotel['arrival_date_month'].value_counts().reset_index()
month_data.rename(columns={'index':'Month'}, inplace = True)
month_data.rename(columns={'arrival_date_month':'Count'}, inplace=True)
plt.figure(figsize=(10,5))
plt.title('Top 3 Months')
sns.barplot(x= 'Month', y ='Count', data= month_data[:3])

# Plotting a pie chart to see cancellations data
cancellation_df = pd.DataFrame(hotel['is_canceled'].value_counts().reset_index())
cancellation_df.rename(columns={'index':'label','is_canceled':'Count'},inplace =True)
label = cancellation_df['label'].tolist()
count = cancellation_df['Count'].tolist()
explode = [0,0.125]
colors = sns.color_palette('bright')
plt.figure(figsize=(6,6))
plt.pie(count, labels=label, colors=colors, autopct='%.0f%%',explode=explode, shadow=True)
plt.title('Cancellation Rate in Hotel Data')
plt.legend()
plt.show()

# Checking the percentage of customers whose rooms were changed.
got_preferred_room = pd.DataFrame(hotel['got_preferred_room'].value_counts().reset_index())
got_preferred_room.rename(columns={'index':'label','got_preferred_room':'Count'}, inplace =True)
room_label = got_preferred_room['label'].tolist()
room_count = got_preferred_room['Count'].tolist()
explode = [0,0.125]
colors = sns.color_palette('bright')
plt.figure(figsize=(6,6))
plt.pie(room_count, labels=room_label, colors=colors, autopct='%.0f%%',explode=explode, shadow=True)
plt.title('%,of Customers that got originally reserved room')
plt.legend()
plt.show()

# Checking if the Room change was responsible for cancellations.
cancellations = hotel.loc[hotel['is_canceled']=='1']
room_change = pd.DataFrame(cancellations['got_preferred_room'].value_counts().reset_index())
room_change.rename(columns={'index':'label','got_preferred_room':'Count'}, inplace =True)
preferrence_label = room_change['label'].tolist()
preferrence_count = room_change['Count'].tolist()
explode = [0.125,0]
colors = sns.color_palette('bright')
plt.figure(figsize=(6,6))
plt.pie(preferrence_count, labels=preferrence_label, colors=colors, autopct='%.0f%%',explode=explode, shadow=True)
plt.title('% of Custumer which may have cancelled due to room change')
plt.legend()
plt.show()

# Plotting a lineplot to see daily adr over the period of time.
plt.figure(figsize=(16, 6))
sns.lineplot(data = hotel, x = hotel['arrival_date'], y= hotel['adr'], hue=hotel['hotel'])
plt.title('Daily ADR')
plt.show()

# Plotting a lineplot to look at the booking trend.
daily_booking = pd.DataFrame(hotel.groupby('arrival_date')['hotel'].agg(lambda x: x.count()).reset_index())
daily_booking.rename(columns={'index':'arrival_date'},inplace=True)
daily_booking.rename(columns={'hotel':'booking_count'},inplace=True)
plt.figure(figsize=(16,6))
sns.lineplot(data = daily_booking, x=daily_booking['arrival_date'], y =daily_booking['booking_count'])
plt.title('Daily Bookings')
plt.show()

# Looking at the boxplot trend to find the best months for hotel business in terms of revenue.
f,ax = plt.subplots(figsize=(16,8))
fig = sns.boxplot(x= hotel['arrival_date_month'],y = hotel['revenue'], data= hotel, showfliers= False)
fig.axis(ymin =0, ymax=1750);
plt.xticks(rotation=45);
plt.title('Monthly Bookings')
plt.show()

# Plotting the top 15 countries in terms of bookings and highlighting top 5 countries.
mask = hotel['country'].value_counts().index
clrs = ['red' if (x in mask[:5]) else 'orange' for x in mask]
hotel['country'].value_counts()[:15].plot(kind='bar', figsize =(16,6), color=clrs)
plt.grid(axis = 'x')
plt.title('Visitor Countries')
plt.ylabel('Count')
plt.xlabel('Countries')
plt.xticks(rotation=45)
plt.tight_layout()