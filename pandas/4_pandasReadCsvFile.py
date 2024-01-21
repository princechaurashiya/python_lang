#read csv files: (comma seperated file ) it is a simple way to store the big and bigest data sets. csv files contains plain text.

#Loading the .csv into a DataFrame with to_string
import pandas as pd
df = pd.read_csv('homo_sapiens.csv')
print(df.to_string())

'''
Not giving output, because output is so large.
'''

# Loading the .csv into a DataFrame without to_string\
import pandas as pd
df = pd.read_csv('homo_sapiens.csv')
print(df)
'''
Output:
      Entry ID Source Organism Accession Code(s)
0         1A02             NaN               NaN
1          NaN    Homo sapiens            Q13469
2          NaN    Homo sapiens            P01100
3          NaN    Homo sapiens            P05412
4         1A1M    Homo sapiens            P01889
...        ...             ...               ...
58815      NaN    Homo sapiens            Q9NXV2
58816     8U84    Homo sapiens            Q9NXV2
58817      NaN    Homo sapiens            Q13618
58818      NaN    Homo sapiens            P62873
58819      NaN    Homo sapiens            P59768

[58820 rows x 3 columns]

'''

# max_rows : you can check your system's maximum rows with:
import pandas as pd
print (pd.options.display.max_rows)

'''
Output:
60
'''

# Yes, we can increase the maximum number of rows to display the entire dataframe.
import pandas as pd
pd.options.display.max_rows = 999
df = pd.read_csv('homo_sapiens.csv')
print(df)

'''
Not giving output, because output is so large.
'''