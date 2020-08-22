"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""
# Python Dependencies
import traceback
from datetime import date, timedelta

#Thirdparty Dependencies
import pandas as pd

# Package Dependencies
from zerodha_kite_connect.API.instruments import Instruments
from zerodha_kite_connect.API.base_api import BASEAPI


class HistoricalData(BASEAPI):
	def __init__(self, symbol, instruments_obj, duration, interval, kite_client=None):
		# TODO -1L- Interval have specific values only - define them as a list/dict and use that from consts.
		super().__init__(kite_client)
		self.__instrument_obj = instruments_obj
		self.__exchange = None
		self.__symbol = symbol
		self.__duration = duration
		self.__interval = interval

	def __int__(self,symbol, exchange, duration, interval, kite_client=None):
		super().__init__(kite_client)
		self.__instrument_obj = None
		self.__exchange = exchange
		self.__symbol = symbol
		self.__duration = duration
		self.__interval = interval

	@property
	def instrument_obj(self):
		if not self.__instrument_obj:
			try:
				if self.__exchange:
					obj_in = Instruments(self.__exchange, self.kc_client)
					self.__instrument_obj = obj_in
				else:
					raise Exception("Neither exchange or instrument obj availble wrong initialization of class")
			except Exception as e:
				print("Error in getting instrument df %s" % str(e))
				print(traceback.format_exc())
		return self.__instrument_obj

	@property
	def OCHLV_dataframe(self):
		try:
			instrument_token = self.__instrument_obj.get_instrument_for_symbol(self.__symbol)
			historical_data = self.kc_client.historical_data(instrument_token,date.today()-timedelta(self.__duration),
																											 date.today(),self.__interval)
			historical_data_df = pd.DataFrame(historical_data)
			historical_data_df.set_index("date", inplace=True)
			return historical_data_df
		except Exception as e:
			print("Error in getting OHCL data for symbol : %s with error %s" % (self.__symbol, str(e)))
			print(traceback.format_exc())
			return None

	def save_OHCLV_data_to_DB(self):
		# TODO -1- Implement
		pass

	def save_OHCLV_data_to_csv(self):
		# TODO -2- Implement
		pass





