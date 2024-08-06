# -*- coding: utf-8 -*-
"""dblp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kytQUVYaXXJWGH4NhPiG5Kk_B_hBhcJg

## Code crawling for dblp

* Keyword: trust|distrust|trustworthiness software develop|engineer ai|intelligence|language

* 13 results
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from ast import keyword

from google.colab import drive
drive.mount('/content/drive')

results = {
    'author': [],
    'title': [],
    'journal': [],
    'volume': [],
    'number': [],
    'pages': [],
    'year': [],
    'url': [],
    'doi': [],
    'timestamp': [],
    'biburl': [],
    'bibsource': [],
    'editor': [],
    'booktitle': [],
    'publisher': [],
    'eprinttype': [],
    'eprint': [],
    'series': []
}

try:
  url=('https://dblp.org/search?q=trust%7Cdistrust%7Ctrustworthiness%20software%20develop%7Cengineer%20ai%7Cintelligence%7Clanguage')
  content = requests.get(url).text
  page = BeautifulSoup(content, 'html.parser')

  for entry in page.find_all('nav', attrs={'class': "publ"}):
    bib=entry.find_all('li', attrs={'class': "drop-down"})[1]
    bib_a=bib.find('div', attrs={'class': "head"}).find('a')['href']

    bib_content=requests.get(bib_a).text
    bib_page=BeautifulSoup(bib_content, 'html.parser')
    bib_text=bib_page.find('pre', {'class':'verbatim select-on-click'}).text.strip()
    lines=bib_text.replace('\n', ' ').split(',')
    for line in lines:
      if '=' in line:
        key,value = map(str.strip, line.split('='))
        key =key.strip()
        value=value.strip().replace('{', '').replace('}', '')
        if key in results:
          results[key].append(value)
        else:
          results[key].append("DNE")
except:
    print("An exception occurred")
GS_df = pd.DataFrame(results)

GS_df.to_csv('/content/drive/MyDrive/Paper_crawing/GS_data.csv', index=False)