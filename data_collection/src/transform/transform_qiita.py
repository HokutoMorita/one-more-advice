import ast
import pandas as pd

from work_flow_logging import work_flow_logging


workflow_logger = work_flow_logging.WorkFlowLogging('logging.cfg')
logger = workflow_logger.logger

def transform_qiita_item():
    """
    Qiitaの投稿データを整形する
    """
    qiita_item_df = pd.read_csv('../data/extracted/extracted_qiita_item.csv')

    qiita_item_df['user_id'] = qiita_item_df['user'].map(extract_user_id)

    required_columns = ['id', 'body', 'coediting', 'comments_count', 
        'likes_count', 'private', 'reactions_count', 
        'title', 'url', 'page_views_count', 'user_id'
    ]
    qiita_item_df = extract_required_columns(qiita_item_df, required_columns)

    rename_target_columns = {
        'id': 'item_id',
        'body': 'text'
    }
    qiita_item_df = rename_columns(qiita_item_df, rename_target_columns)

    return qiita_item_df

def extract_user_id(user_dict_str):
    """
    QiitaユーザーIDを抽出する
    辞書型の文字列を辞書型に変換する
    辞書からQiitaユーザーIDを取得する
    """
    user_dict = ast.literal_eval(user_dict_str)
    return user_dict['id']

def extract_required_columns(df, required_columns):
    """
    データフレームから使用するカラムのみ抽出する
    """
    return df[required_columns]

def rename_columns(df, target__columns):
    """
    データフレームから対象のカラム名を変更する
    """
    return df.rename(columns=target__columns)
