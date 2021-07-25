import logging
import logging.config
import os
import requests
import json


class WorkFlowLogging():

    def __init__(self, logger_fpath, debug=False):
        self.logger = logging.getLogger()
        if debug:
            logging.config.fileConfig(logger_fpath, disable_existing_loggers=False)
        else:
            logging.config.fileConfig(logger_fpath)

        # BigQueryを利用する場合のログの制御
        logging.getLogger("googleapiclient.discovery_cache").setLevel(level=logging.ERROR)
        logging.getLogger("googleapiclient.discovery").setLevel(level=logging.ERROR)

    def workflow_start(self):
        msg = '### WORKFLOW START ###'
        self.logger.info(msg)

    def workflow_done(self):
        msg = '### WORKFLOW DONE ###'
        self.logger.info(msg)

    def task_start(self, task_name):
        msg = '=== TASK {} START ==='.format(task_name)
        self.logger.info(msg)

    def task_done(self, task_name):
        msg = '=== TASK {} DONE ==='.format(task_name)
        self.logger.info(msg)

    def subtask_start(self, msg):
        self.logger.info('--- SUBTASK {} START ---'.format(msg))

    def subtask_done(self, msg):
        self.logger.info('--- SUBTASK {} DONE ---'.format(msg))

    def traceback(self, msg):
        self.logger.error('*** TRACEBACK START ***')
        self.logger.error(msg)
        self.logger.error('*** TRACEBACK DONE ***')

if __name__ == '__main__':
    print('=== {} start ==='.format(__file__), flush=True)

    # 環境変数が設定されているかどうかのテスト(正しい値が設定されているかはテストしていない)
    environment_variable_test()

    # 実行方法の確認
    run_examples()
    print('=== {} done ==='.format(__file__), flush=True)
