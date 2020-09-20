import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

df1 = df
''' Some values in the the FlightNumber column are missing. These numbers are
meant to increase by 10 with each row so 10055 and 10075 need to be put in
place. Fill in these missing numbers and make the column an integer column
(instead of a float column).'''


x,y = df1.FlightNumber.loc[[0]].values[0]+10 , df1.FlightNumber.loc[[2]].values[0]+10
df1.FlightNumber.loc[[1]] = df1.FlightNumber.loc[[1]].fillna(x)
df1.FlightNumber.loc[[3]] = df1.FlightNumber.loc[[3]].fillna(y)

#converting float to int

df1.FlightNumber = df1.FlightNumber.astype(int)

df1

'''The From_To column would be better as two separate columns! Split each
string on the underscore delimiter _ to give a new temporary DataFrame with
the correct values. Assign the correct column names to this temporary
DataFrame.'''

df1_temp = df1.From_To.str.split("_", expand = True)
df1_temp.columns = ["From", "To"]
df1_temp

'''Notice how the capitalisation of the city names is all mixed up in this
temporary DataFrame. Standardise the strings so that only the first letter is
uppercase (e.g. "londON" should become "London".)'''

df1_temp.From = df_temp.From.str.title()
df1_temp.To = df_temp.To.str.title()
df1_temp

''' Delete the From_To column from df and attach the temporary DataFrame
from the previous questions.'''

df1 = df1.drop(["From_To"], axis = 1).join(df1_temp)
df1


''' 5. In the RecentDelays column, the values have been entered into the
DataFrame as a list. We would like each first value in its own column, each

second value in its own column, and so on. If there isn't an Nth value, the value
should be NaN.
Expand the Series of lists into a DataFrame named delays, rename the columns
delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
with delays.'''

df1_delay = pd.DataFrame(df1['RecentDelays'].values.tolist())
df1_delay.columns = ["delay_{}".format(n) for n in range(1, len(df1_delay.columns)+1)]
df1_delay

df1 = df1.drop(['RecentDelays'], axis = 1).join(df1_delay)
df1
