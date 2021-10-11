# OneMoreAdvice開発

## Docker環境構築
```
$ docker-compose up -d
$ docker-compose up -d --build
$ docker-compose stop
$ docker-compose down --rmi all
```

## ローカル用DBの環境構築
### 1. Docker環境でDBサーバーを稼働させる
```
$ docker-compose up one_more_advice_db
```

### 2. DDLを流し込んでテーブルを作成する
下記のファイルをDB内にインポートする
```
DB/DDL/20210725_DDL_one_more_advice.sql
```

### Docker環境内からローカルDBに接続する方法
下記のコマンドを実行してMySQLのホスト情報を取得する
```sh
$ docker inspect one-more-advice_one_more_advice_db_1
  # このコマンドを実行して取得したjson内の"NetworkSettings"=> "Networks"=>"Gateway"のアドレスがMySQLへの接続に必要なホストとなる。
```
## データ収集基盤の環境構築
### 1. .envファイルの作成
```
$ cp data_collection/env_sample data_collection/.env
```

### 2. Docker環境にログイン
```
$ docker-compose build data_collection
$ docker-compose run data_collection bash
```

### 3. Docker環境内でMakefileを実行
```
$ make hoge
```
