import logging
import requests
import time

from urllib.parse import urlencode

import hmac
import hashlib
import typing


logger = logging.getLogger()


class BinanceFuturesClient:
    def __init__(self, public_key: str, secret_key: str, testnet: bool):
        """
        Client for Binance
        :param public_key: {str} API public key
        :param secret_key: {str} API secret key
        :param testnet: {bool} TRUE->testnet FALSE->mainnet
        """
        if testnet:
            self.base_url = "https://testnet.binancefuture.com"
        else:
            self.base_url = "https://fapi.binance.com"

        self.public_key = public_key
        self.secret_key = secret_key

        self.headers = {'X-MBX-APIKEY': self.public_key}

        self.prices = dict()

        logger.info("BINANCE FUTURE CLIENT CONNECTED")

    def _generate_signature(self, data: typing.Dict):
        """
        Function to generate your signature, based on API KEYS and data requirments for binance
        :param data: {Dict} dict of data for binance
        :return: sha 256 hash of your signature for binance
        """
        return hmac.new(self.secret_key.encode(), urlencode(data).encode(), hashlib.sha256).hexdigest()

    def _make_request(self, method: str, endpoint: str, data: typing.Dict):
        """
        Function to request from binance post something, get something, cancel something
        :param method: {str} method for binance POST/GET/CANCEL, ONLY POST IS DONE
        :param endpoint: {str} url endpoint
        :param data: {Dict} dict of data for binance
        :return: None/Error/Json
        """

        if method == "POST":
            response = requests.post(
                self.base_url + endpoint, params=data, headers=self.headers)
        else:
            raise ValueError

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)",
                         method, endpoint, response.json(), response.status_code)
            return None

    def place_order(self, symbol, side, quantity, order_type, price=None, tif=None):
        """
        Function to place order on binance
        :param symbol: {str} currency symbol in uppercase
        :param side: {str} SELL/BUY
        :param quantity: {int} how much you want to buy/sell
        :param order_type: {str} MARKET/STOP/LIMIT
        :param price: {int} price for LIMIT AND STOP order
        :param tif: {int} time in force-> how long order should stay active, only STOP/LIMIT
        :return:
        """
        data = dict()
        data['symbol'] = symbol
        data['side'] = side
        data['quantity'] = quantity
        data['type'] = order_type

        if price is not None:
            data['price'] = price

        if tif is not None:
            data['timeInForce'] = tif

        data['timestamp'] = int(time.time() * 1000)
        data['signature'] = self._generate_signature(data)

        order_status = self._make_request("POST", "/fapi/v1/order", data)

        return order_status
