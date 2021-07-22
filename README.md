# OneMoreAdvice開発

## Docker環境構築
```
$ docker-compose up -d
$ docker-compose up -d --build
$ docker-compose stop
$ docker-compose down --rmi all
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
