import pandas as pd
import json
import requests
from flask import Flask, request, Response


# constants

TOKEN = '1904358878:AAHRNiRgkR113HZpgP3dCjCE4Y8PacdNX4E'

# # Info about the bot
# https://api.telegram.org/bot1904358878:AAHRNiRgkR113HZpgP3dCjCE4Y8PacdNX4E/getMe
#
# # get updates
# https://api.telegram.org/bot1904358878:AAHRNiRgkR113HZpgP3dCjCE4Y8PacdNX4E/getUpdates
#
# # send message
# https://api.telegram.org/bot1904358878:AAHRNiRgkR113HZpgP3dCjCE4Y8PacdNX4E/sendMessage?chat_id=1223001388&text=hi edu-p, im bot

def send_message( chat_id, text ):
    url = 'https://api.telegram.org/bot{}/'.format( TOKEN )
    url = url + 'sendMessage?chat_id={}'.format( chat_id )

    r = requests.post( url, json={'text': text} )

    print( 'Status Code {}'.format( r.status_code ) )

    return None


def load_dataset( store_Id ):
    # loading test dataset
    df10 = pd.read_csv( 'C:/Users/PICHAU/Desktop/AnaliseDeDados/DsEmProd/datasets/test.csv' )
    df_store_raw = pd.read_csv( 'C:/Users/PICHAU/Desktop/AnaliseDeDados/DsEmProd/datasets/store.csv' )

    # merge test dataset + store, pois a gente carregou os resultados mas n os parametros
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store'  )

    # choose especific store for prediction
    df_test = df_test[df_test['Store'].isin( store_Id )]

    # remove closed days
    df_test = df_test[ df_test['Open'] != 0 ]
    df_test = df_test[ ~df_test['Open'].isnull() ] # pegar todas as linhas que nao tem open vazio
    df_test = df_test.drop( 'Id', axis=1 )

    # convert dataframe to json
    data = json.dumps( df_test.to_dict( orient='records' ) )

    return data

def predict( data ):
    # API Call
    url = 'https://prediction-rossmann-v2.herokuapp.com/rossmann/predict'
    header = {'Content-type': 'application/json' }
    data = data

    r = requests.post( url, data=data, headers=header )
    print( 'Status Code {}'.format( r.status_code ) )

    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

    return d1

def parse_message( message ):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    store_id = store_id.replace( '/', '' )

    try:
        store_id = int( store_id )
    except ValueError:
        store_id = 'error'



    return chat_id, store_id

# API initialize ( vamos criar um endpoint que vai transformar a mensagem de texto em um json que nosso modelo consegue trabalhar )
app = Flask( __name__ )

@app.route( '/', methods=['GET', 'POST'] )
def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message( message )

        if store_id != 'error':
            # loading data
            # prediction
            # claculation
            # send message
        else:
            send_message( chat_id, 'Invalid store id' )
            return Response( 'OK', status=200 )

    else:
        return '<h1> Rossmann Telegram Edu-p BOT </h1>'

if __name__ == 'main':
    app.run( host='0.0.0.0', port=5000 )













#
# d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()
#
# for i in range( len( d2 ) ):
#     print( 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format(
#             d2.loc[i, 'store'],
#             d2.loc[i, 'prediction'] ) )
