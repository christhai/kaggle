import csv as csv
import numpy as np
csv_file_object = csv.reader(open('train.csv', 'rb')) 	# Load in the csv file
header = csv_file_object.next() 
data=[]

for row in csv_file_object:
	data.append(row[0:])
data = np.array(data)

# Set some variables
number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

women_only_stats = data[0::,4] == "female" 	# This find
men_only_stats = data[0::,4] != "female"

women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)
# and derive some statistics about them
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived
