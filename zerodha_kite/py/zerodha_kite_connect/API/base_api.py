"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""
# Python Dependencies
import traceback

#Package Dependency
from zerodha_kite_connect.zerodha_connect import ZerodhaConnect

class BASEAPI:
	def __init__(self, kite_client=None, kite_ticker_client=None):
		self.__kite_client = kite_client
		self.__kite_ticker_client = kite_ticker_client

	@property
	def kc_client(self):
		if not self.__kc_client:
			try:
				obj_zc = ZerodhaConnect()
				self.__kc_client = obj_zc.kc_client
			except Exception as e:
				print("Error in creating kite connect Client with error %s." % str(e))
				print(traceback.format_exc())
		return self.__kc_client

	@property
	def kt_client(self):
		if not self.__kite_ticker_client:
			try:
				obj_zc = ZerodhaConnect()
				self.__kite_ticker_client = obj_zc.kite_ticker_client
			except Exception as e:
				print("Error in creating kite connect Client with error %s." % str(e))
				print(traceback.format_exc())
		return self.__kite_ticker_client
