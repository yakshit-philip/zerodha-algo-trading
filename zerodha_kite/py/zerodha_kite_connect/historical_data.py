"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""

# Package Dependencies
from zerodha_connect import ZerodhaConnect


class HistoricalData:
	def __init__(self, kite_client=None):
		self.__kc_client = kite_client

	@property
	def kc_client(self):
		if not self.__kc_client:
			try:
				obj_zc = ZerodhaConnect()
				self.__kc_client = obj_zc.kc_client
			except Exception as e:
				print("Error in creating kite connect Client.")
		return self.__kc_client
