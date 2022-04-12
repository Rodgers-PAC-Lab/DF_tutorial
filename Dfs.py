import pandas as pd
##NOTES: In this file, I was playing around with different ways to transform the flat dataframe into a heirarchical multi-index. Went down a few wrong turns and moved to Df_w_multis.

#I want to learn how the levels on a dataframe affect the different methods and properties and what you can and can't do with them.
#To do this, I'm going to make several dataframes that are identical except for their levels and indexes, patterned like our trial data.

#Df_A: totally flat. It will create an autonumbered index,called RangeIndex
Df_A = pd.read_csv('Flat.csv')
print('Df_A',Df_A)

#Makes a Pandas series named 'mouse' from Df_A, with an autonumbered RangeIndex
mouse_series = Df_A['mouse']
print('Mouse series',mouse_series)



# Df_A.loc[[mouse or mouse name stuff],:]
# The above doesn't work because 'mouse' is not an index. Apparently loc requires an index.
# But just for kicks, let's try getting the location:
#Df_A.get_loc('M1_PAFT')
#Errors saying Dataframe object has no attribute get_loc

# idx=pd.MultiIndex(
#     levels=[[Df_A['mouse'].unique()],[Df_A['day'].unique()]],
#     codes=[[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]]
# )
Df_B=Df_A
Df_B=Df_B.set_index(['mouse','day'])

idx =pd.MultiIndex(
    levels=[['M1','M2','M3'],[Df_A['day'].unique().tolist()]],
    codes=[[0,0,1,1,2,2], [0,1,0,1,0,1]]
)
#Df_B= Df_A.set_levels=[['M1_PAFT','M2_PAFT','M3_PAFT','M4_PAFT','F1_PAFT', 'F3_PAFT','F2_PAFT', 'F4_PAFT'],[]]
#Df_B = pd.read_csv('Stacked.csv')
#Df_B = pd.DataFrame(data=Df_A,index=)
#Df_B=pd.MultiIndex.from_frame(Df_B)

#print('Df_B',Df_B)