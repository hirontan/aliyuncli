# README

## `Image`からサーバを作成する

### 実行環境
- MAC or Linux

### 実行事前準備（Python2.7.10で実行しています）
- `aliyun` は Python3 で実行できる環境は整っていそうだが、まだ安定稼働していないように思えるので、今回は利用していません
```
$ pip install aliyun-python-sdk-core
$ pip install aliyun-python-sdk-ecs
→必要なライブラリをインストール
$ pip install logging
$ pip install retry
$ pip install argparse
```

- スクリプト内の[instance_id]などは各自設定お願いします

### 実行方法
```
$ cd [実行ディレクトリ]
$ python exec.py --region [ap-northeast-1] --key [api key] --access [api access key] --image [image id]
```
