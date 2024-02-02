# removing the duplicate values: 1st you need to discover the duplicate values via duplicated() method.

# loading and reading the original dataframe
import pandas as pd
prince = pd.read_csv('dirtydata.csv')
print(prince.to_string)

# returns True for every row that is duplicate otherwise return false:
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
print(prince.duplicated())

#removing the duplicate from the datat set. via drop_duplicates()
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
prince.drop_duplicates(inplace=True)
print(prince.to_string)