from bs4 import BeautifulSoup
import requests
import re
import json
from text_to_json import text_to_json

def get_min_news_id(response):
    
    try:
        regex_min_news_id = re.compile('var min_news_id = "(.*?)";')
        min_news_id = regex_min_news_id.search(response.text).group(1)    
    except:
        min_news_id = json.loads(response.text)['min_news_id']
    return min_news_id
    
regex_min_news_id = re.compile('var min_news_id = "(.*?)";')    


url = "https://www.inshorts.com/en/read"
request = requests.get(url)
min_news_id = regex_min_news_id.search(request.text).group(1)
text_to_json(request.text)

page_number = 0
while (True):
    url = "https://www.inshorts.com/en/ajax/more_news"
    request = requests.post(url, data={'news_offset' : min_news_id})

    min_news_id = json.loads(request.text)['min_news_id']
    with open('min_news_id.txt', 'aw') as min_news_id_file:
        min_news_id_file.write(min_news_id + ' - ' + str(page_number) + '\n')
        min_news_id_file.close()
        
    text_to_json(json.loads(request.text)['html'])
    page_number += 1
    print (page_number)


