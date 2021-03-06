import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
#clean data
loansData.dropna(inplace=True) #drop NA values

#boxplot
loansData.boxplot(column=['Amount.Requested','Amount.Funded.By.Investors'], return_type='dict')
plt.title('Amount Requested vs Amount Funded')
#plt.show()
plt.savefig("boxplot_requested_vs_funded.png")

#histogram
lab = ['Amount Requested', 'Amount Funded']
plt.hist([loansData['Amount.Requested'],loansData['Amount.Funded.By.Investors']], stacked=True, label=lab)
plt.legend(loc='upper right')
plt.title('Amount Requested vs Amount Funded')
#plt.show()
plt.savefig("hist_requested_vs_funded.png")

#qq plot
ax1 = plt.subplot(211)
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)

ax2 = plt.subplot(212)
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
#plt.show()
plt.savefig("qqplot_requested_vs_funded.png")


