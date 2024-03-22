#  A Pandas series is like a coloumn in a table . it is 1D array 
#  which holds data of any type.

#Here we will create a simple pandas series.
import pandas as pd 
prince = [1,7,2]
princenew = pd.Series(prince)
print(princenew)

#labeling - lavel can be  use to access a specified value.
import pandas as pd 
prince = [1,7,2,]
princenew = pd.Series(prince)
print(princenew[0])

# With Create label you can create your own name labels.
import pandas as pd 
prince = [1,7,2,]
princenew = pd.Series(prince,index = ["x","y","z"])
print(princenew)

#labeling - lavel can be  use to access a specified 
#value.(After creating own lable)
import pandas as pd 
prince = [1,7,2,]
princenew = pd.Series(prince,index = ["x","y","z"])
print(princenew["x"])

# you can also use a key or value object like a dictionary , 
# when creating a series.

# Here we will create a simple pandas series from a dictionary.
import pandas as pd 
cal = {"day1":420, "day2":380, "day3":390}
princenew = pd.Series(cal)
print(princenew)

# Now we will create a series using only data from day1 and day2
import pandas as pd 
cal = {"day1":420, "day2":380, "day3":390}
result = pd.Series(cal,index =["day1","day2"])
print(result)

# DataFrame: Data sets in pandas are usually multidimentinal tabes ,, and they are called DataFrame 
# Series are like a columns and dataframes is the whole table.

# we will now create a dataframe from 2 series.
import pandas as pd 
prince = {"cal":[420,380,390], "duration":[50,40,45]}
princenew = pd.DataFrame(prince)
print(princenew)