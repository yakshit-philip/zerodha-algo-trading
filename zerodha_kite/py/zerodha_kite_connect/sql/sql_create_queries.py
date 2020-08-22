"""
Copyright Opia Technologies Pvt Limited 2020
@author
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
Class to fetch sql queries for creating tables and dbs
"""


def create_db(db_name):
	create_db = f"sqlite3 {db_name}.db"
	return create_db


def create_streaming_table_for_symbol(exchange, symbol):
	create_full_mode_table = \
		f"""
		CREATE TABLE FULL_{exchange}_{symbol}(
			ID_DATE TEXT PRIMARY KEY NOT NULL,
			LAST_PRICE REAL NOT NULL,
			LAST_QUANTITY INTEGER NOT NULL,
			AVERAGE_PRICE REAL NOT NULL,
			VOLUME INTEGER NOT NULL,
			BUY_QUANTITY INTEGER NOT NULL,
			SELL_QUANTITY INTEGER NOT NULL,
			OPEN_PRICE REAL NOT NULL,
			HIGH_PRICE REAL NOT NULL,
			CLOSE_PRICE REAL NOT NULL,
			LOW_PRICE REAL NOT NULL,
			CHANGE REAL NOT NULL,
			LAST_TRADE_TIME TEXT NOT NULL,
			OPEN_INTEREST INTEGER NOT NULL,
			OPEN_INTEREST_HIGH INTEGER NOT NULL,
			OPEN_INTEREST_LOW INTEGER NOT NULL
		);
		"""
	create_full_mode_market_depth_buy_table = \
		f"""
		CREATE TABLE FULL_{exchange}_{symbol}_MARKET_DEPTH_BUY(
			ID_DATE TEXT NOT NULL,
			QUANTITY INTEGER NOT NULL,
			PRICE REAL NOT NULL,
			ORDERS INTEGER NOT NULL,
			PRIMARY KEY (ID_DATE,QUANTITY,PRICE,ORDERS)
		);
		"""
	create_full_mode_market_depth_sell_table = \
		f"""
		CREATE TABLE FULL_{exchange}_{symbol}_MARKET_DEPTH_SELL(
			ID_DATE TEXT NOT NULL,
			QUANTITY INTEGER NOT NULL,
			PRICE REAL NOT NULL,
			ORDERS INTEGER NOT NULL,
			PRIMARY KEY (ID_DATE,QUANTITY,PRICE,ORDERS)
		);
		"""
	return create_full_mode_table , create_full_mode_market_depth_buy_table , create_full_mode_market_depth_sell_table
