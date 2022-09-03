# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 08:40:18 2022

@author: okmen
"""

import unicorn_binance_websocket_api
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
def telegrambotu():        
    try:
            
            apiid="5694856804:AAGmEnnVVHYi2rwRMIpcqRoGC0M7gIqKxdU"
    
            namebot="bionlukdeneme"
            username="bionlukdenemebot"
            link="t.me/bionlukdenemebot"       
            logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    
            logger = logging.getLogger(__name__)
                    
                    
            def c(update, context):
                try:
                    gelen_mesaj=update["message"]["text"]
                except Exception as e:
                    gelen_mesaj="yokflavves"
                    print("hata mesajı",e)
                
                
                if gelen_mesaj =="yokflavves":
                    print("mesaj okunamadı")
                else:
                    
                    ######################## ÖRNEK
                    # veri="BTCUSDT,15m;ETHUSDT,30m;SOLUSDT,1h;AAVEUSDT,4h;TRXUSDT,2h;"
                    #print(update["message"]["chat"]["id"])
                    coin=gelen_mesaj.split(" ")[1][1:].upper()+"USDT"
                    fiyat=float(gelen_mesaj.split(" ")[2])
                                    
                    depth = client.get_order_book(symbol=coin,limit=1000)
    
                    alis=0
                    satis=0
                    
                    for alislar in depth["bids"]:
                        if fiyat == float(alislar[0]):
                            alis=(float(alislar[0])*float(alislar[1]))
                            break
                    
                    for satislar in depth["asks"]:
                        if fiyat == float(satislar[0]):
                            satis=(float(satislar[0])*float(satislar[1]))
                            break
                 
                    gonder="Coin:%s\nAlış: %s\nSatış: %s\ntotal %s\nK(Kademe): %s"%(coin,alis,satis,alis+satis,fiyat)
                    #update.message.reply_text("Alış: %s\n Satış: %s\n total %s\n K(Kademe): %s"%(alis,satis,alis+satis,fiyat))
                    #resime geç
                    
                    ##################################333
                    try:
                        grafikicinlabel=[]
                        data=[]
                        
                        sayac=0
                        for i in depth["bids"]:
                            sayac +=1
                            grafikicinlabel.append(i[0])
                            data.append(i[1])
                            if sayac==10:
                                break
                        
                        
                        
                         
                         
                        
                        #fig = plt.figure(figsize=(4,3),dpi=144)
                        
                        
                        
                        
                        fig = plt.figure(figsize =(10, 7))
                        plt.pie(data, labels = grafikicinlabel)
                        
                        fig.suptitle('BİDS', fontsize=23)
                        #plt.title("bids", x=0.0, y=0.0)
                        # show plot
                        plt.savefig('bids.png')
                        
                        
                        ##################################333
                        
                        grafikicinlabel=[]
                        data=[]
                        
                        sayac=0
                        for i in depth["asks"]:
                            sayac +=1
                            grafikicinlabel.append(i[0])
                            data.append(i[1])
                            if sayac==10:
                                break
                        
                        
                        
                         
                         
                        
                        #fig = plt.figure(figsize=(4,3),dpi=144)
                        
                        
                        
                        
                        fig = plt.figure(figsize =(10, 7))
                        plt.pie(data, labels = grafikicinlabel)
                        
                        fig.suptitle('ASKS', fontsize=23)
                        #plt.title("bids", x=0.0, y=0.0)
                        # show plot
                        plt.savefig('ASKS.png')
                        
                        ##################################333
                        
                        
                        
                        ##################################333
                        
                        # create figure
                        fig = plt.figure(figsize=(40, 15))
                          
                        # setting values to rows and column variables
                        rows = 1
                        columns = 2
                          
                        # reading images
                        Image1 = Image.open('bids.png')
                        Image2 = Image.open('ASKS.png')
                        
                        # Adds a subplot at the 1st position
                        fig.add_subplot(rows, columns, 1)
                          
                        # showing image
                        plt.imshow(Image1)
                        plt.axis('off')
                        
                          
                        # Adds a subplot at the 2nd position
                        fig.add_subplot(rows, columns, 2)
                          
                        # showing image
                        plt.imshow(Image2)
                        plt.axis('off')
                        plt.savefig('bidsandasks.png')
                        
                        ##################################333
                    except Exception as e:
                        print(e)
                                    
                                    
                    
                    
                    #resim bitti
                    bot = telegram.Bot(apiid)
                    """            
                    bot.send_photo(update["message"]["chat"]["id"],
                            photo=open('bidsandasks.png', 'rb'),
                            caption=gonder)
                    """
                    document = open('bidsandasks.png', 'rb')
                    bot.sendDocument(update["message"]["chat"]["id"],
                                             document = document,
                                             caption=gonder)
            
            
            def d(update, context):
                try:
                    gelen_mesaj=update["message"]["text"]
                except Exception as e:
                    gelen_mesaj="yokflavves"
                    print("hata mesajı",e)
                
                
                if gelen_mesaj =="yokflavves":
                    print("mesaj okunamadı")
                else:
                    
                    coin=gelen_mesaj.split(" ")[1][1:].upper()+"USDT"
                    zaman=int(gelen_mesaj.split(" ")[2])
                  
                    dAdi="jsons/"+coin+".json"
                    try:      
                            with open(dAdi) as f:
                                sozluka = json.load(f)
                                print("sözlük geldi")
                    except Exception as e:
                            print("sozluk alma hatası"+str(e))


                    sozluk_yeni={"alıs":[{"price":0,"quoteQty":0}],"satis":[{"price":0,"quoteQty":0,"time":0}]}
                    for veri in sozluka["veriler"]:
                        eklensinmi=False    
                        price=veri["p"]
                        miktar=veri["q"]
                        alisemrimi=veri["m"]==False
                        timestamp=veri["T"]
                        
                        try:
                                        start_ts = veri["T"]/1000
                                        end_ts = time.time()
                                        dt1 = datetime.fromtimestamp(start_ts)
                                        dt2 = datetime.fromtimestamp(end_ts)
                                        delta = dt2 - dt1 
                                        def days_hours_minutes(td):
                                            return td.days, td.seconds//3600, (td.seconds//60)%60               
                                        verininzamanı=days_hours_minutes(delta)
                                        if ((verininzamanı[0]>0) or ((verininzamanı[1]<zaman) == False)) :
                                            try:
                                                sozluk["veriler"].pop(sozluk["veriler"].index(veri))
                                            except:
                                                pass
                                            pass
                        except:pass
                      
                        
                    
                        
                        if veri["m"]==False:
                            sira_kalender=-1
                            for kalender in sozluk_yeni["alıs"]:
                                sira_kalender +=1
                                                                        
                              
                                if kalender["price"]==float(veri["p"]):
                                    #kalender["quoteQty"]=kalender["quoteQty"]+float(veri["quoteQty"])#hata burada bu kalender şeyine kayıt yapamıyo eskiden [0] falandı ya o işe yarıyordu.
                                    sozluk_yeni["alıs"][sira_kalender]["quoteQty"]=kalender["quoteQty"]+(float(veri["q"])*float(veri["p"]))
                                    eklensinmi=True
                                    sira_kalender=-1
                                    break
                                
                            if eklensinmi==False:
                                                                            
                                sozluk_yeni["alıs"].append({"price":float(veri["p"]),"quoteQty":float(veri["q"])*float(veri["p"])})  
                                eklensinmi=True
                        else:
                            sira_kalender=-1
                            for kalender in sozluk_yeni["satis"]:
                                sira_kalender +=1
                                                                        
                              
                                if kalender["price"]==float(veri["p"]):
                                    #kalender["quoteQty"]=kalender["quoteQty"]+float(veri["quoteQty"])#hata burada bu kalender şeyine kayıt yapamıyo eskiden [0] falandı ya o işe yarıyordu.
                                    sozluk_yeni["satis"][sira_kalender]["quoteQty"]=kalender["quoteQty"]+(float(veri["q"])*float(veri["p"]))
                                    eklensinmi=True
                                    sira_kalender=-1
                                    break
                                
                            if eklensinmi==False:
                                                                            
                                sozluk_yeni["satis"].append({"price":float(veri["p"]),"quoteQty":float(veri["q"])*float(veri["p"])})  
                                eklensinmi=True
                            
                        
                        
                    df = pd.DataFrame()
                    
                    
                    
                    try:
                                        toplam_alis=0
                                        toplam_alis_sayac=0
                                        alislars=""
                                        for alislar in sozluk_yeni["alıs"]:
                                            
                                                    if alislar["price"]==0:
                                                        pass
                                                    else:
                                                        toplam_alis_sayac=toplam_alis_sayac+1
                                                        pandasdf=pd.DataFrame.from_dict({"kademe":[alislar["price"]],"Alış Total":[alislar["quoteQty"]],
                                                                         "Satış Total":pd.NaT,"toplam":pd.NaT})
                                                        df = df.append(pandasdf, ignore_index = True)
                    
                                        
                                        toplam_satis=0
                                        toplam_satis_sayac=0
                                        #update.message.reply_text(a)      
                                        satislars =""
                                        for satislar in sozluk_yeni["satis"]:
                                            
                                                    if satislar["price"]==0:
                                                        pass
                                                    else:
                                                        toplam_satis_sayac=toplam_satis_sayac+1
                                                        
                                                        varmi=df.loc[df['kademe'] == satislar["price"]]                  
                                                        if len(varmi)   >0:
                                                      
                                                            #print(varmi)
                                                            df.loc[df['kademe'] == satislar["price"], 'Satış Total'] = [satislar["quoteQty"]]
                                                        else:
                                                            try:
                                                                pandasdf=pd.DataFrame.from_dict({"kademe":[satislar["price"]],
                                                                                                 "Alış Total":pd.NaT,
                                                                                                 "Satış Total":[satislar["quoteQty"]],
                                                                                                 "toplam":pd.NaT})
                                                                df = df.append(pandasdf, ignore_index = True)
                                                            except Exception as e:
                                                                print(e)
                                        
                                        
                    
                                        dfyeni = pd.DataFrame()
                                        
                                        
                                        
                                        for i in range(0,len(df),10):
                                                
                                            aratoplamicin=float('{0:.2f}'.format((df[i:i+10]["Alış Total"].dropna().sum())))
                                            arasatisicin=float('{0:.2f}'.format((df[i:i+10]["Satış Total"].dropna().sum())))
                                            toplam='{0:.2f}'.format(float(aratoplamicin)+float(arasatisicin))
                                            ekledicticin={"Alış Total":aratoplamicin,"Satış Total":arasatisicin,"toplam":aratoplamicin+arasatisicin}
                        
                                            pandasdf=pd.DataFrame.from_dict({"kademe":"SUBTOTAL",
                                                                             "Alış Total":[ekledicticin["Alış Total"]],
                                                                             "Satış Total":[ekledicticin["Satış Total"]],
                                                                             "toplam":[ekledicticin["toplam"]]})
                                            
                                   
                                            dfyeni2=(df[i:i+10])
                                            dfyeni=dfyeni.append(dfyeni2, ignore_index = True)
                                            dfyeni=dfyeni.append(pandasdf, ignore_index = True)
                                        # en son ana toplam
                                        
                                        aratoplamicin=float('{0:.2f}'.format((df["Alış Total"].dropna().sum())))
                                        arasatisicin=float('{0:.2f}'.format((df["Satış Total"].dropna().sum())))
                                        toplam='{0:.2f}'.format(float(aratoplamicin)+float(arasatisicin))
                                        ekledicticin={"Alış Total":aratoplamicin,"Satış Total":arasatisicin,"toplam":aratoplamicin+arasatisicin}
                                        pandasdf=pd.DataFrame.from_dict({"kademe":"TOTAL",
                                                                             "Alış Total":[ekledicticin["Alış Total"]],
                                                                             "Satış Total":[ekledicticin["Satış Total"]],
                                                                             "toplam":[ekledicticin["toplam"]]})
                                            
                                        dfyeni=dfyeni.append(pandasdf, ignore_index = True)                    
                                                       
                                        #dfyeni.to_excel("exceller/"+coin+'.xlsx', sheet_name='Sayfa1')        
                                        dfyeni2=pd.DataFrame()
                                        
                                        
                                        ekledicticin_enson={"kademe":str(coin),"Alış Total":str(zaman)}
                                        
                                        pandasdf=pd.DataFrame.from_dict({"kademe":[ekledicticin_enson["kademe"]],
                                                                         "Alış Total":[ekledicticin_enson["Alış Total"]],})
                                        
                                        dfyeni2=dfyeni2.append(pandasdf, ignore_index = True)
                                        dfyeni2=dfyeni2.append(dfyeni, ignore_index = True)
                                        dfyeni2.to_excel("exceller/"+coin+'.xlsx', sheet_name='Sayfa1')     
                                        
                                        bot = telegram.Bot(apiid)
                                        document = open("exceller/"+coin+'.xlsx', 'rb')
                                        bot.sendDocument(update["message"]["chat"]["id"],
                                                                 document = document)    
                                        
                        
                    except:pass  
                                                         
                 
                    
                    
            def help(update, context):
                """Send a message when the command /help is issued."""
                update.message.reply_text('Yardım geliyor')
            
            
           
            
            
            def error(update, context):
                """Log Errors caused by Updates."""
                logger.warning('Update "%s" caused error "%s"', update, context.error)
            
            
            def main():
                try:
                        
                    token = apiid
                    updater = Updater(token, use_context=True)
                    dp = updater.dispatcher
                    #komutlar burada
                    dp.add_handler(CommandHandler("c", c))
                    dp.add_handler(CommandHandler("d", d))
                    dp.add_handler(CommandHandler("help", help))
                    
        
                    dp.add_error_handler(error)
                    
                    
                    
                    
                    
                    
                    updater.start_polling()
                    updater.idle()
                except:pass
            
            
            if __name__ == '__main__':
                main()  
    
    except Exception as e:
            print("son hata:"+e)






#veri toplama






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
        try:
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
                        pass
                    
    
        except:
             ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
             ubwa.create_stream(['aggTrade'], ["btcusdt"])
   


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
        try:
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
                            #print("bin veri aşıldı.")    
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
                        pass
                    
        except:
            ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
            ubwa.create_stream(['aggTrade'], coinler1semboller)
            
def coinler2():
    global x 
    print("coinler2  başladı") 
    coinler2semboller=semboller[x+100:x+200]
    coinler2semboller.append("xrpusdt")
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], coinler2semboller)
    
    
    sozluk2={"coin":{"veriler":[]}}
    
    
    while True:
        try:
            
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
                        pass
        except:
            ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
            ubwa.create_stream(['aggTrade'], coinler2semboller)
def coinler3():
    print("coinler3  başladı") 
    global x 
    coinler3semboller=semboller[x+200:x+300]
    coinler3semboller.append("ethusdt")
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], coinler3semboller)
    
    
    sozluk2={"coin":{"veriler":[]}}
  
    
    while True:
        try:
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
                        pass
        except:
            ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
            ubwa.create_stream(['aggTrade'], coinler3semboller)
            
def coinler4():
    print("coinler4  başladı") 
    global x 
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['aggTrade'], semboller[x+300:x+400])
    
    
    sozluk2={"coin":{"veriler":[]}}
   
    
    while True:
        try:
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
                        pass
        except:
            ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
            ubwa.create_stream(['aggTrade'], semboller[x+300:x+400])                
                    
            
#y = threading.Thread(target=yuksekhacimliler)
#y.start()    


y1 = threading.Thread(target=coinler1)
y1.start()    

#y2 = threading.Thread(target=coinler2)
#y2.start()    

y3 = threading.Thread(target=coinler3)
y3.start()    

#y4 = threading.Thread(target=coinler4)
#y4.start()    


y_ssss = threading.Thread(target=telegrambotu)
y_ssss.start()     

















  
