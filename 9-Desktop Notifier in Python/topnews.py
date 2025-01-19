import requests
import xml.etree.ElementTree as ET

# url of news rss feed
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def load_rss():
	resp = requests.get(RSS_FEED_URL)
	return resp.content

def parse_xml(rss):
	root = ET.fromstring(rss)
	news_items = []

	for item in root.findall('./channel/item'):
		news = {}
		for child in item:
			if child.tag == '{http://search.yahoo.com/mrss/}content':
				news['media'] = child.attrib['url']
			else:
				news[child.tag] = child.text.encode('utf8')
		news_items.append(news)
	return news_items

def top_stories():
	rss = load_rss()
	news_items = parse_xml(rss)
	return news_items
