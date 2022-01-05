# Krypto trader

Program, jenž na základě RSI nakupuje/prodává pozice v rámci libovolně zvolené kryptoměny

Před spuštěním:

1. vygenerovat si vlastní API_KEYS na testnet.binancefuture.com (PUBLIC a SECRET KEY)
2. naistahovat knihovny, co nemáte potřebné k projektu
3. stáhnout wheel od TA-Lib, https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib pro zprovoznění talib knihovny
4. vyberte si podle své verze pythonu a windows (TA_Lib-0.4.22-cp37-cp37m-win_amd64.whl->python3.7, windows 64b)
5. rozbalte wheel přímo do projektu na úrovni mainu
6. pip install TA_Lib-0.4.22-cp37-cp37m-win_amd64.whl (nebo jiný wheel whodný pro vás)
7. nainstalovat python-dotenv-> schová api klíče proti pushnutí do githubu ->enviroment variable (pip install python-dotenv)
9. vytvoření složky .env do které dáme API_KEY= váš publlic key a SECRET_KEY= váš secret key (na main úrovni)

Obsluha:

- v config #INPUT si zadáte parametry dle své potřeby
- vytvoříte si vlastní .env kam dáte API_KEY a SECRET_KEY

Nápady do budoucna:

- více strategií
- více burz+převody mezi nimi
- více měn zaráz
- UI

## TODO

- Lépe definovat kroky potřebné kzprovoznění traderu především část spojenou s technical analysis library (TA-Lib).
