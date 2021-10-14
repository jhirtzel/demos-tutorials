#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,features="lxml")

response = open('search_response.html','w')
response.write(soup.prettify())
response.close()

# TODO: Open a browser tab for each result
linkElems = soup.select('.kCrYT a')
print(f'there were {len(linkElems)} elements')

numToOpen = min(3, len(linkElems))
for i in range(numToOpen):
	print('http://www.google.com'+linkElems[i].get('href'))
	webbrowser.open('http://www.google.com'+linkElems[i].get('href'))