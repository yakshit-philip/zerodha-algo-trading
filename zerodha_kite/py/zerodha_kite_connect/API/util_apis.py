"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""
# Python Dependency
import traceback

#Package Dependencies
from zerodha_kite_connect.API.base_api import BASEAPI

class UTILAPIS(BASEAPI):
	def __init__(self, kite_client=None):
		super().__init__(kite_client)

	def get_quote(self, exchange , symbol):
		try:
			ticker_string = f"{exchange}:{symbol}"
			quote = self.kc_client.quote(ticker_string)
			return quote
		except Exception as e:
			print("Error in getting quote for symbol %s with Error %s." %(symbol , str(e)))
			print(traceback.format_exc())
			return None

	def ltp(self , exchange , symbol):
		try:
			ticker_string = f"{exchange}:{symbol}"
			last_trading_price = self.kc_client.ltp(ticker_string)
			return last_trading_price
		except Exception as e:
			print("Error in fetching last trading price for symbol %s with error %s" %(symbol, str(e)))
			print(traceback.format_exc())
			return None

	def order_details(self):
		try:
			orders = self.kc_client.orders()
			return orders
		except Exception as e:
			print("Error in fetching orders : %s" % str(e))
			print(traceback.format_exc())
			return None

	def position_details(self):
		try:
			orders = self.kc_client.positions()
			return orders
		except Exception as e:
			print("Error in fetching positions : %s" % str(e))
			print(traceback.format_exc())
			return None

	def holding_details(self):
		try:
			orders = self.kc_client.holdings()
			return orders
		except Exception as e:
			print("Error in fetching user holdings : %s" % str(e))
			print(traceback.format_exc())
			return None
