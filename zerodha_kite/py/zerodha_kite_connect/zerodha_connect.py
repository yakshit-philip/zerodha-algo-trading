"""
Copyright Opia Technologies Pvt Limited 2020
@author
	Name : Yakshit Philip
	Email : yakshit.philip@gmail.com
Class to test manual Connection to zerodha Kite connect API
"""

# Python Internal Packages
import time

# Third Party Dependencies
from kiteconnect import KiteConnect
from selenium import webdriver

# Package Dependency
from zerodha_kite_connect.utils.utils import decrypt
from zerodha_kite_connect.utils import creds as creds
from zerodha_kite_connect.utils import consts as consts


class ZerodhaConnect:
	def __init__(self):
		self.__kc_client = None
		self.__access_token = None

	@property
	def kc_client(self):
		if not self.__kc_client:
			try:
				if not self.access_token:
					print("Error in retrieving access token")
					raise Exception("Cannot create kite session as no access token is available.")
				kite_client = KiteConnect(api_key=creds.API_KEY)
				kite_client.set_access_token(self.access_token)
				self.__kc_client = kite_client
			except Exception as e:
				print("Error in creating kite client with error %s." % str(e))
		return self.__kc_client

	def get_request_token(self, login_url):
		initialization_of_driver_successful = False
		try:
			service = webdriver.chrome.service.Service("../../../drivers/chromedriver")
			service.start()
			options = webdriver.ChromeOptions()
			options.add_argument("--headless")
			options.to_capabilities()
			driver = webdriver.Remote(service.service_url, options)
			initialization_of_driver_successful = True
			driver.get(login_url)
			driver.implicitly_wait(consts.WAIT_TIME)
			username = driver.find_element_by_xpath(consts.USERNAME_XPATH)
			password = driver.find_element_by_xpath(consts.PASSWORD_XPATH)
			username.send_keys(creds.KITE_USER_ID)
			password.send_keys(decrypt(creds.PASSWORD_ENCRYPTED))
			driver.find_element_by_xpath(consts.LOGIN_BUTTON_XPATH).click()
			pin = driver.find_element_by_xpath(consts.PIN_XPATH)
			pin.send_keys(decrypt(creds.PIN_ENCRYPTED))
			driver.find_element_by_xpath(consts.GO_BUTTON_XPATH)
			time.sleep(consts.SLEEP_TIME)
			request_token = driver.current_url.split('=')[1].split('&action')[0]
			if request_token:
				return request_token
			else:
				raise Exception("Couldn't Login - please try again.")
		except Exception as e:
			print("Error in getting request Token with error %s." % str(e))
		finally:
			if initialization_of_driver_successful:
				driver.quit()

	# - TODO -1- for later save the access token to a file and pick it from there and check if it is active or
	#    expired and based on that generate new access token
	@property
	def access_token(self):
		if not self.__access_token:
			try:
				kite_client = KiteConnect(api_key=creds.API_KEY)
				request_token = self.get_request_token(login_url=(kite_client.login_url()))
				data = kite_client.generate_session(request_token=request_token, api_secret=creds.API_SECRET)
				access_token = data.get("access_token", None)
				if not access_token:
					print("No key available in session as access token. sending as None.")
				self.__access_token = access_token
			except Exception as e:
				print("Error in fetching access token with error %s." % str(e))
		return self.__access_token

	def renew_kite_connection(self):
		"""
		Function to renew kite connection in case of expiration of access token.
		Returns:
			kc_client : Kite Connection object
		"""
		self.__kc_client = None
		self.__access_token = None
		return self.kc_client
