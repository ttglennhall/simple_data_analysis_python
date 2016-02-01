import pandas as pd
from scipy import stats

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

#split the data
data = data.splitlines()
data = [i.split(',') for i in data]

#create a pandas dataframe
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

#convert data to floats
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#run descriptive stats
#center
print ('Calculating the center of our sets')
print ('The mean for the Alcohol and Tobacco datasets are: {}, {}'.format(df['Alcohol'].mean(), df['Tobacco'].mean()))
print ('The median for the Alcohol and Tobacco datasets are: {}, {}'.format(df['Alcohol'].median(), df['Tobacco'].median()))
print ('The mode for the Alcohol and Tobacco datasets are: {}, {}'.format(stats.mode(df['Alcohol']), stats.mode(df['Tobacco']))) #if all occur equally often, returns smallest number

#variability
print ('\nCalculating the variability in our sets')
print ('The range for the Alcohol and Tobacco datasets are: {}, {}'.format(max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco'])))
print ('The standard deviation of the Alcohol and Tobacco datasets are: {}, {}'.format(df['Alcohol'].std(), df['Tobacco'].std()))
print ('The variance of the Alcohol and Tobacco datasets are: {}, {}'.format(df['Alcohol'].var(), df['Tobacco'].var()))




