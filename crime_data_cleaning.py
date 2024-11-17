

import numpy as np
import pandas as pd
import seaborn ,matplotlib.pyplot as plt
crime = pd.read_csv("~/Documents/py/training/cleaning/Crime_Data_from_2020_to_Present.csv")
# before importing the data i did the following using excel
# i dropped duplicated values using excel (more than 2k rows )
# i dropped some columns that has too many null values more than 65 %
crime.replace("", np.nan, inplace=True)

print(crime.shape)
crime['TIME OCC'] = crime['TIME OCC'].astype(str).str.zfill(4)
crime['TIME OCC'] = pd.to_datetime(crime['TIME OCC'], format='%H%M', errors='coerce').dt.time
#crime['Date Rptd'] = pd.to_datetime(crime['Date Rptd'],errors='coerce')
#crime['DATE OCC'] = pd.to_datetime(crime['DATE OCC'],errors='coerce')
crime['Vict Age'] = crime['Vict Age'].apply(lambda x : np.nan if x <= 0 else x)
crime['Vict Sex'] = crime['Vict Sex'].replace({'X': np.nan, 'H': np.nan,'-' : np.nan})
crime['Date Rptd'] = crime['Date Rptd'].str.replace(' 12:00:00 AM','')
crime['Date Rptd'] = pd.to_datetime(crime['Date Rptd'])
crime['DATE OCC'] = crime['DATE OCC'].str.replace(' 12:00:00 AM','')
crime['DATE OCC'] =pd.to_datetime(crime['DATE OCC'] )
#df_count=crime['Vict Sex'].value_counts()
df_null =crime.isnull().sum()
#print(df_null)
#crime.to_csv("~/Documents/py/training/cleaning/cleaned_data.csv",index = False)
crime.info()




