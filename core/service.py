import json
from datetime import datetime
from pymongo import MongoClient
from bson.json_util import dumps
from bson.timestamp import Timestamp
import datetime
from textblob import TextBlob as tb
import numpy as np
from datetime import date


cliente = MongoClient('localhost',27017)
banco = cliente['local']
db_pi = banco['pi2']

def sentimentos(palavra):
    dados = db_pi.distinct("createdAt",{"$and":[{"text":{"$regex": u"{0}".format(palavra)}},{"lang":{"$eq":"en"}},{"createdAt":{"$gte":"Sep 14, 2017 2:22:08 PM","$lte" :"Sep 30, 2017 2:23:00 PM"}}]})

    # dados = db_pi.find({"$and" :[{"text":{"$regex": u"ladygaga"}},{"lang":{"$eq":"en"}}]}).limit(10)
    # valores=[]
    # for t in dados:
    #     polaridade = tb(t['text']).sentiment
    #     valores.append(polaridade.polarity)
    datas= []
    medias=[]

    for tweet in dados:
        tweet_espec = db_pi.find({"$and":[{"text":{"$regex": u"{0}".format(palavra)}},{"lang":{"$eq":"en"}},{"createdAt":{"$eq":tweet}}]})
        polaridade = []
        for tweet2 in tweet_espec:
            polaridade.append(tb(tweet2['text']).sentiment.polarity)

        datas.append(tweet)
        medias.append(np.mean(polaridade))

    dadosfinais = {
        "datas":datas,
        "polaridade": medias
    }

    return dadosfinais
    # return valores

def qntPorPalavra():
    # datasDistintas = db_pi.distinct("createdAt")
    palavras=['lady gaga','rockinrio']

    qntidadesRep =[]

    for p in palavras:
        qnt = db_pi.find({"text":{"$regex": u"{0}".format(p)}}).count()
        qntidadesRep.append(qnt)

    resultado = {
        "palavras":palavras,
        "repeticoes": qntidadesRep
    }
    return resultado


