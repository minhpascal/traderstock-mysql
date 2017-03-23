#coding=utf-8
#import talib as ta
#import numpy as np
#import pandas as pd
#import os,time,sys,re,datetime
#import csv
#import scipy
#import smtplib
#from email.mime.text import MIMEText
#from email.MIMEMultipart import MIMEMultipart

import os, time, sys, re, datetime
import csv
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import multiprocessing

import stock
import macdkdjrsi
import kdj
import macd
import db
import volume
import ma
import boll

import tushare as ts


if __name__ == '__main__':

    
    s = stock.Stock.getInstance()
    b = boll.Boll.getInstance()
    m_a = ma.Ma.getInstance()

    start = time.clock()

    #s.save_stock_list()


    #s.download_all_stockdata()
    #s.update_all_stockdata()
    #s.download_recently_stockdata()
    s.update_recently_stockdata()

    #m_a.ma_xuangu2()

    #s.test()
    
    #mkr = macdkdjrsi.MacdKdjRsi.getInstance()
    #k = kdj.Kdj.getInstance()
    #m = macd.Macd.getInstance()
    #k.get_kdj_successrate(ty='D')
    #m.get_macd_successrate(ty='D')
    #k.get_kdj_successrate(ty='W')
    #m.get_macd_successrate(ty='W')
    #m.macd_xuangu()
    #k.kdj_xuangu()


    end = time.clock()

    print("ret: %f s" % (end - start))


