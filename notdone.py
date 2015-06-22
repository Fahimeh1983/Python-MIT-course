import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def get_path(filename):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir,filename)
    return file_path

def read_csv(filepath):
    data = []
    input_file = open(filepath,'rU')
    input_file_object = csv.reader(input_file)
    header = input_file_object.next()
    for row in input_file_object:
        data.append(row)
    data = np.array(data)
    return data
    
def read_as_pd(filepath):
    data_frame = pd.read_csv(filepath)
    return data_frame
    
input_file_path = get_path('train.csv')
data = read_csv(input_file_path)      
df = read_as_pd(input_file_path)

# DATA EXPLORATION : descriptions
#print df.describe() #This prints amazing informations
#sns.kdeplot(df["Fare"].dropna(), shade=True)
#plt.show()

# most of the fare are below 40, therefore we consider all above 40, equalt to 39
Fare_ceiling = 40
Those_paid_more_than_Fare_ceiling = data[0::,9].astype(np.float) >= Fare_ceiling
data [Those_paid_more_than_Fare_ceiling, 9] = Fare_ceiling -1 

Fare_bracket_size = 10 #0-10,10-20,20-30,30-40
number_of_Fare_brackets = Fare_ceiling / Fare_bracket_size
number_of_classes = len(df["Pclass"].unique())

#clustering
for i in range(number_of_classes):
    condition = (data[0::,4]== "female" ) \
    & (data[0::,2].astype(np.float) == i+1) \
    & (data[0::,9].astype(np.float) >= 10)\
    & (data[0::,9].astype(np.float) < 30.)
    print condition
    
sns.boxplot(df["Fare"],df["Sex"],vert=False)
plt.show()
