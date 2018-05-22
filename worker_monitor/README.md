 # 概要
ethermineとlitecoinpoolのdashboardから以下の2点の情報

* 各プールのworker数
* ethermine dashboardで赤になっているworker

を取得し,slackに通知します. 


## 手順

config.ini.exampleをconfig.iniに変更して

* webhook_url
* ethermine_wallet
* litecoinpool_apikey

の3点を書き換えてください
