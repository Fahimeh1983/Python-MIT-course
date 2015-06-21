import os
import csv
import numpy as np

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(),filename)
    return file_path

def read_csv(filepath):
    data = []
    with open (filepath,'rU') as csv_file:
        reader = csv.reader(csv_file)
        header = csv_file.next()
        for row in reader:
           data.append(row)
        data = np.array(data)
        return data
        
path = get_file_path('train.csv')            
data = read_csv(path)

#numpy allowes us to do some incredible things for "masking"
female_index = data[0::,4] == "female"
male_index = data[0::,4] != "female"

#save the value of the second column (survived) for men and women 
women_onboard = data[female_index,1].astype(np.float)
men_onboard = data[male_index,1].astype(np.float)

#print np.size(women_onboard), np.size(men_onboard)
percentage_women_survived = np.sum(women_onboard)/np.size(women_onboard) 
percentage_men_survived = np.sum(men_onboard)/np.size(men_onboard)  

print "percentage of women survived: ",  percentage_women_survived * 100. 
print "percentage of men survived: ",  percentage_men_survived * 100.

# now we are done with the training, lets predict based on gender only
# if the test is a male, we predict he wont survive and if it is a female
# we predict that she will survive~/work/python-mini-project
# we write the results in gender_base_prediction.csv

test_file_path = get_file_path('test.csv')    
test_file_data = read_csv(test_file_path)
gender_base_prediction_file = open('gender_base_prediction.csv','wb')
gender_base_prediction_file_object = csv.writer(gender_base_prediction_file)
gender_base_prediction_file_object.writerow(["PassengerId","Survived"])

for row in test_file_data:
    if row[3] == "female":
        gender_base_prediction_file_object.writerow([row[0],"1"])
    else :
        gender_base_prediction_file_object.writerow([row[0],"0"])
gender_base_prediction_file.close()
