import pandas as pd
import json
import requests

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

pd.DataFrame( r.json(), columns=r.json()[0].keys() )

d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

for i in range( len( d2 ) ):
    print( 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format(
            d2.loc[i, 'store'],
            d2.loc[i, 'prediction'] ) )
