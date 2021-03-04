import requests
import numpy as np
r=requests.get('https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?api_key=pkoRGGy2vknqjypPyQuw&start_date=2017-01-01&end_date=2017-12-31')
res=r.json()
datas=res['dataset']['data']
open_price=[]
high_price=[]
low_price=[]
closing_price=[]
trading_volume=[]
for data in datas:
    if data[1] is None:
        data[1]=0
        open_price.append(data[1])
        high_price.append(data[2])
        low_price.append(data[3])
        closing_price.append(data[4])
        trading_volume.append(data[6])
    else:
        open_price.append(data[1])
        high_price.append(data[2])
        low_price.append(data[3])
        closing_price.append(data[4])
        trading_volume.append(data[6])
        
max_open_price=max(open_price)
min_open_price=min(x for x in open_price if x!=0)
print('2017 highest open price is: ${}.'.format(max_open_price))
print('2017 lowest open price is: ${}.'.format(min_open_price))
daily_change=(round((x1-x2),2) for x1,x2 in zip(high_price,low_price))

print('2017 largest daily change is ${}: ' .format(max(list(daily_change))))
print('2017 largest change betwen any two days is ${}: ' .format(max(closing_price)-min(closing_price)))
print('2017 average trading volume is : {} '.format(round(sum(trading_volume)/len(trading_volume)),0))
    
