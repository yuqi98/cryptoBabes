import pandas as pd
import numpy as np


def minute_feature(bitdata):
    index_minute = bitdata.groupby(['date','hours','minutes']).agg({'hour_minute': lambda x: x.iloc[0]})
    max_list = bitdata.groupby(['date','hours','minutes']).agg({'price': np.max})
    max_list.columns=['high']
    min_list = bitdata.groupby(['date','hours','minutes']).agg({'price': np.min})
    min_list.columns=['low']
    average_list = bitdata.groupby(['date','hours','minutes']).agg({'price': np.average})
    average_list.columns = ['average']
    open_list = bitdata.groupby(['date','hours','minutes']).agg({'price': lambda x: x.iloc[0]})
    open_list.columns=['open']
    close_list = bitdata.groupby(['date','hours','minutes']).agg({'price': lambda x: x.iloc[-1]})
    close_list.columns=['close']
    result = index_minute
    result = result.join(max_list['high'])
    result = result.join(min_list['low'])
    result = result.join(average_list['average'])
    result = result.join(open_list['open'])
    result = result.join(close_list['close'])
    return result


def hour_feature(bitdata):
    index_minute = bitdata.groupby(['date','hours']).agg({'hours': lambda x: x.iloc[0]})
    max_list = bitdata.groupby(['date','hours']).agg({'price': np.max})
    max_list.columns=['high']
    min_list = bitdata.groupby(['date','hours']).agg({'price': np.min})
    min_list.columns=['low']
    average_list = bitdata.groupby(['date','hours']).agg({'price': np.average})
    average_list.columns = ['average']
    open_list = bitdata.groupby(['date','hours']).agg({'price': lambda x: x.iloc[0]})
    open_list.columns=['open']
    close_list = bitdata.groupby(['date','hours']).agg({'price': lambda x: x.iloc[-1]})
    close_list.columns=['close']
 
    result = index_minute
    result = result.join(max_list['high'])
    result = result.join(min_list['low'])
    result = result.join(average_list['average'])
    result = result.join(open_list['open'])
    result = result.join(close_list['close'])
 
    return result


