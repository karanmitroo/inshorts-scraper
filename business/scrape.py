from bs4 import BeautifulSoup
import requests
import re
import json
from text_to_json import text_to_json

    
regex_min_news_id = re.compile('var min_news_id = "(.*?)";')
url = "https://www.inshorts.com/en/read/business"
request = requests.get(url)
min_news_id = regex_min_news_id.search(request.text).group(1)   #This has to be sent as a parameter while sending a new request.
# print request.text
id = text_to_json(request.text, 1)

page_number = 0
while (True):
    url = "https://www.inshorts.com/en/ajax/more_news"
    request = requests.post(url, data={'news_offset' : min_news_id , 'category' : 'business'})
    id = text_to_json(json.loads(request.text)['html'], id)

    min_news_id = json.loads(request.text)['min_news_id']   #Find min_news_id for the next page.
    
    """
    A small log system to store the number of pages it has scraped
    and also their min_news_id respectively
    """
    
        


