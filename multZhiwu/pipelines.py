# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
import MySQLdb
import MySQLdb.cursors

class MultzhiwuPipeline(object):
    def process_item(self, item, spider):
        return item


class CatePipelinePipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):

        print(item)

        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)

        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    # 将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        for k in range(0, len(item)):
            conn.execute("""
                    insert into cate(name,cid, img_url,source_link)
                    values(%s, %s, %s, %s)
                """, (123, 123,123,123) )
    # 异常处理
    def _handle_error(self, failue, item, spider):
        log.err(failure)
