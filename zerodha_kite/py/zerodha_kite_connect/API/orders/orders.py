"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""
# Python Dependencies
import abc

# Package Dependencies
from zerodha_kite_connect.API.base_api import BASEAPI
from zerodha_kite_connect.utils import consts as consts

class Orders(BASEAPI):
	def __init__(self,exchange, kite_client=None):
		super().__init__(kite_client)
		self.__exchange = exchange

	@property
	def exchange_type(self):
		if self.__exchange == consts.NSE:
			return consts.NSE_EXCHANGE_TYPE
		elif self.__exchange == consts.BSE:
			return consts.BSE_EXCHANGE_TYPE
		else:
			return None

	def get_transaction_type(self, buy_sell):
		if buy_sell == consts.BUY:
			return consts.BUY_TRANSACTION_TYPE
		elif buy_sell == consts.SELL:
			return consts.SELL_TRANSACTION_TYPE
		else:
			return None

	@abc.abstractmethod
	def place_market_regular_order(self, symbol, quantity, buy_sell):
		pass

	@abc.abstractmethod
	def place_bracket_order(self, symbol, price, quantity, buy_sell, atr):
		pass



