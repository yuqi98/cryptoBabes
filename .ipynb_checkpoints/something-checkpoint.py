import pandas as pd
import numpy as np
import dateandtime

def preprocess(data):
    data['MTS'] = data.apply((lambda x: pd.Series({'MTS':dateandtime.convert_dates(x['MTS'])})), axis = 1)
    date = [str(x) for x in data['MTS']]
    date_new = [x.split() for x in date]
    data['MTS'] = pd.Series([x[0] for x in date_new])
    data['TIME'] = pd.Series([x[1] for x in date_new])
    time_new = [x.split(':') for x in data['time']]
    data['HOURS'] = pd.Series([x[0] for x in time_new])
    data['MINUTES'] = pd.Series([x[1] for x in time_new])
    data['SECONDS'] = pd.Series([x[2] for x in time_new])
    data['HOUR_MINUTE'] = pd.Series([(x[0] + ':' + x[1]) for x in time_new])
    return data
   
  