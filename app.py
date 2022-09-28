from flask import (
    Flask, 
    jsonify
)
import datetime
import requests
import json
import math
from flask import Flask, request
import pandas as pd
from binance import Client
api_key="cLn6BbpRC8wpE6NIq0Z7ebLkpZez0o8I1X5dEG7EjMvULZPoAlyTc8EmQpaSzv17"
api_secret="i3hUtLdolcx5289Atv9oCTWI4ayntw84p8oWOuXDcnXiq9BPklPW9AOjEYqVjVeT"
client = Client(api_key, api_secret)
global overall
overall=0

# Function that create the app 

    # create and configure the app
app = Flask(__name__)

    # Simple route
@app.route('/')
def index(): 
        return "<h1>test1</h1>"


@app.route('/telweb', methods=['GET','POST'])
def telweb(): 
         side='buy'
         qtsy=str(109829)
         send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=TESTMESSAGE AS SIDE?' +side +" WITH QUANTITY " +qtsy

         response = requests.get(send_text)

         return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
     

     data = json.loads(request.data)

     if data['passphrase'] == "ramp":
           return jsonify( {
            "code": "error",
            "message": "good ramp"
           }) 
          
     elif data['passphrase']=="oldcode":
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
        
                cp6=client.futures_create_order(
                                symbol='SANDUSDT',
                                type='MARKET',  # The price at which you wish to buy/sell, float
                                side='BUY',  # Direction ('BUY' / 'SELL'), string
                                quantity=qt1  # Number of coins you wish to buy / sell, float
                )
                print(cp6['updateTime'])
                timestamp = datetime.datetime.fromtimestamp((cp6['updateTime']/1000))
                print(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                btms=str(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=ORDEREXECUTEDAT' +btms
                response=requests.get(send_text)
                return response.json()
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
                
                cp5=client.futures_create_order(
                                symbol='SANDUSDT',
                                type='MARKET',  # The price at which you wish to buy/sell, float
                                side='SELL',  # Direction ('BUY' / 'SELL'), string
                                quantity=qt2  # Number of coins you wish to buy / sell, float
                )
                print(cp5)
                print(cp5['updateTime'])
                timestamp = datetime.datetime.fromtimestamp((cp5['updateTime']/1000))
                print(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                btms=str(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=ORDEREXECUTEDAT' +btms+side
                response=requests.get(send_text)
                return response.json()
            except Exception as e:
                print(type(e).__name__, str(e))   
            
            
       
        
         return jsonify( {
         "code": "error",
         "message": "good work"
        
        
         
        
          }) 

     elif data['passphrase']=="newcode":
         side = data['side']
         pr = data['price']
         global overall

         if side=="Y":
            try:
                client.futures_create_order(symbol='SANDUSDT', side='SELL',positionSide="BOTH",type='STOP_MARKET',timeInForce= "GTE_GTC",quantity=6,reduceOnly='false',stopPrice=0.8920)
            
            except Exception as e:
                print(type(e).__name__, str(e))
            try:
                client.futures_create_order(symbol='SANDUSDT', side='SELL',positionSide="BOTH", type='LIMIT', quantity=12, reduceOnly='false',timeInForce= "GTE_GTC",price=0.8920)
            
            except Exception as e:
                print(type(e).__name__, str(e))    

         if side=="test":
            
            try:
                print("2")
                
                result = client.futures_get_order(symbol='SANDUSDT',orderId='11333832504')
                print("3")
                print(result)
            except Exception as e:
                print(type(e).__name__, str(e))   


         if side=="LONG":
            try:
                ap=client.futures_create_order(symbol='SANDUSDT', side='BUY',positionSide="BOTH",type='MARKET',quantity=115,reduceOnly='false')
                print(ap)
                result = client.futures_get_order(symbol='SANDUSDT',orderId=ap['orderId'])
                
                pr=float(pr)
                avgp=float(result['avgPrice'])
                print(pr)
                print(avgp)
                chang=pr - avgp
                overall=overall + chang
                print(chang)
                print(overall)
                send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=EXECUTED WITH SIDE ' +result['side'] +" WITH QUANTITY " +result['executedQty']+" WITH PRICE " +result['avgPrice']+" BUT ACTUAL PRICE " +str(pr)+" SO CHANGE " +str(chang)+" AND OVERALL CHANGE " +str(overall)
                response = requests.get(send_text)
                print("ok")
            except Exception as e:
                print(type(e).__name__, str(e))
                
         if side=="SHORT":
            try:
                ap=client.futures_create_order(symbol='SANDUSDT', side='SELL',positionSide="BOTH",type='MARKET',quantity=115,reduceOnly='false')
                print(ap)
                result = client.futures_get_order(symbol='SANDUSDT',orderId=ap['orderId'])
                pr=float(pr)
                avgp=float(result['avgPrice'])
                print(pr)
                print(avgp)
                chang=avgp - pr
                print(overall)
                overall=overall + chang
                print(chang)
                print(overall)
                send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=EXECUTED WITH SIDE ' +result['side'] +" WITH QUANTITY " +result['executedQty']+" WITH PRICE " +result['avgPrice']+" BUT ACTUAL PRICE " +str(pr)+" SO CHANGE " +str(chang)+" AND OVERALL CHANGE " +str(overall)
                response = requests.get(send_text)
                print("ok")
            except Exception as e:
                print(type(e).__name__, str(e))  



         if side=="LONG_1":
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
        
                cp6=client.futures_create_order(
                                symbol='SANDUSDT',
                                type='MARKET',  # The price at which you wish to buy/sell, float
                                side='BUY',  # Direction ('BUY' / 'SELL'), string
                                quantity=qt1  # Number of coins you wish to buy / sell, float
                )
                print(cp6['updateTime'])
                timestamp = datetime.datetime.fromtimestamp((cp6['updateTime']/1000))
                print(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                btms=str(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=ORDEREXECUTEDAT' +btms
                response=requests.get(send_text)
                return response.json()
            except Exception as e:
                print("e3")
                print(type(e).__name__, str(e))    
            



         if side=="SHORT_1":
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
                
                cp5=client.futures_create_order(
                                symbol='SANDUSDT',
                                type='MARKET',  # The price at which you wish to buy/sell, float
                                side='SELL',  # Direction ('BUY' / 'SELL'), string
                                quantity=qt2  # Number of coins you wish to buy / sell, float
                )
                print(cp5)
                print(cp5['updateTime'])
                timestamp = datetime.datetime.fromtimestamp((cp5['updateTime']/1000))
                print(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                btms=str(timestamp.strftime('%d-%m-%Y %H:%M:%S')) 
                send_text = 'https://api.telegram.org/bot5064252177:AAGlwwtDi4B7TiwB4LTDyPvtYNeGIKJDlHk/sendMessage?chat_id=998041732&parse_mode=Markdown&text=ORDEREXECUTEDAT' +btms+side
                response=requests.get(send_text)
                return response.json()
            except Exception as e:
                print(type(e).__name__, str(e))   
            
            
       
        
         return jsonify( {
         "code": "error",
         "message": "good work"
        
        
         
        
          }) 

    
    




if __name__ == '__main__':
    
    app.run(debug=True)

