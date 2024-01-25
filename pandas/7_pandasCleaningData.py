# cleaning data: It means fixing the bad data in your data set. Bad data could be: empty cell , data in a wrong format , duplicate data and wrong data 
# Empty cell: it will give you wrong result always, we will have to remove the rows always that contain the bad data.

#Loading and reading the original dataframe
import pandas as pd
prince = pd.read_csv("dirtydata.csv")
print(prince.to_string())


# Here we will return a new data frame with no empty cell.

import pandas as pd
prince = pd.read_csv("dirtydata.csv")
princenew = prince.dropna()
print(princenew.to_string())

# if at any case you want to change the original dataframe, than use the inplace=True argument. it will remove the rows containing the NULL(NaN) values.
import pandas as pd 
prince = pd.read_csv("dirtydata.csv")
prince.dropna(inplace=True)
print(prince.to_string())

# replacing the empty value: we will use the fillna() method which will allow us to replace the empty cell with a value.

import pandas as pd 
sharad = pd.read_csv('dirtydata.csv')
sharad.fillna(130, inplace=True)
print(sharad.to_string)

# to replace only the empty value for one column, you need to specify the column name.
import pandas as pd
prince = pd.read_csv('dirtydata.csv')
prince["Calories"].fillna(130,inplace= True)
print(prince.to_string)

#here we can also replace the empty cell using mean (), median() or mode().
#calculate the MEAN and replace the empty values with it .
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
x = prince['Calories'].mean()
prince['Calories'].fillna(x,inplace=True)
print(prince.to_string())

# calculate the MEDIAN and replace any empty values in it.:
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
x = prince['Calories'].median()
prince['Calories'].fillna(x,inplace=True)
print(prince.to_string())

# calculate the MODE and replace the empty cell with it.:
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
x = prince['Calories'].mode()[0]
prince['Calories'].fillna(x,inplace=True)
print(prince.to_string())
