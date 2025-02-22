# -*- coding: utf-8 -*-
"""ACM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oF_1krRXRHehH5L3fw8d0NVHyt_gZt8K

## Code crawling for ACM

* Keyword: (“trust” OR “distrust” OR “trustworthiness”) AND (“SE” OR “Software Engineering”) AND (“LLM” OR “Large Language Model” OR “LLMs” OR “Large Language Models” OR “Deep Learning” OR “Machine Learning”)

* result-> 2,001
* removing duplicates-> 1,923
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from ast import keyword

from google.colab import drive
drive.mount('/content/drive')

import requests
from bs4 import BeautifulSoup
import pandas as pd
from ast import keyword
results = []
# ACM's page number start with 1
i = 0 #pagination start
while i < 61: # pagination end
        try:
            url= ('https://dl.acm.org/action/doSearch?AllField='
            +'%28%E2%80%9Ctrust%E2%80%9D+OR+%E2%80%9Cdistrust%E2%80%9D+OR+%E2%80%9Ctrustworthiness%E2%80%9D%29+AND+%28%E2%80%9CSE%E2%80%9D+OR+%E2%80%9CSoftware+Engineering%E2%80%9D%29+AND+%28%E2%80%9CLLM%E2%80%9D+OR+%E2%80%9CLarge+Language+Model%E2%80%9D+OR+%E2%80%9CLLMs%E2%80%9D+OR+%E2%80%9CLarge+Language+Models%E2%80%9D+OR+%E2%80%9CDeep+Learning%E2%80%9D+OR+%E2%80%9CMachine+Learning%E2%80%9D%29'
            +'&pageSize=50&startPage='+str(i)+'&pageSize=50')
            content = requests.get(url).text
            page = BeautifulSoup(content, 'lxml')
            for entry in page.find_all("div", attrs={"class": "issue-item issue-item--search clearfix"}):
                content_type = entry.find('div', attrs={'class': 'issue-heading'})
                date = entry.find('div',attrs={'class':'bookPubDate simple-tooltip__block--b'})
                title = entry.find('h5', attrs={'class': 'issue-item__title'})
                author = entry.find('ul', attrs={'class': 'rlist--inline'})
                detail = entry.find('div', attrs={'class': 'issue-item__detail'})
                abst = entry.find('div',attrs={'class':'issue-item__abstract'})
                if detail:
                  conference = detail.find('a')

                results.append({"title": title.text.replace('[PDF]',''),
                                "url":'https://dl.acm.org'+entry.a['href'],
                                'authors':author.text.replace('\n',''),
                                'date':date.text.strip(),
                                'content type':content_type.text.strip(),
                                'conference':conference.text.strip(),
                                'abstract':abst.text.replace('\n','')})
        except:
            print("An exception occurred")
            print(i)
            ##print(year[y])
        i=i+1

ACM_df = pd.DataFrame(results)

ACM_df.head(5)

ACM_df.to_csv('/content/drive/MyDrive/Paper_crawing/ACM_data.csv', index=False)