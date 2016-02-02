import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

#print freq

#plt.figure()
#plt.bar(freq.keys(), freq.values(), width=1)
#plt.show()

chi, p = stats.chisquare(freq.values())

print ('chi-squared of open credit lines is: {}'.format(chi))
print ('the p-value of the chi-squared for open credit lines is: {}'.format(p))

