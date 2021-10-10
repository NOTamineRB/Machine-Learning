import pandas as pd
import numpy as np
training_data = pd.read_csv('Absenteeism_at_work.csv', sep = ';')
training_data.head()
training_data['Absenteeism time in hours'].replace([1,2,3,4,5,6,7,8,9,10],1,inplace=True)
training_data['Absenteeism time in hours'].replace([16,24,40,32,120,80,64,112,56,104,48],1,inplace=True)
training_data['Absenteeism time in hours'].value_counts()