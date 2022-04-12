import pandas as pd
##NOTES: This is the current WIP.

#I want to learn how the levels on a dataframe affect the different methods and properties and what you can and can't do with them.
#To do this, I'm going to make several dataframes that are identical except for their levels and indexes, patterned like our trial data.

#Df_A: no levels. It will create an autonumbered index,called RangeIndex, which labels the rows.
#The columns have an index of their names/labels.
Df_A = pd.read_csv('Flat.csv')
print('Df_A','\n',Df_A)

#The index is kind of like an address. It's a value that you can use to refer back to your data later.
#For example, in an Excel spreadsheet, the row numbers (ex: 1) and column names(ex: A) are indexes so you can refer to a cell (ex: A1)
#This makes Df_B, a copy of Df_A, but with 'mouse','day', and 'trial' all set as indexes.
Df_B=Df_A.set_index(['mouse','day','trial'])
print('Df_B','\n',Df_B)
#See how now, they're on different levels in a heirarchy, so that each mouse has a day, and each day has 3 trials.

#The df.info() command gives you information about the structure of your dataframe, and the type of data stored in it.
#Look at the difference between the two. What are the columns? What's in the indexes?
print(Df_A.info())
print(Df_B.info())

#Keys() and columns are the same in a dataframe. Try it
print('Flat df keys()', Df_A.keys(),)
print('MultiIndex df keys()', Df_B.keys(),)

#Notice that it doesn't consider an index to be a column anymore, even if it looks like it's a column when the df is printed.
#The ONLY column in Df_B is 'rcp' because mouse, day, and trial are all indexes and pandas interprets them as if they are attached to the rows.

#Another way Pandas refers to columns and rows is as 'axes' like you'd have on a plot.
#Axis 0 is the rows or the x axis, axis 1 is the columns or the y axis.
print('Flat df axis 0:  ', Df_A.axes[0])
print('Flat df axis 1:  ', Df_A.axes[1])

#Even in a MI dataframe, you still only have 2 axes.
#It's just that instead of a series, the axis with multiple indexes will be a MultiIndex object, which looks kind of like an array.
print('MultiIndex df axes:  ', Df_B.axes)

#Each column in a dataframe is a series. This makes a Pandas series named 'mouse' from Df_A, with an autonumbered RangeIndex.
mouse_series = Df_A['mouse']
print('Mouse series','\n',mouse_series)

#We can't use Df_B['mouse'] because in Df_B, 'mouse' is an index not a column.
#Paste Df_B['mouse'] in the terminal and see what happens when you try.
#Instead, we can reference the indexes by using the df.index object.
print(Df_B.index)

#To get the unique

##TODO: Now I'm trying to show how in Df_B, 'mouse' isn't a column anymore so DfB['mouse'] doesn't work.
#I want to show how you CAN make an equivalent series like what you get in mouse_series, and how you get info like the levels of various indexes.



c = Df_A.columns
