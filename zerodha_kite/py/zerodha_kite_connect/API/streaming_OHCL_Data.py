"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""

# Python Dependencies
import traceback

# Package Dependency
from zerodha_kite_connect.API.base_api import BASEAPI
from zerodha_kite_connect.utils import consts as consts


class Streaming_OHCL_DATA(BASEAPI):
	def __init__(self, symbol_dict, instrument_obj, kite_client=None, kite_ticker_client=None):
		super().__init__(kite_client, kite_ticker_client)
		self.__instruments_obj = instrument_obj
		self.__symbol_dict = symbol_dict
		self.__instrument_token_dict = None

	@property
	def instrument_token_dict(self):
		if not self.__instrument_token_dict:
			try:
				instrument_tokens = self.__instruments_obj.get_instruments_for_symbols(self.__symbol_dict.keys())
				self.__instrument_token_dict = instrument_tokens
			except Exception as e:
				print("Error in getting instrument token list with error %s" % str(e))
				print(traceback.format_exc())
		return self.__instrument_token_dict

	def mode_dict(self):
		mode_dict = dict()
		mode_dict[consts.LTP_MODE] = []
		mode_dict[consts.FULL_MODE] = []
		mode_dict[consts.QUOTE_MODE] = []
		try:
			for symbol, mode in self.__symbol_dict.iteritems():
				if mode == consts.LTP_MODE:
					mode_dict[consts.LTP_MODE].append(self.instrument_token_dict[symbol])
				elif mode == consts.QUOTE_MODE:
					mode_dict[consts.QUOTE_MODE].append(self.instrument_token_dict[symbol])
				elif mode == consts.FULL_MODE:
					mode_dict[consts.FULL_MODE].append(self.instrument_token_dict[symbol])
				else:
					mode_dict[consts.QUOTE_MODE].append(self.instrument_token_dict[symbol])
		except Exception as e:
			print("Error in setting mode for symbols with error %s" % str(e))
			print(traceback.format_exc())
		return mode_dict

	@staticmethod
	def set_mode_state(ws, mode_dict):
		if mode_dict.get(consts.LTP_MODE):
			ws.set_mode(ws.MODE_LTP, mode_dict.get(consts.LTP_MODE))
		if mode_dict.get(consts.QUOTE_MODE):
			ws.set_mode(ws.MODE_QUOTE, mode_dict.get(consts.QUOTE_MODE))
		if mode_dict.get(consts.FULL_MODE):
			ws.set_mode(ws.MODE_FULL, mode_dict.get(consts.FULL_MODE))

	def on_connect(self, ws, response):
		ws.subscribe(self.instrument_token_dict.values())
		self.set_mode_state(ws, self.mode_dict())

	@staticmethod
	def on_ticks(ticks):
		print("Ticks are : %s " % ticks)

	@staticmethod
	def on_close(ws, code, reason):
		ws.stop()

	def connect(self):
		self.kt_client.on_ticks = self.on_ticks
		self.kt_client.on_connect = self.on_connect
		# currently not adding on close as i want to infinitely stream the data
		# self.kt_client.on_close = self.on_close
		self.kt_client.connect()
