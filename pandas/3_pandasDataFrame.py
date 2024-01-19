# DataFrame: it is a 3D data structure like a 2D array with table inl. rows and columns.
import pandas as pd
data ={"cal":[420,380,390],"dur":[50,40,45]}
prince = pd.DataFrame(data)
print(prince)

'''
Output:
   cal  dur
0  420   50
1  380   40
2  390   45
'''

# Locate row: pandas use the loc attribute to return one or more specified row.
import pandas as pd
data = {"cal":[420,380,390],"dur":[50,40,45]}
prince = pd.DataFrame(data)
print(prince.loc[0])

'''
Output:
cal    420
dur     50
Name: 0, dtype: int64
'''

# #Example of returning row 0 and 1
import pandas as pd
data = {"cal":[420,380,390],"dur":[50,40,45]}
prince = pd.DataFrame(data)
print(prince.loc[[0,1]])

'''
Output:
   cal  dur
0  420   50
1  380   40
'''

# Name Index: with the index arg, you can name your own index.
import pandas as pd
data ={"cal":[420,380,390],"dur":[50,40,45]}
prince = pd.DataFrame(data,index = ["day1", "day2", "day3"])
print(prince)

'''
Output:
      cal  dur
day1  420   50
day2  380   40
day3  390   45
'''

# locate the named index:
import pandas as pd 
data = {"cal":[420,380,390],"dur":[50,40,45]}
prince = pd.DataFrame(data,index=["day1","day2","day3"])
print(prince.loc["day2"])

'''
Output:
cal    380
dur     40
Name: day2, dtype: int64

'''

#for output in dataframe
import pandas as pd 
data = {"cal":[420,380,390],"dur":[50,40,45]}
prince = pd.DataFrame(data,index=["day1","day2","day3"])
print(prince.loc[["day1","day2"]])

'''
Oputput:
      cal  dur
day1  420   50
day2  380   40

'''

# Load the data from the csv file into DataFrame i.e data.csv
import pandas as pd
fileload = pd.read_csv("homo_sapiens.csv")
print(fileload.loc[[0]])

'''
Output:
  Entry ID Source Organism Accession Code(s)
0     1A02             NaN               NaN

'''