import os
import json
import traceback
import luigi

from work_flow_logging import work_flow_logging

from extract.api import extract_qiita
from transform import transform_qiita
from load import load_qiita

# Loggingの仕組みの定義
LOGGER = work_flow_logging.WorkFlowLogging('logging.cfg')

class ExtractQiitaItem(luigi.Task):
    """
    Qiitaの投稿データを取得する
    """
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget(self.getOutputFilePath())

    def getOutputFilePath(self):
        return "../finished_file_token/{:s}".format(self.__class__.__name__)

    def run(self):
        LOGGER.task_start('Extract Qiita Item')
        try:
            # Extract
            LOGGER.subtask_start('Extract Qiita Item')
            qiita_item_df = extract_qiita.extract_qiita_item()
            qiita_item_df.to_csv('../data/extracted/extracted_qiita_item.csv', index=False, quoting=1, line_terminator='\r\n')
            LOGGER.subtask_done('Extract Qiita Item')

            with open(self.getOutputFilePath(), 'w') as fout:
                fout.write('\n')
        except:
            LOGGER.traceback(traceback.format_exc())

        LOGGER.task_done('Extract Qiita Item')

class TransformQiitaItem(luigi.Task):
    """
    Qiitaの投稿データを整形する
    """
    def requires(self):
        return [ExtractQiitaItem()]

    def output(self):
        return luigi.LocalTarget(self.getOutputFilePath())

    def getOutputFilePath(self):
        return "../finished_file_token/{:s}".format(self.__class__.__name__)

    def run(self):
        LOGGER.task_start('Transform Qiita Item')
        try:
            # Transform
            LOGGER.subtask_start('Transform Qiita Item')
            qiita_item_df = transform_qiita.transform_qiita_item()
            qiita_item_df.to_csv('../data/transformed/transformed_qiita_item.csv', index=False, quoting=1, line_terminator='\r\n')
            LOGGER.subtask_done('Transform Qiita Item')

            with open(self.getOutputFilePath(), 'w') as fout:
                fout.write('\n')
        except:
            LOGGER.traceback(traceback.format_exc())

        LOGGER.task_done('Transform Qiita Item')

class LoadQiitaItem(luigi.Task):
    """
    Qiitaの投稿データをDBに投入する
    """
    def requires(self):
        return [TransformQiitaItem()]

    def output(self):
        return luigi.LocalTarget(self.getOutputFilePath())

    def getOutputFilePath(self):
        return "../finished_file_token/{:s}".format(self.__class__.__name__)

    def run(self):
        LOGGER.task_start('Load Qiita Item')
        try:
            # Load
            LOGGER.subtask_start('Load Qiita Item')
            load_qiita.load_qiita_item()
            LOGGER.subtask_done('Load Qiita Item')

            with open(self.getOutputFilePath(), 'w') as fout:
                fout.write('\n')
        except:
            LOGGER.traceback(traceback.format_exc())

        LOGGER.task_done('Load Qiita Item')

class TransformQiitaUser(luigi.Task):
    """
    Qiitaのユーザーデータを整形する
    """
    def requires(self):
        return [TransformQiitaItem()]

    def output(self):
        return luigi.LocalTarget(self.getOutputFilePath())

    def getOutputFilePath(self):
        return "../finished_file_token/{:s}".format(self.__class__.__name__)

    def run(self):
        LOGGER.task_start('Transform Qiita User')
        try:
            # Transform
            LOGGER.subtask_start('Transform Qiita User')
            qiita_item_df = transform_qiita.transform_qiita_user()
            qiita_item_df.to_csv('../data/transformed/transformed_qiita_user.csv', index=False, quoting=1, line_terminator='\r\n')
            LOGGER.subtask_done('Transform Qiita User')

            with open(self.getOutputFilePath(), 'w') as fout:
                fout.write('\n')
        except:
            LOGGER.traceback(traceback.format_exc())

        LOGGER.task_done('Transform Qiita User')

class LoadQiitaUser(luigi.Task):
    """
    QiitaのユーザーデータをDBに投入する
    """
    def requires(self):
        return [TransformQiitaUser()]

    def output(self):
        return luigi.LocalTarget(self.getOutputFilePath())

    def getOutputFilePath(self):
        return "../finished_file_token/{:s}".format(self.__class__.__name__)

    def run(self):
        LOGGER.task_start('Load Qiita Item')
        try:
            # Load
            LOGGER.subtask_start('Load Qiita Item')
            load_qiita.load_qiita_user()
            LOGGER.subtask_done('Load Qiita Item')

            with open(self.getOutputFilePath(), 'w') as fout:
                fout.write('\n')
        except:
            LOGGER.traceback(traceback.format_exc())

        LOGGER.task_done('Load Qiita Item')

def main():
    LOGGER.workflow_start()
    luigi.run()
    LOGGER.workflow_done()


if __name__ == '__main__':
    main()
