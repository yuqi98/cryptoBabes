import pandas as pd
import numpy as np
import dateandtime

def preprocess(data):
   data.drop(['exchange','symbol'],axis=1,inplace=True)
   data['date'] = data.apply((lambda x: pd.Series({'date':dateandtime.convert_dates(x['date'])})), axis = 1)
   date = [str(x) for x in data['date']]
   date_new = [x.split() for x in date]
   data['date'] = pd.Series([x[0] for x in date_new])
   data['time'] = pd.Series([x[1] for x in date_new])
   time_new = [x.split(':') for x in data['time']]
   data['hours'] = pd.Series([x[0] for x in time_new])
   data['minutes'] = pd.Series([x[1] for x in time_new])
   data['seconds'] = pd.Series([x[2] for x in time_new])
   data['hour_minute'] = pd.Series([(x[0] + ':' + x[1]) for x in time_new])
   return data
