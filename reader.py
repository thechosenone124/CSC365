import csv
import pandas as pd
import numpy as np

#Takes the list.txt and teachers.txt file and merges them into one big text file
def createCSV():
   listcols=['StLastName', 'StFirstName', 'Grade', 'Classroom', 'Bus', 'GPA']
   teachercols = ['TLastName', 'TFirstName', 'Classroom']

   df1 = pd.read_csv('list.txt', names=listcols, header=None)
   df2 = pd.read_csv("teachers.txt", names=teachercols, header=None)

   df3 = df1.merge(df2, on=["Classroom"], how='inner')
   df3.to_csv("final.txt",index=False,header=False)
   df3.to_csv("key.txt",index=False,header=True) #this one labels the columns

