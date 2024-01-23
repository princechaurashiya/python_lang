# Viewing the data : one of the most used method for a quick overview of the dataframe is the head () method. this method returns the headers and a specified number of rows 

# here we will print the 1st 10 rows in the dataframe.
import pandas as pd 
prince = pd.read_csv('homo_sapiens.csv')
print(prince.head(10))

'''
Output:
 Entry ID                 Source Organism Accession Code(s)
0     1A02                             NaN               NaN
1      NaN                    Homo sapiens            Q13469
2      NaN                    Homo sapiens            P01100
3      NaN                    Homo sapiens            P05412
4     1A1M                    Homo sapiens            P01889
5      NaN                    Homo sapiens            P61769
6      NaN  Human immunodeficiency virus 2               NaN
7     1A1N                    Homo sapiens            P01889
8      NaN                    Homo sapiens            P61769
9      NaN  Human immunodeficiency virus 1               NaN

'''

# here we will print the last 10 rows in the dataframe
import pandas as pd
prince = pd.read_csv('homo_sapiens.csv')
print(prince.tail(10))

'''
Output:
      Entry ID  Source Organism   Accession Code(s)
58810      NaN    Homo sapiens            P59768
58811      NaN    Homo sapiens            Q9NXV2
58812     8U83    Homo sapiens            P62873
58813      NaN    Homo sapiens            Q13618
58814      NaN    Homo sapiens            P59768
58815      NaN    Homo sapiens            Q9NXV2
58816     8U84    Homo sapiens            Q9NXV2
58817      NaN    Homo sapiens            Q13618
58818      NaN    Homo sapiens            P62873
58819      NaN    Homo sapiens            P59768


'''

# what if you want the information about the data in the dataframe: via info()
import pandas as pd 
df = pd.read_csv('homo_sapiens.csv')
print(df.info())

'''
Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 58820 entries, 0 to 58819
Data columns (total 3 columns):
 #   Column             Non-Null Count  Dtype 
---  ------             --------------  ----- 
 0   Entry ID           9056 non-null   object
 1   Source Organism    58596 non-null  object
 2   Accession Code(s)  47655 non-null  object
dtypes: object(3)
memory usage: 1.3+ MB
None

'''