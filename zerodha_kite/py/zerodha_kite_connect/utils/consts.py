"""
Copyright Opia Technologies Pvt Limited 2020

Author :
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
"""
from kiteconnect import KiteConnect
from zerodha_kite_connect.utils.creds import API_KEY
# Login Constants
WAIT_TIME = 10
SLEEP_TIME = 10
USERNAME_XPATH = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input"
PASSWORD_XPATH = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input"
LOGIN_BUTTON_XPATH = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button"
PIN_XPATH = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input"
GO_BUTTON_XPATH = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/button"

# Order API Constants

BUY = 'BUY'
SELL = 'SELL'
NSE = "NSE"
BSE = "BSE"
KITE = KiteConnect(API_KEY)
BUY_TRANSACTION_TYPE = KITE.TRANSACTION_TYPE_BUY
SELL_TRANSACTION_TYPE = KITE.TRANSACTION_TYPE_SELL
MARKET_ORDER_TYPE = KITE.ORDER_TYPE_MARKET
LIMIT_ORDER_TYPE = KITE.ORDER_TYPE_LIMIT
NSE_EXCHANGE_TYPE = KITE.EXCHANGE_NSE
BSE_EXCHANGE_TYPE = KITE.EXCHANGE_BSE
VARIETY_BRACKET_ORDER = KITE.VARIETY_BO
VARIETY_REGULAR = KITE.VARIETY_REGULAR
VARIETY_AFTER_MARKET_ORDER = KITE.VARIETY_AMO
VARIETY_COVER_ORDER = KITE.VARIETY_CO
CNC_ORDER = KITE.PRODUCT_CNC
MIS_ORDER = KITE.PRODUCT_MIS
NRML_ORDER = KITE.PRODUCT_NRML
DAY_ORDER = KITE.VALIDITY_DAY
IOC_ORDER = KITE.VALIDITY_IOC

