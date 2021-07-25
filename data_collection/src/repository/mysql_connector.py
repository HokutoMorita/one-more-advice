import os
import pandas as pd
import mysql.connector as mydb
from datetime import datetime as dt
from work_flow_logging import work_flow_logging


workflow_logger = work_flow_logging.WorkFlowLogging('logging.cfg')
logger = workflow_logger.logger


class MySqlConnector:
    '''
    MySqlとの接続、クエリ実行、データ取得をするためのクラス
    '''

    def __init__(self, hostname, user, password, database, port, dictionary=False):
        # RDS接続情報
        self.hostname = hostname
        self.user = user
        self.password = password
        self.database = database
        self.port = port

        self.client = None
        self.con = None
        self.cur = None

        # コネクション作成
        self.con = mydb.connect(
                        host=self.hostname,
                        port=self.port,
                        user=self.user,
                        password=self.password,
                        database=self.database,
                        connection_timeout=600
                    )
        # コネクションが切れた時に再接続してくれるよう設定
        self.con.ping(reconnect=True)
        self.cur = self.con.cursor(dictionary=dictionary)
    
    def update_insert_data_by_df(self, df, table_name, table_columns, chunk_size=1000):
        """
        UPDATE INSERTクエリを実行する
        """
        for column in table_columns:
            if column not in df.columns:
                print(f'Warning: No column "{column}" in dataframe. Null is set.')
                df[column] = None
        columns_str = ', '.join(table_columns)
        value_templates = self.__get_value_templates(table_columns)
        update_value_str = ', '.join([
            f'`{column}` = VALUES(`{column}`)' for column in table_columns
        ])
        update_query = f"""
        INSERT INTO `{table_name}` ({columns_str})
        VALUES ({value_templates})
        ON DUPLICATE KEY UPDATE
            {update_value_str}
        """
        
        # データサイズが大きいケースに備えてchunk単位でupdate
        df_indexed = df.reset_index()
        ## chunk_sizeごとにグループを作り、そのグループ単位でUPDATE INSERTを実行する
        groups = df_indexed.index // chunk_size
        for group, chunk_df in df_indexed[table_columns].groupby(groups):
            update_data = [
                self.__preprocess_update_value(row) for index, row in chunk_df.iterrows()
            ]
            self.cur.executemany(update_query, update_data)
    
    def __get_value_templates(self, columns: list):
        """
        SQL Update Insert時のテンプレートを上書きする (基本は%s)
        
        PythonのINSERT時のテンプレート例
        cur.executemany("INSERT INTO test_table VALUES (%s, %s, %s)", records)
        詳しくはこの資料を参照
        https://qiita.com/valzer0/items/2f27ba98397fa7ff0d74
        """
        print('mysql_connector : __get_value_templates function start')
        templates = []
        for column in columns:
            template = '%s'
            templates.append(template)
        print('mysql_connector : __get_value_templates function done')
        return ', '.join(templates)

    def __preprocess_update_value(self, row: pd.Series):
        """
        SQL Update Insert時のvalueを設定に基づいて上書きする
        PythonのINSERT時のテンプレート例
        cur.executemany("INSERT INTO test_table VALUES (%s, %s, %s)", records)
        詳しくはこの資料を参照
        https://qiita.com/valzer0/items/2f27ba98397fa7ff0d74
        """
        values = []
        for column, value in row.iteritems():
            if pd.isnull(value):
                value = None
            values.append(value)
        return tuple(values)
