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
print('Flat df keys()', Df_A.keys(),Df_A.columns)
print('MultiIndex df keys()', Df_B.keys(),Df_B.columns)
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

#Df.index.levels gives you more information about the indexes:
#It gives you a list of the unique values in each index, and the order of the lists corresponds to the level of the index.
print(Df_B.index.levels)
#So the mouse name is level 0, the day is level 2, the trial is level 3.
#You can use df.index.names to get the names of an index ('mouse','day','trial') as a list
print(Df_B.index.names)
#You can use df.swaplevel(a,b) to swap two levels in the heirarchy. Try it:
Df_C=Df_B.swaplevel(0,1)

## Next up I want to talk about how to refer to data. .loc in particular is a pain if you don't know quite what it's doing.
#In Df_A, whose only index is the autonumbering, .loc will only accept the row number as an argument and it will return the entire row as a series.
print(Df_A.loc[5])

#For a MI dataframe, you can use any of the indexes, but they have to be in order.
slice1 = Df_B.loc['F1_PAFT'])
slice2 = Df_B.loc['F1_PAFT','Mon',0:1])
#What happens if you try them out of order? What if you skip a level? Try it in the console.
#Note that you can only select more than one value for the lowest level.
#Df_B.loc['F1_PAFT','Mon',0:1] is valid, but Df_B.loc['F1_PAFT':'M2_PAFT','Mon',0] is not.
#For that, use the slice() function/method
##TODO: HELP HELP I DON'T KNOW THE VOCAB FOR THESE THINGS ARE
slice3 =Df_B.loc[(slice('F1_PAFT','M2_PAFT'),'Mon',0),:]
##TODO: Also slice() treats a comma like it's a : and I don't understand

#Df_A[Df_A['mouse']=='F1_PAFT']