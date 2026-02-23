#! python3
# lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com//search?=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    print(f'Problem: {exc}')

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result
link_elems = soup.select('.r a')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http:/google.com' + link_elems[i].get('href'))
