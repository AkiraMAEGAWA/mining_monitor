import sys
sys.path.append("${Workspace}/worker_monitor/lib/")
import MiningMonitor as mm

import datetime
now = datetime.datetime.now()

eth_monitor = mm.MiningMonitor(_currency="eth")
ltc_monitor = mm.MiningMonitor(_currency="ltc")

if now.minute == 0:
    print(f"---- red worker状況 ----")
    eth_monitor.post2slack(_text=f"---- red worker状況 ----")

else:
    print(f"---- {now.day}日: {now.hour}時: {now.minute}分 ---- \n ---- red worker状況 ----")
    eth_monitor.post2slack(_text=f"---- {now.day}日: {now.hour}時: {now.minute}分 ---- \n ---- red worker状況 ----")


red_ethworkers = eth_monitor.get_red_workers()
print(red_ethworkers)
for i in red_ethworkers:
    eth_monitor.post2slack(_text=f"red worker: {i} \n")
