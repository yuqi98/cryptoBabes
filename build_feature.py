import pandas as pd
import numpy as np
import groupby_minutes_and_hour
import SMA_EWM
import math
import scipy.fftpack
from math import log
import preprocessing

origin_data = pd.read_csv('original_data.csv')
fisher_transform = []
for x in origin_data['price']:
    fisher = 0.5*log(abs((1+x)/(1-x)))
    fisher_transform.append(fisher)

origin_data['fisher_transform'] = pd.Series(fisher_transform)
origin_data['fft'] = pd.Series(np.fft.fft(origin_data['price']))

origin_data.to_csv('origin_FT_FFT.csv',index=False)

origin_data = pd.read_csv('original_data.csv')

bitdata = preprocessing.preprocess(origin_data)

feature_minute = groupby_minutes_and_hour.minute_feature(bitdata)
feature_hour = groupby_minutes_and_hour.hour_feature(bitdata)

size = 10
coe = [1,2,3,4,5,6,7,8,9,10]

sma_ewm = SMA_EWM.combine(SMA_EWM.cal_SMA(bitdata,size),SMA_EWM.cal_EWM(bitdata,size,coe))

feature_minute.to_csv('feature_minute.csv',index=False)
feature_hour.to_csv('feature_hour.csv',index=False)

sma_ewm.to_csv('sma_ewm.csv',index=False)


