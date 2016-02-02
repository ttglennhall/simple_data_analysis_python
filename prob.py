import numpy as np 
import collections
import scipy.stats as stats
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#calculate frequency
c = collections.Counter(x) #print(c)
# calculate the number of instances in the list
count_sum = sum(c.values())
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

#create box plot
plt.boxplot(x)
#plt.show()
plt.savefig("x_array_boxplot.png")

#create histogram
plt.hist(x, histtype='bar')
#plt.show()
plt.savefig("x_array_histogram.png")

#creat qq plot
plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(x, dist="norm", plot=plt)
#plt.show() #this will generate the first graph
plt.savefig("x_array_qqplot.png")






