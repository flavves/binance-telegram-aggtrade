

import unicorn_binance_websocket_api
import json

from datetime import datetime
from binance.enums import *
from binance.client import Client
from binance.client import Client
import threading
from datetime import datetime
import pandas as pd
global client
client = Client()
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import time
import json
import pandas as pd



try:
    client = Client()
    
    semboller=[]
    
    
    tickers = client.get_ticker()
    
    
    uzunluk_listenin=int(len(tickers))
    
    semboller=[]
    degerler=[]
    for qe in range(0,uzunluk_listenin):
            
        if (tickers[qe]["symbol"][-4:]) =="USDT" :
            
            
            siralama_icin_bakiyorum=(tickers[qe]["priceChangePercent"])
            
            degerler.append(float(siralama_icin_bakiyorum))
      
        
      
        
    degerler.sort(reverse=True)
            
    
    uzunluk_degerlerin=int(len(degerler))      
    
    
    
    for yummi in range(0,uzunluk_listenin):
    
        for qeq in range(0,uzunluk_listenin):   
            if ((tickers[qeq]["symbol"][-4:]) =="USDT" ):
            
                try:              
           
                    if degerler[yummi]==float(tickers[qeq]["priceChangePercent"]):
                        semboller.append((tickers[qeq]["symbol"]))
                except:
                    pass              
            
    
    semboller=list(set(semboller))
except:
        pass

semboller.remove("STORMUSDT")
semboller.remove("PAXUSDT")   
semboller.remove("BTTUSDT")   
semboller.remove("TUSDUSDT")  
semboller.remove("BUSDUSDT")
semboller.remove("USDCUSDT")
semboller.remove("ETHUSDT")
semboller.remove("BTCUSDT")
semboller.remove("BNBUSDT")
semboller.remove("XRPUSDT")



#yüksek hacimlileri bölüştürdüm btc yi ayrı koydum
def yuksekhacimliler():
    print("yüksek hacimliler başladı") 
    #burada eklediğim kütüphane sorunsuz websocket bağlantısı sağladı bana
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], ["btcusdt"])
    
    
    sozluk2={"coin":{"veriler":[]}}
  
    
    while True:
        oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer()
        if oldest_data_from_stream_buffer:
                #print(oldest_data_from_stream_buffer)
                a = json.loads(oldest_data_from_stream_buffer)
                
        
              
    
                #eklensinmi=False
                #price=a["data"]["p"]
                #miktar=a["data"]["q"]
                #alisemrimi=a["data"]["m"]==False
                #timestamp=a["data"]["T"]
                
                try:
                    #print("coin:%s\nalis emri mi:%s\nprice:%s\nmiktar:%s"%(a["stream"],alisemrimi,price,miktar))
        
                    try:
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    except:
                        sozluk2.update({a["stream"].split("@")[0]:{"veriler":[]}})
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    
                    
                    if len(sozluk2[a["stream"].split("@")[0]]["veriler"]) >300:
                            
                        dAdi="jsons/"+a["stream"].split("@")[0]+".json"
                        
                        try:      
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                        except:
                            sozluk={"veriler":[]}
                            with open(dAdi, 'w') as f:
                                json.dump(sozluk, f)
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                                
        
                    
                    
                        for i in sozluk2[a["stream"].split("@")[0]]["veriler"]:
                            #print(i)
                            sozluk["veriler"].append(i)
                            
                        with open(dAdi, 'w') as f:
                            json.dump(sozluk, f)
                        sozluk2[a["stream"].split("@")[0]]={"veriler":[]}
                       
                except Exception as e:
                    print(e)
                
    



global x
x=0
def coinler1():
    print("coinler1  başladı") 
    global x 
    coinler1semboller=semboller[x:x+100]
    coinler1semboller.append("bnbusdt")
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], coinler1semboller)
    
    
    sozluk2={"coin":{"veriler":[]}}
  
    
    while True:
        oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer()
        if oldest_data_from_stream_buffer:
                #print(oldest_data_from_stream_buffer)
                a = json.loads(oldest_data_from_stream_buffer)
                
        
              
    
                #eklensinmi=False
                #price=a["data"]["p"]
                #miktar=a["data"]["q"]
                #alisemrimi=a["data"]["m"]==False
                #timestamp=a["data"]["T"]
                
                try:
                    #print("coin:%s\nalis emri mi:%s\nprice:%s\nmiktar:%s"%(a["stream"],alisemrimi,price,miktar))
        
                    try:
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    except:
                        sozluk2.update({a["stream"].split("@")[0]:{"veriler":[]}})
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    
                    
                    if len(sozluk2[a["stream"].split("@")[0]]["veriler"]) >1000:
                        print("bin veri aşıldı.")    
                        dAdi="jsons/"+a["stream"].split("@")[0]+".json"
                        
                        try:      
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                        except:
                            sozluk={"veriler":[]}
                            with open(dAdi, 'w') as f:
                                json.dump(sozluk, f)
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                                
        
                    
                    
                        for i in sozluk2[a["stream"].split("@")[0]]["veriler"]:
                            #print(i)
                            sozluk["veriler"].append(i)
                            
                        with open(dAdi, 'w') as f:
                            json.dump(sozluk, f)
                        sozluk2[a["stream"].split("@")[0]]={"veriler":[]}
                        print("kaydetti")
                        
                except Exception as e:
                    print(e)
                
    
