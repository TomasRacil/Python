[![Actions Status](https://github.com/TomasRacil/Python/workflows/Build%20and%20test/badge.svg)](https://github.com/TomasRacil/Python/actions)

# Web crawler

> A computer program that automatically and systematically searches web pages for certain keywords.

## General info

- Using [Scrapy](https://scrapy.org/) framework to extract relevant data from a webpage.
- Target webpage in this case is [alza.cz/akcni-zbozi](https://alza.cz/akcni-zbozi) and all subsequent pages.

Relevant data extracted:
* Product/Item name
* Price before discount
* Price after discount
* Showed discount perecntage

- Data items saved to a [SQLite3](https://docs.python.org/3/library/sqlite3.html) database.
- Scraper doesn't ignore robot.txt and is set up to not overwhelm the website.

## Usage

- Path to the WebCrawler root directory.
- Execute in terminal to start scraping: `scrapy crawl alzaSpidey`
- Database .db file can be opened using [sqliteonline.com/](https://sqliteonline.com/) web interface.

## Possible expansion

- Analyze database entries for possible mistakes or manipulatiuon.
- Analyze prices in time to detect price spikes and best time to buy.
- Create UI to change scraper parameters.