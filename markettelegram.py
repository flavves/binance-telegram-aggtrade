# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 08:40:18 2022

@author: okmen
"""
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
            
            apiid="5422970822:AAEvfDaaI8DvxC1xp6ZTpyEAMivOPiU2EG8"
    
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
                    with open(dAdi) as f:
                        sozluk = json.load(f)
                    
                    ###################################3
                    #pandas denemesi excell
                    df = pd.DataFrame()
                    #pandasdf=pd.DataFrame.from_dict({"kademe":[alislar["price"]],"Alış Total":[alislar["quoteQty"]],
                    #                                 "Satış Total":"","toplam":""})
                    
                    #df = df.append(pandasdf, ignore_index = True)
                    
                    ######################################
                    
                    toplam_alis=0
                    toplam_alis_sayac=0
                    alislars=""
                    for alislar in sozluk["alıs"]:
                        
                        start_ts = alislar["time"]
                        end_ts = time.time()
                        dt1 = datetime.fromtimestamp(start_ts)
                        dt2 = datetime.fromtimestamp(end_ts)
                        delta = dt2 - dt1 
                        def days_hours_minutes(td):
                            return td.days, td.seconds//3600, (td.seconds//60)%60               
                        verininzamanı=days_hours_minutes(delta)
                        if verininzamanı[0]==0:
                            if verininzamanı[1]<zaman:
                                if alislar["price"]==0:
                                    pass
                                else:
                                    toplam_alis_sayac=toplam_alis_sayac+1
                                    pandasdf=pd.DataFrame.from_dict({"kademe":[alislar["price"]],"Alış Total":[alislar["quoteQty"]],
                                                     "Satış Total":pd.NaT,"toplam":pd.NaT})
                                    df = df.append(pandasdf, ignore_index = True)
                                    
                                    
                                    """
                                    if toplam_alis_sayac==11:
                                        toplamicinsozluk={"aratoplam":toplam_alis}
                                        pandasdf=pd.DataFrame.from_dict({"Alış Total":[toplamicinsozluk["aratoplam"]],
                                                                         "toplam":"ARA TOPLAM"})
                                        toplam_alis=0
                                        toplam_alis_sayac=0
                                    """
                                        
                    
                    
                 
                    
                    toplam_satis=0
                    toplam_satis_sayac=0
                    #update.message.reply_text(a)      
                    satislars =""
                    for satislar in sozluk["satis"]:
                        start_ts = satislar["time"]
                        end_ts = time.time()
                        dt1 = datetime.fromtimestamp(start_ts)
                        dt2 = datetime.fromtimestamp(end_ts)
                        delta = dt2 - dt1 
                        def days_hours_minutes(td):
                            return td.days, td.seconds//3600, (td.seconds//60)%60               
                        verininzamanı=days_hours_minutes(delta)
                        if verininzamanı[0]==0:
                            if verininzamanı[1]<zaman:
                                if satislar["price"]==0:
                                    pass
                                else:
                                    toplam_satis_sayac=toplam_satis_sayac+1
                                    
                                    varmi=df.loc[df['kademe'] == satislar["price"]]                  
                                    if len(varmi)   >0:
                                  
                                        print(varmi)
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

def veritoplama():
        
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
    
    
    
    #bu olcak gibi
    
    idler=[]
    time.sleep(2)
    coin="BANDUSDT"
    
    while 1:
            
        for coin in semboller:
               
            dAdi="jsons/"+coin+".json"
            
            try:      
                with open(dAdi) as f:
                    sozluk = json.load(f)
            except:
                sozluk={"alıs":[{"price":0,"quoteQty":0,"time":0}],"satis":[{"price":0,"quoteQty":0,"time":0}],"idler":[]}
                with open(dAdi, 'w') as f:
                    json.dump(sozluk, f)
                with open(dAdi) as f:
                    sozluk = json.load(f)
                    
            sayac=0
            
            idler=sozluk["idler"]
            time.sleep(2)
            trades = client.get_recent_trades(symbol=coin,limit=1000)   
            #trades.reverse()  
            eklensinmi=False
            kayac=0
            yeniidler=[]
            for veri in trades:
                  
                    
                    if veri["id"] not in  idler:
                        
                        timestamp = int(veri["time"])/1000
                        dt_object = datetime.fromtimestamp(timestamp)
                        yeniidler.append(veri["id"])
                        eklensinmi=False
                        try:           
                            if veri["isBuyerMaker"]==False:
                                sira_kalender=-1
                                for kalender in sozluk["alıs"]:
                                    sira_kalender +=1    
                                    if kalender["price"]==float(veri["price"]):
                                        #kalender["quoteQty"]=kalender["quoteQty"]+float(veri["quoteQty"])#hata burada bu kalender şeyine kayıt yapamıyo eskiden [0] falandı ya o işe yarıyordu.
                                        sozluk["alıs"][sira_kalender]["quoteQty"]=kalender["quoteQty"]+float(veri["quoteQty"])
                                        sozluk["alıs"][sira_kalender]["time"]=timestamp
                                        eklensinmi=True
                                        sira_kalender=-1
                                        break
                                    
                                if eklensinmi==False:
                                        
                                        sozluk["alıs"].append({"price":float(veri["price"]),"quoteQty":float(veri["quoteQty"]),"time":timestamp})  
                                        eklensinmi=True
                                    
                            elif veri["isBuyerMaker"]==True:
                                sira_kalender=-1
                                for kalender in sozluk["satis"]:
                                    sira_kalender +=1
                                    if kalender["price"]==float(veri["price"]):
                                        sozluk["satis"][sira_kalender]["quoteQty"]=kalender["quoteQty"]+float(veri["quoteQty"])
                                        sozluk["satis"][sira_kalender]["time"]=timestamp
                                        eklensinmi=True
                                        sira_kalender=-1
                                        break    
                                    
                                    
                                if eklensinmi==False:
                                          
                                        sozluk["satis"].append({"price":float(veri["price"]),"quoteQty":float(veri["quoteQty"]),"time":timestamp})  
                                        eklensinmi=True
                        except Exception as e:
                            print(e)  
            
            for x in yeniidler:
              idler.append(x)                
            
            
            sozluk["idler"]=idler
            
            with open(dAdi, 'w') as f:
                json.dump(sozluk, f)


y = threading.Thread(target=telegrambotu)
y.start()     
  
z = threading.Thread(target=veritoplama)
z.start()   