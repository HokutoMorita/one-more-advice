import urllib.request, urllib.error
from bs4 import BeautifulSoup
import pandas as pd


STATIC_URL = 'https://teratail.com'
url = 'https://teratail.com/feed/active/1'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

articles = []


def extract_teratail_item():
    teratail_item_df = get_teratail_item()
    return teratail_item_df

def get_teratail_item():
    for data in soup.select('div.boxContentWrap > ul > li'):
        title = data.find('h2').text  # 記事タイトル
        url = STATIC_URL + data.find('h2').a['href']  # 記事URL
        tag_list = data.select('ul.entry-tags > li')  # タグのli要素を取得
        tags = [tag.text.strip() for tag in tag_list]  # タグリスト生成

        article={
            'title':title,
            'url':url,
            'tags':tags
        }
        articles.append(article)
    return pd.DataFrame(articles)
