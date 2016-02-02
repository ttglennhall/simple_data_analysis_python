import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import statsmodels.api as sm 

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]
#print loansData['Interest.Rate'][0:5]

loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]
#print loansData['Loan.Length'][0:5]

loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
#print loansData['FICO.Score'][0:5]

#plt.figure()
#p = loansData['FICO.Score'].hist()
#plt.show()

#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
#plt.show()

#each of these are series datatypes
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

#the dependent variable
y = np.matrix(intrate).transpose()

#the independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

#create independent variable matrix
x = np.column_stack([x1,x2])

#linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

#print f
print f.summary()





