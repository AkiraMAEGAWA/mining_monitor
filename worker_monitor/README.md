 # 概要
ethermineとlitecoinpoolのdashboardから以下の2点の情報

* 各プールのworker数
* ethermine dashboardで赤になっているworker

を取得し,slackに通知します. 

## 動作環境
### 言語
* python3.4 or later

### 使用モジュール
* slackweb
* json
* urllib
* datetime
* configparser
* ssl


## 手順

config.ini.exampleをconfig.iniに変更して

* webhook_url
* ethermine_wallet
* litecoinpool_apikey

の3点を書き換えてください
