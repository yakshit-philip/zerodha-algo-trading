"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""
# Python Dependency
import traceback

# Package Dependency
from zerodha_kite_connect.API.orders.orders import Orders
from zerodha_kite_connect.utils import consts as consts


class NRMLORDERS(Orders):
	def __init__(self, exchange, kite_client=None):
		super().__init__(exchange, kite_client)
		self.__product_type = consts.NRML_ORDER

	# TODO -1L- Add retry decorator in case of failure.
	def place_market_regular_order(self, symbol, quantity, buy_sell):
		order_id_generated = None
		try:
			order_response = self.kc_client.place_order(
				variety=consts.VARIETY_REGULAR, exchange=self.exchange_type, tradingsymbol=symbol,
				transaction_type=self.get_transaction_type(buy_sell), quantity=quantity, product=self.__product_type,
				order_type=consts.MARKET_ORDER_TYPE, validity=consts.DAY_ORDER)
			if order_response:
				if order_response.get("status") and order_response.get("status") == "success":
					order_id_generated = order_response.get("data").get("order_id")
		except Exception as e:
			print("Error in placing Regular Market order for Symbol %s with error %s" % (symbol, str(e)))
			print(traceback.format_exc())
		return order_id_generated

	def place_bracket_order(self, symbol, price, quantity, buy_sell, atr):
		order_id_generated = None
		try:
			order_response = self.kc_client.place_order(
				variety=consts.VARIETY_BRACKET_ORDER, exchange=self.exchange_type, tradingsymbol=symbol,
				transaction_type=self.get_transaction_type(buy_sell), quantity=quantity, product=self.__product_type,
				order_type=consts.LIMIT_ORDER_TYPE, validity=consts.DAY_ORDER, price=price,squareoff=int(6*atr),
				stoploss=int(3*atr),trailing_stoploss=2)
			if order_response:
				if order_response.get("status") and order_response.get("status") == "success":
					order_id_generated = order_response.get("data").get("order_id")
		except Exception as e:
			print("Error in placing Regular Market order for Symbol %s with error %s" % (symbol, str(e)))
			print(traceback.format_exc())
		return order_id_generated
