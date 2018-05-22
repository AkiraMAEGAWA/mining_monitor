import configparser
inifile = configparser.ConfigParser()
inifile.read('../config.ini', 'UTF-8')

pwd = inifile.get("path", "pwd")

import sys
sys.path.append(pwd)
import MiningMonitor as mm

import datetime
now = datetime.datetime.now()

eth_monitor = mm.MiningMonitor(_currency="eth")
ltc_monitor = mm.MiningMonitor(_currency="ltc")

if now.minute == 0:
    print("---- red worker状況 ----")
    eth_monitor.post2slack(_text="---- red worker状況 ----")

else:
    # print(f"---- {now.day}日: {now.hour}時: {now.minute}分 ---- \n ---- red worker状況 ----")
    # eth_monitor.post2slack(_text=f"---- {now.day}日: {now.hour}時: {now.minute}分 ---- \n ---- red worker状況 ----")
    print("---- {0}日: {1}時: {2}分 ---- \n ---- red worker状況 ----".format(now.day, now.hour, now.minute))
    eth_monitor.post2slack(_text="---- {0}日: {1}時: {2}分 ---- \n ---- red worker状況 ----".format(now.day, now.hour, now.minute))


red_ethworkers = eth_monitor.get_red_workers()
print(red_ethworkers)
for i in red_ethworkers:
    # eth_monitor.post2slack(_text=f"red worker: {i} \n")
    eth_monitor.post2slack(_text="red worker: {0} \n".format(i))
