from flask import (
    Flask, 
    jsonify
)
import requests
import json
import math
from flask import Flask, request
import pandas as pd
from binance import Client
api_key="cLn6BbpRC8wpE6NIq0Z7ebLkpZez0o8I1X5dEG7EjMvULZPoAlyTc8EmQpaSzv17"
api_secret="i3hUtLdolcx5289Atv9oCTWI4ayntw84p8oWOuXDcnXiq9BPklPW9AOjEYqVjVeT"
client = Client(api_key, api_secret)

# Function that create the app 

    # create and configure the app
app = Flask(__name__)

    # Simple route
@app.route('/')
def index(): 
        return "<h1>Welcome to Geeks for Geeks</h1>"


@app.route('/telweb', methods=['GET','POST'])
def telweb(): 
         
         send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=nemessage3?'

         response = requests.get(send_text)

         return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():

     data = json.loads(request.data)

     if data['passphrase'] != "abcdefgh":
           return jsonify( {
            "code": "error",
            "message": "Bad work"
           }) 
     else:
         side = data['side']
        
         

         if side=="Y":
            try:
                client.futures_create_order(symbol='SANDUSDT', side='SELL', type='MARKET', quantity=100, reduceOnly='true')
            
            except Exception as e:
                print(type(e).__name__, str(e))


         if side=="LONG":
            try:
                client.futures_cancel_all_open_orders(symbol='SANDUSDT')
                print("t1")
            
            except Exception as e:
                print(type(e).__name__, str(e))
                print("e1")
            try:
                cp=client.futures_create_order(symbol='SANDUSDT', side='BUY', type='MARKET', quantity=100, reduceOnly='true')
                print(cp)
                print("t2")
            except Exception as e:
                print(type(e).__name__, str(e))
                print("e2")
            try:
                print("t3")
                df=pd.DataFrame(client.futures_account_balance())
                usdtprice=df[df['asset']=="USDT"]['balance']
                bal=usdtprice.iloc[0]
                bal=float(bal)
                print(bal)

                sandprice=client.futures_symbol_ticker(symbol='SANDUSDT')
                sandprice=float(sandprice['price'])
                print(sandprice)

                qt1=math.floor((bal*2)/sandprice)
                print(qt1)
        
                client.futures_create_order(
                                symbol='SANDUSDT',
                                type='MARKET',  # The price at which you wish to buy/sell, float
                                side='BUY',  # Direction ('BUY' / 'SELL'), string
                                quantity=qt1  # Number of coins you wish to buy / sell, float
                )
            
            except Exception as e:
                print("e3")
                print(type(e).__name__, str(e))    
            



         if side=="SHORT":
            try:
                client.futures_cancel_all_open_orders(symbol='SANDUSDT')
            
            except Exception as e:
                print(type(e).__name__, str(e))
            try:
                 cp1=client.futures_create_order(symbol='SANDUSDT', side='SELL', type='MARKET', quantity=100, reduceOnly='true')
                 print(cp1)
            except Exception as e:
                print(type(e).__name__, str(e))
            try:
                df=pd.DataFrame(client.futures_account_balance())
                usdtprice=df[df['asset']=="USDT"]['balance']
                bal=usdtprice.iloc[0]
                bal=float(bal)
                print(bal)

                sandprice=client.futures_symbol_ticker(symbol='SANDUSDT')
                sandprice=float(sandprice['price'])
                print(sandprice)

                qt2=math.floor((bal*2)/sandprice)
                print(qt2)
                
                client.futures_create_order(
                                symbol='SANDUSDT',
                                type='MARKET',  # The price at which you wish to buy/sell, float
                                side='SELL',  # Direction ('BUY' / 'SELL'), string
                                quantity=qt2  # Number of coins you wish to buy / sell, float
                )
            
            except Exception as e:
                print(type(e).__name__, str(e))   
            
            
       
        
         return jsonify( {
         "code": "error",
         "message": "good work"
        
        
         
        
          }) 
    


if __name__ == '__main__':
    app.run(debug=True)

