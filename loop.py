import pandas as pd

##NOTES: Want to use this to mess around with looping through the rows of a dataframe later.

Df_A = pd.read_csv('Flat.csv')
Df_B=Df_A.set_index(['mouse','day','trial'])

speed= [0.25,0.1,0.25]
varience= 0.1
# for sp in speed:
#     if sp == 0.25:
#         # if varience == 0.0001:
#         #     condition = 1
#         # elif varience == 0.01:
#         #     condition = 2
#         # elif varience == 0.1:
#         #     condition = 3
#         # else:
#         #     condition = 'unknown varience'
#     else:
#         condition = 'nah'


def findcondition(speed, varience):
    if speed == 'Low':
        if varience == 'Low':
            condition = 1
        elif varience == 'Medium':
            condition = 2
        elif varience == 'High':
            condition = 3
        else:
            condition = 'unknown varience'
    else:
        condition = 'nah'
    print(condition)
    return condition

# speedlist = iter(Df_B['speed'],Df_B['variance'])
#
# for speed,var in speedlist:
#     loop.findcondition(speed,0.0001)

# ConditionDict = {}
# for row in Df_A.itertuples(name="Condition"):
#     print(row)
#     print(row.speed)
#     if row.speed == "Low" and row.variance=="Low":
#         print("you got it!")
#         cond = 1
#         ConditionDict.update({row.speed : cond})
#     elif row.speed == "Med" and row.variance=="Low":
#         print("It's the second one")
#         cond = 0
#         ConditionDict[row.Index]= cond
#     else:
#         cond = 3
#         row = row._replace(condition = 3)
#         print("Nothing yet")
#     print(row, ConditionDict)