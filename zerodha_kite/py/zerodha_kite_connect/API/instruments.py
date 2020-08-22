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
from zerodha_kite_connect.API.base_api import BASEAPI


class Instruments(BASEAPI):
	def __init__(self, exchange, kite_client=None):
		super().__init__(kite_client)
		self.__exchange = exchange
		self.__instruments = None
		self.__instruments_df = None

	@property
	def instruments_of_exchange(self):
		if not self.__instruments:
			try:
				instruments = self.kc_client.instruments(self.__exchange)
				self.__instruments = instruments
			except Exception as e:
				print("Error in getting instruments for exchange : %s with error %s" % (self.__exchange, str(e)))
				print(traceback.format_exc())
		return self.__instruments

	@property
	def instruments_of_exchange_as_dataframe(self):
		if not self.__instruments_df:
			try:
				instruments_dataframe = pd.DataFrame(self.instruments_of_exchange)
				self.__instruments_df = instruments_dataframe
			except Exception as e:
				print("Error in getting instruments for exchange : %s with error %s" % (self.__exchange, str(e)))
				print(traceback.format_exc())
		return self.__instruments_df

	def store_instruments_of_exchange_as_csv(self):
		try:
			instruments_df = self.instruments_of_exchange_as_dataframe
			today = date.today()
			date_today = today.strftime("%b-%d-%Y")
			path_of_csv = "%s_Instruments_%s" % (self.__exchange, str(date_today))
			instruments_df.to_csv(path_of_csv, index=False)
			return True
		except Exception as e:
			print("Error in storing instruments for exchange : %s with error %s" % (self.__exchange, str(e)))
			print(traceback.format_exc())
			return False

	def get_instruments_from_csv(self, path_of_csv):
		# TODO -1- Implement to convert csv into dataframe based on the csv path.
		pass

	def get_instrument_for_symbol(self, symbol):
		try:
			instruments_df = self.instruments_of_exchange_as_dataframe
			instrument_object = instruments_df[instruments_df.tradingsymbol == symbol]
			instrument_token = instrument_object.instrument_token.values[0]
			return instrument_token
		except Exception as e:
			print(f"Error in getting instrument token for symbol: {symbol} with error {str(e)}")
			print(traceback.format_exc())
			return -1

	def get_instruments_for_symbols(self, symbol_list):
		instrument_token_dict = dict()
		try:
			instruments_df = self.instruments_of_exchange_as_dataframe
			for symbol in symbol_list:
				instrument_object = instruments_df[instruments_df.tradingsymbol == symbol]
				instrument_token = instrument_object.instrument_token.values[0]
				instrument_token_dict[symbol] = int(instrument_token)
		except Exception as e:
			print("Error in instruments token for the given symbols with error : %s" % str(e))
			print(traceback.format_exc())
		return instrument_token_dict


