"""
Copywrite Opia Technologies Pvt Limited 2020
@author Yakshit Philip
Class to test manual Connection to zerodha Kite connect API
"""

from kiteconnect import KiteConnect
import pandas as pd

API_KEY = "abc"
API_SECRET = "bcd"


def test_client_connection():
    kite_client = KiteConnect(api_key=API_KEY)
    print(kite_client.login_url())
    # manually get login request URL
    REQUEST_TOKEN = "request_token"
    data = kite_client.generate_session(request_token=REQUEST_TOKEN, api_secret=API_SECRET)
    access_token = data.get("access_token")
    if not access_token:
        print("Error in retrieving access token")
        return
    kite_client.set_access_token(access_token)
    return kite_client





