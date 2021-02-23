# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebcrawlerPipeline(object):

    def __init__(self) -> None:
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("alzaSpidey.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS items_tb""")
        self.curr.execute("""create table items_tb(
                            item text,
                            price text,
                            priceBefore text,
                            discount text
                            )""")

    def store_db(self,item):
        self.curr.execute("""insert into items_tb values (?,?,?,?)""",(
            item['item'][0],
            item['price'][0],
            item['priceBefore'][0],
            item['discount'][0],
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        
        return item
