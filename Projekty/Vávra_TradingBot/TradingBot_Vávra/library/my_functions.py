import config, json, numpy, talib
#  musel jsem instalovat wheel https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
#  pip install TA_Lib-0.4.22-cp37-cp37m-win_amd64.whl

import logging
from connector.binance_future import BinanceFuturesClient #binance testnet connector
#  from binance.client import Client -> ONLY FOR mainet

#IMPORT FROM USER'S CONFIG FILE
closes = []
SOCKET= config.FINAL_WSS   #"wss://stream.binancefuture.com/ws/btcusdt@kline_1m" #normal daily
RSI_PERIOD=config.RSI_PERIOD
RSI_OVERBOUGHT=config.RSI_OVER
RSI_OVERSOLD=config.RSI_UNDER
TRADE_SYMBOL=config.SYMBOL
TRADE_QUANTITY= config.TRADE_QUANTITY
ORDER_TYPE=config.ORDER_TYPE
in_position = False

#LOGGER SETUP
logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

#client2=BinanceFuturesClient(config.API_KEY, config.API_SECRET, True)
#client2.place_order(TRADE_SYMBOL, "BUY", 0.01, "LIMIT", 20000, "GTC")

#client1=BinanceFuturesClient(config.API_KEY, config.API_SECRET, True)
#client1.place_order(TRADE_SYMBOL, "BUY", quantity=0.01, order_type="MARKET")


def _order(side: str, quantity=TRADE_QUANTITY, symbol=TRADE_SYMBOL, order_type=ORDER_TYPE)->bool:
    """
    Function to send order
    :param side: {str} -- BUY/SELL
    :param quantity:{str} -- AMOUNT
    :param symbol: {str} -- SYMBOL OF CURRENCY ("BTCUSDT")
    :param order_type: {str} -- LIMIT/STOP/MARKET
    :return: -- bool
    """

    client2 = BinanceFuturesClient(config.API_KEY, config.API_SECRET, True)
    try:
        print("SENDING ORDER")
        ###########
        client2.place_order(symbol=symbol, side=side, quantity=quantity, order_type=order_type)
        return True
    except:
        return False


def on_open(ws):
    """
    Logger open message
    :param ws:
    :return: None
    """
    logger.info("WS CONNECTION OPENED")


def on_close(ws):
    """
    Logger close message
    :param ws:
    :return: None
    """
    logger.info("WS CONNECTION OPENED")


def on_message(ws, message: str):  # x in Json True-> closing candle
    """
    Function to take kline message, get candle info, trigger _order() if needed
    :param ws:
    :param message: {str} kline Json in string
    :return: None
    """

    global closes
    global in_position

    json_message = json.loads(message)
    candle=json_message['k']
    print("MESSAGE:")
    print("CANDLE CLOSE PRISE ::", candle['c'])
    is_candle_closed=candle['x']
    close=candle['c']

    if is_candle_closed:
        closes.append(float(close))
        logger.info("CLOSES ::  {}".format(closes))

        if len(closes)>RSI_PERIOD:
            np_closes=numpy.array(closes)
            rsi=talib.RSI(np_closes, RSI_PERIOD)  #Period is 14
            print("all rsi calculated")
            last_rsi= rsi[-1]
            logger.info("CURRENT RSI ::  {}".format(last_rsi))

            if last_rsi>RSI_OVERBOUGHT:
                if in_position:
                    # client order sell
                    order_succeded = _order(side="SELL")
                    if order_succeded:
                        in_position=False
                        logger.info("OUT OF POSITION")
                else:
                    print("ALREADY OUT OF POSITION")

            if last_rsi<RSI_OVERSOLD:
                if in_position:
                    print("ALREADY IN POSITION")
                else:
                    #binance logic
                    #client order BUY
                    order_succeded=_order(side="BUY")
                    if order_succeded:
                        in_position=True
                        logger.info("IN POSITION")

