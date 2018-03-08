import requests
import re

regex_min_news_id = re.compile(r'var min_news_id \= "(.*)"')

read = (requests.get("https://www.inshorts.com/en/read").text).encode('utf-8')

# print (re.match(regex_min_news_id, read.encode('utf-8')))

print (re.search(regex_min_news_id, read))

while (True):
	break