def coinler2():
    global x 
    print("coinler2  başladı") 
    coinler2semboller=semboller[x+100:x+200]
    coinler2semboller.append("xrpusdt")
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], coinler2semboller)
    
    
    sozluk2={"coin":{"veriler":[]}}
    
    
    while True:
        oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer()
        if oldest_data_from_stream_buffer:
                #print(oldest_data_from_stream_buffer)
                a = json.loads(oldest_data_from_stream_buffer)
                
        
              
    
                #eklensinmi=False
                #price=a["data"]["p"]
                #miktar=a["data"]["q"]
                #alisemrimi=a["data"]["m"]==False
                #timestamp=a["data"]["T"]
                
                try:
                    #print("coin:%s\nalis emri mi:%s\nprice:%s\nmiktar:%s"%(a["stream"],alisemrimi,price,miktar))
        
                    try:
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    except:
                        sozluk2.update({a["stream"].split("@")[0]:{"veriler":[]}})
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    
                    
                    if len(sozluk2[a["stream"].split("@")[0]]["veriler"]) >300:
                            
                        dAdi="jsons/"+a["stream"].split("@")[0]+".json"
                        
                        try:      
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                        except:
                            sozluk={"veriler":[]}
                            with open(dAdi, 'w') as f:
                                json.dump(sozluk, f)
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                                
        
                    
                    
                        for i in sozluk2[a["stream"].split("@")[0]]["veriler"]:
                            #print(i)
                            sozluk["veriler"].append(i)
                            
                        with open(dAdi, 'w') as f:
                            json.dump(sozluk, f)
                        sozluk2[a["stream"].split("@")[0]]={"veriler":[]}
                       
                except Exception as e:
                    print(e)

def coinler3():
    print("coinler3  başladı") 
    global x 
    coinler3semboller=semboller[x+200:x+300]
    coinler3semboller.append("ethusdt")
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], coinler3semboller)
    
    
    sozluk2={"coin":{"veriler":[]}}
  
    
    while True:
        oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer()
        if oldest_data_from_stream_buffer:
                #print(oldest_data_from_stream_buffer)
                a = json.loads(oldest_data_from_stream_buffer)
                
        
              
    
                #eklensinmi=False
                #price=a["data"]["p"]
                #miktar=a["data"]["q"]
                #alisemrimi=a["data"]["m"]==False
                #timestamp=a["data"]["T"]
                
                try:
                    #print("coin:%s\nalis emri mi:%s\nprice:%s\nmiktar:%s"%(a["stream"],alisemrimi,price,miktar))
        
                    try:
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    except:
                        sozluk2.update({a["stream"].split("@")[0]:{"veriler":[]}})
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    
                    
                    if len(sozluk2[a["stream"].split("@")[0]]["veriler"]) >300:
                            
                        dAdi="jsons/"+a["stream"].split("@")[0]+".json"
                        
                        try:      
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                        except:
                            sozluk={"veriler":[]}
                            with open(dAdi, 'w') as f:
                                json.dump(sozluk, f)
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                                
        
                    
                    
                        for i in sozluk2[a["stream"].split("@")[0]]["veriler"]:
                            #print(i)
                            sozluk["veriler"].append(i)
                            
                        with open(dAdi, 'w') as f:
                            json.dump(sozluk, f)
                        sozluk2[a["stream"].split("@")[0]]={"veriler":[]}
                        
                except Exception as e:
                    print(e)

def coinler4():
    print("coinler4  başladı") 
    global x 
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], semboller[x+300:x+400])
    
    
    sozluk2={"coin":{"veriler":[]}}
   
    
    while True:
        oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer()
        if oldest_data_from_stream_buffer:
                #print(oldest_data_from_stream_buffer)
                a = json.loads(oldest_data_from_stream_buffer)
                
        
              
    
                #eklensinmi=False
                #price=a["data"]["p"]
                #miktar=a["data"]["q"]
                #alisemrimi=a["data"]["m"]==False
                #timestamp=a["data"]["T"]
                
                try:
                    #print("coin:%s\nalis emri mi:%s\nprice:%s\nmiktar:%s"%(a["stream"],alisemrimi,price,miktar))
        
                    try:
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    except:
                        sozluk2.update({a["stream"].split("@")[0]:{"veriler":[]}})
                        sozluk2[a["stream"].split("@")[0]]["veriler"].append(a["data"])
                    
                    
                    if len(sozluk2[a["stream"].split("@")[0]]["veriler"]) >300:
                            
                        dAdi="jsons/"+a["stream"].split("@")[0]+".json"
                        
                        try:      
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                        except:
                            sozluk={"veriler":[]}
                            with open(dAdi, 'w') as f:
                                json.dump(sozluk, f)
                            with open(dAdi) as f:
                                sozluk = json.load(f)
                                
        
                    
                    
                        for i in sozluk2[a["stream"].split("@")[0]]["veriler"]:
                            #print(i)
                            sozluk["veriler"].append(i)
                            
                        with open(dAdi, 'w') as f:
                            json.dump(sozluk, f)
                        sozluk2[a["stream"].split("@")[0]]={"veriler":[]}
                   
                     
                except Exception as e:
                    print(e)
                    
                    
y = threading.Thread(target=yuksekhacimliler)
y.start()    


#y1 = threading.Thread(target=coinler1)
#y1.start()    

#y2 = threading.Thread(target=coinler2)
#y2.start()    

#y3 = threading.Thread(target=coinler3)
#y3.start()    

#y4 = threading.Thread(target=coinler4)
#y4.start()    





