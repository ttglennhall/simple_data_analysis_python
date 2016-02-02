import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
#clean data
loansData.dropna(inplace=True) #drop NA values

f, (loansData, loansData) = plt.subplots(1, 2, sharey=True)
#loansData.boxplot(column='Amount.Requested')

#plt.subplot(1,2,1)
loansData.boxplot(column='Amount.Requested')
plt.title('Amount Requested')

#plt.subplot(1,2,2)
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.title('Amount Funded By Investors')

plt.show()

loansData.hist(column='Amount.Requested')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()