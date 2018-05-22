import sys
sys.path.append("${Workspace}/worker_monitor/lib/")
import MiningMonitor as mm


import datetime
now = datetime.datetime.now()

eth_monitor = mm.MiningMonitor(_currency="eth")
ltc_monitor = mm.MiningMonitor(_currency="ltc")

active_ethworkers = eth_monitor.get_eth_currentacitiveworkers()
active_ltcworkers = ltc_monitor.get_ltc_currentacitiveworkers()

print(f"--{now.day}日: {now.hour}時:  {now.minute}分 ---- \n ---- active worker状況 ---- ")
eth_monitor.post2slack(_text=f"--{now.day}日: {now.hour}時: {now.minute}分 ---- \n ----activeworker状況---")

print(f"ethminer worker: {active_ethworkers}")
print(f"ltcminer worker: {active_ltcworkers}")
eth_monitor.post2slack(_text=f"ethminer worker:  {active_ethworkers}")
ltc_monitor.post2slack(_text=f"ltcminer worker:  {active_ltcworkers}\n")

