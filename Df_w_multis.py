import pandas as pd
import loop

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
# See how now, they're on different levels in a heirarchy, so that each mouse has a day, and each day has 3 trials.

# The df.info() command gives you information about the structure of your dataframe, and the type of data stored in it.
# Look at the difference between the two. What are the columns? What's in the indexes?
print(Df_A.info())
print(Df_B.info())

# Keys() and columns are the same in a dataframe. Try it
print('Flat df keys()', Df_A.keys(),Df_A.columns)
print('MultiIndex df keys()', Df_B.keys(),Df_B.columns)
# Notice that it doesn't consider an index to be a column anymore, even if it looks like it's a column when the df is printed.
# The ONLY columns in Df_B are 'rcp', 'speed', and 'variance.'
# Mouse, day, and trial are all indexes, and pandas interprets them as if they are on the rows.

# Another way Pandas refers to columns and rows is as 'axes' like you'd have on a plot.
# Axis 0 is the rows or the x axis, axis 1 is the columns or the y axis.
print('Flat df axis 0:  ', Df_A.axes[0])
print('Flat df axis 1:  ', Df_A.axes[1])

# Even in a MI dataframe, you still only have 2 axes.
# It's just that instead of a series, the axis with multiple indexes will be a MultiIndex object, which looks kind of like an array.
print('MultiIndex df axes:  ', Df_B.axes)

# Each column in a dataframe is a series. This makes a Pandas series named 'mouse' from Df_A, with an autonumbered RangeIndex.
mouse_series = Df_A['mouse']
print('Mouse series','\n',mouse_series)

# We can't use Df_B['mouse'] because in Df_B, 'mouse' is an index not a column.
# Paste Df_B['mouse'] in the terminal and see what happens when you try.
# Instead, we can reference the indexes by using the df.index object.
print(Df_B.index)

# Df.index.levels gives you more information about the indexes:
# It gives you a list of the unique values in each index, and the order of the lists corresponds to the level of the index.
print(Df_B.index.levels)
# So the mouse name is level 0, the day is level 2, the trial is level 3.
# You can use df.index.names to get the names of an index ('mouse','day','trial') as a list
print(Df_B.index.names)
# You can use df.swaplevel(a,b) to swap two levels in the heirarchy. Try it:
Df_C=Df_B.swaplevel(0,1)

## Next up I want to talk about how to refer to data. .loc in particular is a pain if you don't know quite what it's doing.
# Df.loc will try to locate data and parts of the df based on the index.

## SLICING BY ROWS:
# In Df_A, whose only index is the autonumbering, .loc will only accept the row number as an argument and it will return the entire row as a series.
print(Df_A.loc[5])

# For a MI dataframe, you can use any of the indexes, but they have to be in order.
slice1 = Df_B.loc['F1_PAFT']
slice2 = Df_B.loc['F1_PAFT','Mon',0]
# What happens if you try them out of order? What if you skip a level? Try it in the console.

# Note that you can only select more than one value for the lowest level.
# Df_B.loc['F1_PAFT','Mon',0:1] is valid, but Df_B.loc['F1_PAFT':'M2_PAFT','Mon',0] is not.
# For that, use python's slice function. Options are slice(start value,end value, step).
# To select everything, the syntax is slice(None)
slice3 = Df_B.loc[(slice(None),'Mon',[0,1,2]),:]

## SLICING BY COLUMNS:
# Selecting an entire column is easy in either dataframe.
# For a df with no levels you can use df['column']. For a MI df, you can use that or df.loc[:,('column')
Df_A_cols=Df_A[['mouse','day']]
Df_B_cols1=Df_B[['rcp','speed']]
Df_B_cols2=Df_B.loc[:,['rcp','speed']]

# There are several ways of selecting specific values from a column. Nested criteria works the same on flat or hierarchical dfs:
Df_A_slow = Df_A[Df_A['speed']=='Low']
Df_B_slow = Df_B[Df_B['speed']=='Low']
# You can also use df.query(), where you write out your query expression as a string.
# Use inplace=True if you want to change the df, getting rid of the records that don't match your query.
Df_A.query('mouse== "F2_PAFT" and speed != "Low"')
Df_B.query('mouse== "F2_PAFT" and speed != "Low"')
# Look at the documentation for Pandas df.query() and python expressions for more info on this.

# To take a subset of the data WITHOUT the headers/labels, you can use df.xs()
# The syntax is df.xs(value(s)) and in a MI df, df.xs(value,level=#)
# You can only use values that are in an index, so Df_A can only search by the autonumbered index.
DfA_xs = Df_A.xs(5)
DfB_xs = Df_B.xs('Tues',level=1)
# Be careful with xs and give any variables good descriptive names.
# Since the headers are removed, a new df created with xs has no obvious way to know what your selection criteria was.

## RESHAPING DATA

# Ok now let's talk about reshaping and re-arranging data.
# The easiest one is transposing the data: flipping what's on the columns vs the rows.
# That's df.transpose() or just df.T
DfA_T = Df_A.transpose()
DfB_T = Df_B.T
# This is useful since some methods only work on the rows.

# Stacking and unstacking fields is another way to reshape the df.
# Stacking is moving stuff from the columns headers to the rows
# Unstacking is moving stuff from the rows to be column headers
# Both of these really only make sense with a MI, otherwise you can do it but it'll just make a big long series.
print(Df_A.stack())
# See? Not very useful.
# Try unstacking first, since we don't have any dfs with multi-indexes on the columns yet.
# These lines will make a new df where the columns are also a multi-index, with mouse at the highest level.
# The rows will be sorted by the trial number.
B_unstack_by_mouse = Df_B.unstack(['mouse'])
B_unstack_by_mouse=B_unstack_by_mouse.swaplevel(0,1,axis=1)
B_unstack_by_mouse = B_unstack_by_mouse.sort_index(axis=0,level=1)

# Now let's use df.stack() to make a df with a column for each mouse.
# We're moving the rcp/speed/variance to the rows, which is level 1 of the columns' index.
Stacked_by_mouse = B_unstack_by_mouse.stack(level=1)


## TODO: I'll try pivoting later.

## MANIPULATING DATA

# You can add a column by setting it as a variable.
Df_A['added']='New column'
Df_B['added']='New column'

# You can do basic operations with columns.
Df_B['added'] = Df_B['rcp']-2

# TODO: Now comes the stuff I really don't understand yet...
#  a section on apply(), then on iterrows()/itercolumns() and looping if I can figure that out
# Also include .drop and .dropna()

##TODO: Ok just got this working, brain fried, will write up sensible explanation/guide on it later.
Df_B['added']=[loop.findcondition(x, y) for x, y in zip(Df_B['speed'], Df_B['variance'])]
# After I've finished I want to put it in a Jupyter notebook and add some practice exercises like Chris has in the example plots.