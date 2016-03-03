# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:45:05 2016

@author: merongoitom
"""

#%pylab inline
#from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import seaborn as sns


filename = 'nyc_subway_weather.csv'

#Access csv file using panda
subway_df = pd.read_csv(filename) 
#print subway_df.head()           
#print subway_df['ENTRIESn_hourly'].describe()
#print subway_df['latitude']
data_by_location = subway_df.groupby(['latitude','longitude'],as_index=False).mean()
#print data_by_location
#print subway_df.groupby('latitude').groups 
#print data_by_location.head()['latitude']
# Standerdise values
scaled_entries = (data_by_location['ENTRIESn_hourly']/data_by_location['ENTRIESn_hourly'].std())*3 
# lat as x-cord, long as y-cord
plt.scatter(data_by_location['latitude'],data_by_location['longitude'],s=scaled_entries) 



