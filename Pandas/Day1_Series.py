import numpy as np
import pandas as pd
#Creating Pandas Series from list. We can also creat it from dict 
marks=[80,85,84,79]
subject=['English','Math','Bangla','Science']
marks_series=pd.Series(marks,index=subject,name='Makkys marks')
# print(marks_series)

#Some most commonly used Attributes of pandas series
'''print(marks_series.size)
print(marks_series.dtype)
print(marks_series.name)
print(marks_series.is_unique)
print(marks_series.index)
print(marks_series.values)'''

subs=pd.read_csv('/home/maks/Python_practice/Pandas/Day one data set/subs.csv').iloc[:, 0]
koli_ipl=pd.read_csv('Pandas/Day one data set/kohli_ipl.csv',index_col='match_no').iloc[:,0]
movie_set=pd.read_csv('Pandas/Day one data set/bollywood.csv',index_col='movie').iloc[:,0]
#Some methods that are used in pandas
# print(movie_set.head())
# print(movie_set.tail())
# print(movie_set.sample(5))
# print(movie_set.value_counts())
