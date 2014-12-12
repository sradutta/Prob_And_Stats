import pandas as pd
from scipy import stats #need this to calculate mode

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

#split the string on the hidden characters that indicate newlines
data = data.splitlines()
#print data

#split each item in this list on the commas
data = [i.split(',') for i in data]
#print data

#create pandas dataframe
column_names = data[0] #first row
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns = column_names)
#print df

#convert columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#calculate mean
alc_mean = df['Alcohol'].mean()
tob_mean = df['Tobacco'].mean()
print "The mean of the alcohol and tobacco is %.2f %.2f" %(alc_mean, tob_mean)

#calculate median
alc_median = df['Alcohol'].median()
tob_median = df['Tobacco'].median()
print "The median of the alcohol and tobacco is %.2f %.2f" %(alc_median, tob_median)

#calculate mode
alc_mode = stats.mode(df['Alcohol'])
tob_mode = stats.mode(df['Tobacco'])
print "The mode of the alcohol and tobacco is %.2f %.2f" %(alc_mode[0], tob_mode[0])


#calculate range
alc_range = max(df['Alcohol'])-min(df['Alcohol'])
tob_range = max(df['Tobacco'])-min(df['Tobacco'])
print "The range for alcoholo and tobbacco is %.2f %.2f" %(alc_range, tob_range)

#calculate variance
alc_var = df['Alcohol'].var()
tob_var = df['Tobacco'].var()
print "The variance for alcohol and tobacco is %.2f %.2f" %(alc_var, tob_var)

#calculate SD
alc_sd = df['Alcohol'].std()
tob_sd = df['Tobacco'].std()
print "The SD for alcoholo and tobacco is %.2f %.2f" %(alc_sd, tob_sd)

#calculate question3
#given: mean = 251, SD = 20, z = 2.3; find the value
value = 2.3*20 + 251
print "The number of days corresponding to a z-score of 2.3 is %.2f" %value









