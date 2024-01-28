# Data in a wrong format: to fix this problem m there are 2 ways: 1st:- removing the rows, 2nd:- convert all the cells in the same format.

import pandas as pd 
prince = pd.read_csv("dirtydata.csv")
print(prince.to_string())

# now let's try to convert all the cells in the date column into dates.via to_datetime
import pandas as pd 
rince = pd.read_csv('dirtydata.csv')
rince["Date"] =pd.to_datetime(rince['Date'])
print(rince.to_string())

# Here now we will remove the rows with a NULL value in the 'date' column.
import pandas as pd 
prince = pd.read_csv('dirtydata.csv')
prince ['Date'] = pd.to_datetime(prince['Date'])
prince.dropna(subset=['Date'], inplace=True)
print(prince.to_string())