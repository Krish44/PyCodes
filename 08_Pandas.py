''' 
-- Pandas allow you to load data from different sources to python, thn use python code to analyse those data
an produce results: tabes, visualization
-- Scrap data from website and store info in panda data-frames
-- Loading data from excel
-- Cannot use panda without Numpy
EDITORS:
 ipython
 Jupitor Notebook - browser based tool
 
'''
#bokeh

import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])
print("df1 :\n",df1, sep='')
# sep='' is to avoid a space in the newline at the beginning, which will be due to ','

df2 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Profit","Value","Price"], index=["First","Second"])
# Not necessary to name index all the time
print("\ndf2 - Along with Index/column names:\n",df2,"\n")

# Extract only one column
print("\nPrinting Profit Column:\n",df2.Profit, sep='')
print("\nmax value in profit:\n",df2.Profit.max(), sep='')

print("\nMean of the df2:\n",df2.mean(), sep='')

df3 = pandas.DataFrame([{"Name":"Krish","Age":"25"},{"Name":"Raj","Age":"25"}])
# There is no Guarantee that order of columns will appear

print(df3)
print("\nType:",type(df3))
print("\nMethods in DataFrame:",dir(df3))
# Use of Mean method
