import os
import traceback
import pandas as pd
from repository.mysql_connector import MySqlConnector

from work_flow_logging import work_flow_logging


workflow_logger = work_flow_logging.WorkFlowLogging('logging.cfg')
logger = workflow_logger.logger


def load_qiita_item():
    """
    Qiitaの投稿データをDBに投入する
    """
    logger.info('mysql connect start')
    try:
        mysql_connector = MySqlConnector(
            hostname=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT'),
        )
    except:
        logger.error('mysql connect failed')
        logger.error(traceback.format_exc())
    logger.info('mysql connect done')
    qiita_item_df = pd.read_csv('../data/transformed/transformed_qiita_item.csv')
    table_name = 'qiita_item'
    table_columns = [
        'item_id', 'text', 'coediting', 'comments_count', 
        'likes_count', 'private', 'reactions_count', 
        'title', 'url', 'page_views_count', 'user_id'
    ]

    logger.info('mysql execute query start')
    try:
        mysql_connector.update_insert_data_by_df(qiita_item_df, table_name, table_columns)
        mysql_connector.con.commit()
    except:
        logger.error('mysql execute query failed')
        logger.error(traceback.format_exc())
    finally:
        mysql_connector.cur.close()
        mysql_connector.con.close()
    logger.info('mysql execute query done')

def load_qiita_user():
    """
    QiitaのユーザーデータをDBに投入する
    """
    logger.info('mysql connect start')
    try:
        mysql_connector = MySqlConnector(
            hostname=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT'),
        )
    except:
        logger.error('mysql connect failed')
        logger.error(traceback.format_exc())
    logger.info('mysql connect done')
    qiita_user_df = pd.read_csv('../data/transformed/transformed_qiita_user.csv')
    table_name = 'qiita_user'
    table_columns = [
        'user_id', 'description', 'facebook_id', 'followees_count', 'followers_count',
        'github_login_name', 'items_count', 'linkedin_id', 'location',
        'name', 'organization', 'permanent_id', 'profile_image_url',
        'team_only', 'twitter_screen_name', 'website_url'
    ]

    logger.info('mysql execute query start')
    try:
        mysql_connector.update_insert_data_by_df(qiita_user_df, table_name, table_columns)
        mysql_connector.con.commit()
    except:
        logger.error('mysql execute query failed')
        logger.error(traceback.format_exc())
    finally:
        mysql_connector.cur.close()
        mysql_connector.con.close()
    logger.info('mysql execute query done')

def load_qiita_tag():
    """
    QiitaのタグデータをDBに投入する
    """
    logger.info('mysql connect start')
    try:
        mysql_connector = MySqlConnector(
            hostname=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT'),
        )
    except:
        logger.error('mysql connect failed')
        logger.error(traceback.format_exc())
    logger.info('mysql connect done')
    qiita_tag_df = pd.read_csv('../data/transformed/transformed_qiita_tag.csv')
    table_name = 'qiita_tag_master'
    table_columns = [
        'tag_name'
    ]

    logger.info('mysql execute query start')
    try:
        mysql_connector.update_insert_data_by_df(qiita_tag_df, table_name, table_columns)
        mysql_connector.con.commit()
    except:
        logger.error('mysql execute query failed')
        logger.error(traceback.format_exc())
    finally:
        mysql_connector.cur.close()
        mysql_connector.con.close()
    logger.info('mysql execute query done')

def load_qiita_item_to_tag():
    """
    Qiitaの投稿データとタグデータの関連データをDBに投入する
    """
    logger.info('mysql connect start')
    try:
        mysql_connector = MySqlConnector(
            hostname=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT'),
        )
    except:
        logger.error('mysql connect failed')
        logger.error(traceback.format_exc())
    logger.info('mysql connect done')
    qiita_item_to_tag_df = pd.read_csv('../data/transformed/transformed_qiita_item_to_tag.csv')
    table_name = 'qiita_item_to_tag_relation'
    table_columns = [
        'item_id', 'tag_name'
    ]

    logger.info('mysql execute query start')
    try:
        mysql_connector.update_insert_data_by_df(qiita_item_to_tag_df, table_name, table_columns)
        mysql_connector.con.commit()
    except:
        logger.error('mysql execute query failed')
        logger.error(traceback.format_exc())
    finally:
        mysql_connector.cur.close()
        mysql_connector.con.close()
    logger.info('mysql execute query done')


