import requests
from bs4 import BeautifulSoup
import lxml
import math

base_url = 'http://clinicaltrials.gov/search?cond=duchenne+muscular+dystrophy&displayxml=true'
r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'xml')

#print(soup.prettify())

#print([child.name for child in soup.children])
#for child in soup.children:
#    for c in child.children:
#        print(c.name)

#for element in soup.find_all('url'):
#    print(element.contents)

count = soup.search_results
print(count['count'])

i = int(count['count']) / 20
print(i)


round = math.ceil(int(count['count']) / 20)
print(round)
i = 1

while True:
    page = requests.get(base_url + '&pg={}'.format(i))
    #print(base_url + '&pg={}'.format(i))
    soup = BeautifulSoup(page.text, 'xml')
    for element in soup.find_all('url'):
        print(element.contents)

    i += 1
    if i >= math.ceil(int(count['count']) / 20):
        break

#for count in soup.find_all('search_results'):
#    print(count.name)
#    print(count.title)
#    print(count.extract())
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.get_text())
