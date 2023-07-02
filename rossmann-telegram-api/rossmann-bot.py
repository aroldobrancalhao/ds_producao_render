import pandas as pd
import json
import requests

from flask import Flask, Response

TOKEN = '6334256984:AAFvi8mr6ogIgyiRxp8vUIRLBxmN0KGB2P8'

## Info about the Bot
#https://api.telegram.org/bot6334256984:AAFvi8mr6ogIgyiRxp8vUIRLBxmN0KGB2P8/getMe
#
## get update
#https://api.telegram.org/bot6334256984:AAFvi8mr6ogIgyiRxp8vUIRLBxmN0KGB2P8/getUpdates
#
## Webhook
#https://api.telegram.org/bot6334256984:AAFvi8mr6ogIgyiRxp8vUIRLBxmN0KGB2P8/setWebhook?url=

## Webhook
#https://api.telegram.org/bot6007107169:AAEfibx38xpRUW5EP6M90HPFbgCsYURXKGU/setWebhook?url=https://bot-telegram-rossmann-p20y.onrender.com
#
## send message
#https://api.telegram.org/bot6334256984:AAFvi8mr6ogIgyiRxp8vUIRLBxmN0KGB2P8/sendMessage?chat_id=5906683343&text=Hi Aroldo, tudo bem com você!


def send_message( chat_id, text ):
    url = 'https://api.telegram.org/bot{}/'.format( TOKEN )
    url = url + 'sendMessage?chat_id={}'.format( chat_id )
    
    r = requests.post( url, json={'text': text })
    print('Status code {}'. format( r.status_code ))
    
    return None
    


def load_dataset( store_id ):
    # loading test dataset
    df10 = pd.read_csv( '/Users/arold/anaconda3/envs/datascienceemproducao/data_science_producao/data/test.csv' )
    df_store_raw = pd.read_csv( '/Users/arold/anaconda3/envs/datascienceemproducao/data_science_producao/data/store.csv' )


    # merge test dataset + store
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

    # choose store for prediction
    df_test = df_test[df_test['Store'] == store_id] 

    if not df_test.empty:
        # remove closed days
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop( 'Id', axis=1 )

        # convert Dataframe to json
        data = json.dumps( df_test.to_dict( orient='records' ) )
    else:
        data = 'error'

    return data

def predict( data ):
    # API Call
    url = 'https://previsao-vendas-rossmann-adaw.onrender.com/rossmann/predict'
    header = {'Content-type': 'application/json' }
    data = data

    r = requests.post( url, data=data, headers=header )
    print( 'Status Code {}'.format( r.status_code ) )

    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

    return d1

def parse_message( message ):
    chat_id = message['message']['chat']['id']
    store_id = message['mesage']['text']

    store_id = store_id.replace( '/', '' )

    try:
        store_id = int( store_id )

    except ValueError:
        
        store_id = 'error'

    return cha_id, store_id

# API inicialize
app = Flask(__name__)

@app.route( '/', methods=['GET', 'POST'] )
def index():
    if requests.method =='POST':
        message = requests.get_json()

        chat_id, store_id = parse_message( message )

        if store_id != 'error':
            #load data
            data = load_dataset( store_id )

            if data != 'error':
                #prediction
                d1 = predict( data )

                # calculation
                d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

                #send message             
                msg = 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( d2.loc['store'].values[0], d2.loc['prediction'].values[0] ) 

                send_message ( chat_id, msg )
                return Response( 'Ok', status=200 )
                
            else:
                send_message( chat_id, 'Store Not Available' )
                return Response( 'Ok', status=200 )

        else:
            send_message( chat_id, 'Store ID is Wrong' )
            return Response( 'ok', status=200 )

    else:
        return '<h1> Rossmann Telegram BOT </h1>'

if __name__ == '__main':
    app.run( host='0.0.0.0', port=5000 )

