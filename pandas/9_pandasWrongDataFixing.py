# Wrong Data: its only a wrong data

#loading and reading the original dataframe
import pandas as pd
prince = pd.read_csv('dirtydata.csv')
print(prince.to_string())

# here we will set "Duration"= row 7:
import pandas as pd
prince = pd.read_csv('dirtydata.csv')
prince.loc[7,'Duration'] = 45
print(prince.to_string)

# for larger data set:now here we will loop through all the values in "Duration" columnm. if the value is higher than  120 then set it to 120.
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
for i in prince.index:
    if prince.loc[i, "Duration"] > 120:
        prince.loc[i, "Duration"] = 120
print(prince.to_string())

# you can also remove the rows for wrong data in larger dataset
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
for i in prince.index:
    if prince.loc[i, "Duration"] > 120:
        prince.drop(i, inplace = True)
print(prince.to_string())
