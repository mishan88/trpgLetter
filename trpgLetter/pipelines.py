# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import boto3
from boto3.session import Session
from scrapy.conf import settings

# When you deploy local
# create '.env' file and write your AWS Access Key ID and Secret Access Key
"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
"""

class TrpgletterPipeline(object):
    def process_item(self, item, spider):
        return item

class DynamoPipeline(object):
    def process_item(self, item, spider):
        # When you deploy local, edit .env
        """
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        session = Session(aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
                          region_name = 'ap-northeast-1')
        """

        # When you deploy on scrapycloud
        session = Session(aws_access_key_id = settings['AWS_ACCESS_KEY_ID'],
                          aws_secret_access_key = settings['AWS_SECRET_ACCESS_KEY'],
                          region_name = 'ap-northeast-1')
        dynamodb = session.resource('dynamodb')
        table = dynamodb.Table('Article')
        table.put_item(
            Item = {
                'url': item['url'],
                'title': item['title'],
                'ID': item['url'] + item['title'] 
            }
        )
