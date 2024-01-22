# JSON: Bif data sets are mormally stored and extracted as JSON. JSON is a plain text, but it has a formate of an object.

# Loading the JOSN into a dataframe
import pandas as pd 
prince = pd.read_json('data.js')
print(prince.to_string())

'''
 Duration  pulse
0        40    110
1        45    118
2        50    120
3        55    130
4        60    139
5        65    140

'''

# Dictionary as a JSON: if you JSON code is not in a file , but in a python dictionary, then you can do all below:
import pandas as pd 
data = {"Duration":{
             "0":60,
             "1":65,
             "2":70,
             "3":75,
             "4":79,
             "5":80
        },
        "pulses":
        {   "0":111,
            "1":147,
            "2":126,
            "3":145,
            "4":127,
            "5":146
         },
          "maxpulses":
        {   "0":211,
            "1":247,
            "2":226,
            "3":145,
            "4":227,
            "5":246
         },
         "calories":{
            "0":411.3,
            "1":447.8,
            "2":426.4,
            "3":445.6,
            "4":427.6,
            "5":446.2
         }
         }
prince = pd.DataFrame(data)
print(prince)

'''
   Duration  pulses  maxpulses  calories
0        60     111        211     411.3
1        65     147        247     447.8
2        70     126        226     426.4
3        75     145        145     445.6
4        79     127        227     427.6
5        80     146        246     446.2

'''
# what if you want the information about the data in the dataframe: via info()
import pandas as pd 
df = pd.read_json('data.js')
print(df.info())

'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 6 entries, 0 to 5
Data columns (total 2 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  6 non-null      int64
 1   pulse     6 non-null      int64
dtypes: int64(2)
memory usage: 144.0 bytes
None

'''
