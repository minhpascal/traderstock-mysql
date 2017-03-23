#coding=utf-8
import talib as ta
import pandas as pd
import os,time,sys,re,datetime
import stock
import copy
import db
import utils

class Boll:
	__instance = None
	def __init__(self):
		pass

	@classmethod
	def getInstance(cls):
		if(cls.__instance == None):
			cls.__instance = Boll()
		return cls.__instance

	#计算boll
	def set_boll_data(self, df, n=20, multiple=2):
		if df is None or df.shape[0] <= 0:
			return None

		#df2 = df.copy()

		#计算布林带的中轨线，上轨线，下轨线
		#df2['boll_tp'] = (df['high'] + df['low'] + df['close'])/3
		#df2['boll_sd'] = df2['boll_tp'].rolling(window=n, center=False).std()


		#df['boll_mid'] = df2['boll_tp'].rolling(window=n, center=False).mean()
		#df['boll_up'] = df['boll_mid'] + df2['boll_sd'] * multiple
		#df['boll_down'] = df['boll_mid'] - df2['boll_sd'] * multiple

		df2 = df.copy()

		#计算布林带的中轨线，上轨线，下轨线
		df['boll_mid'] = df['close'].rolling(window=n, center=False).mean()
		df2['boll_sd'] = df['close'].rolling(window=n, center=False).std()

		df['boll_up'] = df['boll_mid'] + df2['boll_sd'] * multiple
		df['boll_down'] = df['boll_mid'] - df2['boll_sd'] * multiple

		return df