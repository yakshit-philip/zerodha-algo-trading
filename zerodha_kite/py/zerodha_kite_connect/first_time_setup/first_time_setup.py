"""
Copyright Opia Technologies Pvt Limited 2020
@author
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
Class to test manual Connection to zerodha Kite connect API
"""

# Python Dependencies
import traceback

# Package Dependencies
from zerodha_kite_connect.zerodha_connect import ZerodhaConnect
from zerodha_kite_connect.API.historical_data import HistoricalData
from zerodha_kite_connect.API.instruments import Instruments
from zerodha_kite_connect.utils import consts as consts

class SetupZerodha():
	def __init__(self):
		self.__kc_client = None

	def run(self):
		try:
			obj_zc = ZerodhaConnect()
			obj_instruments = Instruments(exchange=consts.NSE, kite_client=obj_zc.kc_client)

			obj_hd = HistoricalData(instruments_obj=obj_instruments,kite_client=obj_zc.kc_client)
		except Exception as e:
			print("Error in setting up the system. %s" % str(e))
			print(traceback.format_exc())
