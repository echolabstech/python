from lxml import html
import requests
from bs4 import BeautifulSoup

url = 'http://www.cedia.org/lib/aptify/submit_find_a_pro_data.php'
data = {
				'country':'USA',
				'postcode':'48108',
				'distance':'250',
				'countries_additional':'USA,Australia,Canada,UK,UnitedKingdom',
				'category':'',
				'email':'',
				}
headers = {'Content-Type':'application/x-www-form-urlencoded'}
response = requests.post(url, data=data, headers=headers)
cookie = response.headers.get('Set-Cookie')
cookie = cookie.split(';')
cookie = cookie[0] + ';' + cookie[1].split(',')[1]

url = 'http://www.cedia.org/lib/aptify/get_search_results.php'
headers = {
						'Cookie':cookie,
						'Accept':'application/json, text/javascript, */*; q=0.01',
						'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
					}
response = requests.post(url, headers=headers)
page = html.fromstring(response.content)
results = page.find_class('finder-results-member clearfix member-certified')
results = page.xpath('//div[@class="finder-results-member clearfix member-certified"]/text()')
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find(class_="finder-results-member clearfix member-certified"))