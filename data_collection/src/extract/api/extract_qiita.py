import os
import requests
import pandas as pd

from work_flow_logging import work_flow_logging


workflow_logger = work_flow_logging.WorkFlowLogging('logging.cfg')
logger = workflow_logger.logger


def extract_qiita_item():
    """
    QiitaのAPIを呼び出して投稿データを取得する
    """
    qiita_item_df = get_qiita_item()
    return qiita_item_df.drop(['tags', 'user'], axis=1)

def get_qiita_item():
    """
    QiitaのAPIから投稿データを取集する
    
    下記の条件から、最大1万件のデータが取得できる
    QiitaのAPIは、1回のレスポンスで最大100件
    ページング番号は100まで
    """
    item_list = []
    # 本番環境では100ページまでデータを取得すること
    # for i in range(1, 101):
    # 開発では速度を重視するため3ページまでのデータを取得する
    for i in range(1, 4):
        url = 'https://qiita.com/api/v2/items?&per_page=100&page={page}'.format(page=i)
        response = request_qiita_data(url)
        result_list = response.json()
        item_list.extend(result_list)
    return pd.DataFrame.from_records(item_list)

def request_qiita_data(url):
    """
    QiitaのAPIを呼び出してデータを取得する
    """
    headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8',
        'Authorization': 'Bearer {}'.format(os.getenv('QIITA_API_KEY'))
    }
    response = requests.get(url=url, headers=headers)
    logger.info('{}, {}'.format(response.status_code, response.url))
    return response
