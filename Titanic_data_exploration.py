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
#print df.head(10) # This prints the first ten rows
#print df.describe() #This prints amazing informations
#print df["Fare"].median(), df["Age"].median() # Look at the medians 
#print df["Sex"].unique()   # Look at non-numerical values 

# DATA EXPLORATION : histogram
#plt.hist(df["Age"].dropna(), bins=15, range = (df["Age"].min(),df["Age"].max()), color=sns.desaturate("indianRed",1))
#plt.title("Titanic Passengers Age Distribution")
#plt.xlabel("Age")
#plt.ylabel("Count of Passengers")
#plt.show()

#DATA EXPLORATION : Boxplot
#sns.boxplot(df["Age"]) #With seaborn we can group the output based on "Sex"
#sns.boxplot(df["Age"].dropna(), df["Sex"], vert=False) #With seaborn we can group the output based on "Sex"
#plt.show()

#DATA EXPLORATION : Kernel Density Estimate Plot
#sns.kdeplot(df["Age"].dropna(), shade=True)
#sns.distplot(df["Age"].dropna())
#plt.show()

#DATA EXPLORATION : Violin plot
#sns.violinplot(df["Age"].dropna())
#sns.violinplot(df["Age"].dropna(), df["Sex"])
#plt.show()

#DATA EXPLORATION: Cumulative Distribution Function
#sns.kdeplot(df["Age"].dropna(), cumulative=True)
#plt.show()
