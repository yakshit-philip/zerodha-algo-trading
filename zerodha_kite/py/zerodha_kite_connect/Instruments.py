"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""

# Third party Dependencies
import pandas as pd

# Python Internal Packages
import traceback
from datetime import date

# Package Dependencies
from zerodha_connect import ZerodhaConnect


class Instruments:
	def __init__(self, kite_client=None):
		self.__kc_client = kite_client

	@property
	def kc_client(self):
		if not self.__kc_client:
			try:
				obj_zc = ZerodhaConnect()
				self.__kc_client = obj_zc.kc_client
			except Exception as e:
				print("Error in creating kite connect Client with error %s." % str(e))
		return self.__kc_client

	def get_instruments_of_exchange(self, exchange):
		try:
			instruments = self.kc_client.instruments(exchange)
			return instruments
		except Exception as e:
			print("Error in getting instruments for exchange : %s with error %s" % (exchange, str(e)))
			print(traceback.format_exc())
			return None

	def get_instruments_of_exchange_as_dataframe(self, exchange):
		try:
			instruments = self.kc_client.instruments(exchange)
			instruments_dataframe = pd.DataFrame(instruments)
			return instruments_dataframe
		except Exception as e:
			print("Error in getting instruments for exchange : %s with error %s" % (exchange, str(e)))
			print(traceback.format_exc())
			return None

	def store_instruments_of_exchange_as_csv(self, exchange):
		try:
			instruments_df = self.get_instruments_of_exchange_as_dataframe(exchange)
			today = date.today()
			date_today = today.strftime("%b-%d-%Y")
			path_of_csv = "%s_Instruments_%s" % (exchange, str(date_today))
			instruments_df.to_csv(path_of_csv, index=False)
			return True
		except Exception as e:
			print("Error in storing instruments for exchange : %s with error %s" % (exchange, str(e)))
			print(traceback.format_exc())
			return False

	def get_instruments_from_csv(self, path_of_csv):
		# TODO -1- Implement to convert csv into dataframe based on the csv path.
		pass

	def get_instrument_for_symbol(self, exchange, symbol):
		try:
			instruments_df = self.get_instruments_of_exchange_as_dataframe(exchange)
			instrument_object = instruments_df[instruments_df.tradingsymbol == symbol]
			instrument_token = instrument_object.instrument_token.values[0]
			return instrument_token
		except Exception as e:
			print(f"Error in getting instrument token for symbol on exchange: {symbol} {exchange} with error {str(e)}")
			print(traceback.format_exc())
			return -1

	@staticmethod
	def get_instrument_for_symbol_from_loaded_df(instruments_df, symbol):
		try:
			instrument_object = instruments_df[instruments_df.tradingsymbol == symbol]
			instrument_token = instrument_object.instrument_token.values[0]
			return instrument_token
		except Exception as e:
			print("Error in getting instrument token for symbol: %s with error %s" % (symbol, str(e)))
			print(traceback.format_exc())
			return -1
