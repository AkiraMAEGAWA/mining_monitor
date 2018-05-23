# 概要
raspberry pi3 を用いたマイニングファーム温度監視ツールです。

## 環境
### 言語
* python3.4 or later

### module
* slackweb
* 

## 手順
*pythonのmoduleであるslackwebをinstallする
- pip install -r requirements.txt

*  raspiにADT7410を接続する
この時、SDAやSCLに注意すること

* raspi_temperature.pyを実行する
- python3 /mining_monitor/raspi_monitor/src/raspi_temperature.py
環境によって少し変更してください
