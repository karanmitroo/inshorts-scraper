from bs4 import BeautifulSoup
import json

def text_to_json(data, id):
	
	soup = BeautifulSoup(data, 'html.parser')

	all_news = soup.findAll("div", {"class" : "news-card z-depth-1"})

	data = []
	count = len(all_news)
	for each_news in all_news:
		article_body = each_news.find("div", {"itemprop" : "articleBody"}).get_text()
		headline = each_news.find("span", {"itemprop" : "headline"}).get_text()
		try:
			url = each_news.find("a", {"class" : "source"})['href']
		except:
			url = ''
		other_details = each_news.find("div", {"class" : "news-card-author-time news-card-author-time-in-content"})
		
		this_news = {
					'article' : article_body,
					'abstract' : headline,
					'date' : other_details.find("span", {"clas" : "date"}).get_text(),
					'time' : other_details.find("span", {"class" : "time"}).get_text(),
					'source' : url,
					'author' : other_details.find("span", {"class" : "author"}).get_text()
					}
		
		# data.append(this_news)

		file = open(str(id) + '.txt', 'w')
		file.write(article_body.encode('utf8'))
		file.close()
		id = id + 1

	return id
	# with open("result_automobile.json", "aw") as out_file:
	# 	json.dump(data, out_file, indent = 4)
	# 	out_file.close()
