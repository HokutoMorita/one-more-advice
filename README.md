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

### Sequel proなどでDBに接続するときの情報
```sh
  - ホスト
    - 127.0.0.1
  - ユーザ名
    - root
  - パスワード
    - one_more_advice
  - データベース
    - one_more_advice
  - ポート
    - 4306
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
