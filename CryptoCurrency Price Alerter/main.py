import requests
import keys
import pandas as pd
from time import sleep

def get_crypto_rates(base_currency='EUR',assets='BTC,ETC,XRP'):
    url = 'https://api.nomics.com/v1/currencies/ticker'

    payload = {'key':keys.NOMICS_API_KEY, 'convert': base_currency, 'ids': assets, 'interval': '1d'}
    response = requests.get(url, params=payload)
    data = response.json()

    crypto_currency, crypto_price, crypto_timestamp = [], [], []

    for assets in data:
        crypto_currency.append(assets['currency'])
        crypto_price.append(assets['price'])
        crypto_timestamp.append(assets['price_timestamp'])

    raw_data = {
        'Assets' : crypto_currency,
        'Rates' : crypto_price,
        'Timestamp' : crypto_timestamp
    }

    df = pd.DataFrame(raw_data)
    return df

def set_alert(dataframe, assets, alert_high):
    crypto_value = float(dataframe[dataframe['Assets'] == assets]['Rates'].item())

    details = f'{assets} : {crypto_value}, Target : {alert_high}'

    if crypto_value >= alert_high:
        print(details + ' << TARGET VALUE REACHED!!')

    else:
        print(details)


loop = 0
while True:
    print(f'----------------------- ({loop}) -----------------------')

    try: 
        df = get_crypto_rates(assets='BTC,ETC,XRP,DOT')
        set_alert(df, 'BTC', 50250.50)            
        set_alert(df, 'ETH', 1800.30)            
        set_alert(df, 'XRP', 0.870) 
        set_alert(df, 'DOT', 100) 

    except Exception as e:
        print('Couldn\'t retrive the data... Trying again.')

        loop += 1
        sleep(30)


