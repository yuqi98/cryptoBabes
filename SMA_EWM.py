import pandas as pd
import numpy as np


def cal_SMA(bitdata,size):
    result = np.array([])

    price = bitdata['price']

    for i in range(len(price)-size+1):
        result = np.append(result,np.sum(price[i:i+size])/size)

    result = pd.DataFrame(result.reshape(-1,1))
    result.columns = ['SMA']
    return result


def cal_EWM(bitdata,size,coe):
    result = np.array([])

    price = bitdata['price']
    
    for i in range(len(price)-size):
        result = np.append(result,np.sum(price[i:i+size]*coe)/(np.sum(coe)))

    result = pd.DataFrame(result.reshape(-1,1))
    result.columns = ['EWM']
    return result

def combine(SMA_list,EWM_list):
    result = SMA_list
    result = result.join(EWM_list)
    return result

