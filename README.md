# cryptoBabes

Team members: Yuqi Zhang, Bassim Eledath, Surbhi Gupta

Contributions:

1. Data preprocessing (Saved as preprocessing.py) -  
Bassim, Yuqi (formatting date and splitting columns)
Description: the step changing MTS to actually date use the code provided by teacher that saved as dateandtime.py,
             the rest just using split.

2. Feature engineering - 
Yuqi - open, close, high, low, average (Saved as groupby_minutes_and_hour.py)
     - sma, ewm (Saved as SMA_EWM.py)
Bassim - Fisher equation, fast fourier transform (Saved in the final python script, no separate file)

3. Python script architecture (Saved as build_feature.py) - 
Yuqi  - compiled all functions to a single python script
Description: build_feature.py import the preprocessing.py, groupby_minutes_and_hour.py, SMA_EWM.py, and create four new csv file:
origin_FT_FFT.csv  -- the original data adding two columns of features : Fisher equation, fast fourier transform
feature_minute.csv  -- open, close, high, low, average of each minute
feature_hour.csv  -- open, close, high, low, average of each hour
sma_ewm.csv -- sma and ewm data based on the preprocessed data with dates

4. 4 coins pair extract -
Yuqi - use get_trades.py to extract 4 coins pair, saved as tBTCUSD_trades.parquet, tEOSUSD_trades.parquet, 


5. Plotting - 
Yuqi - plotted using interactive candlestick graphs via Plotly (saved as plotly.ipynb)

Surbhi - plotted based on price and time, and feature of sell

Bassim - created a web framework using dash to present interactive plots of coin pairs. Deployment of web app done by Yuqi. 

Access it using this link -- https://dash-bitcoin.herokuapp.com/

5. Twitter sentiment analysis - 
Bassim

6. Reddit bitcoin thread sentiment analysis - 
Bassim


