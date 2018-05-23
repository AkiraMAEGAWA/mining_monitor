import configparser
inifile = configparser.ConfigParser()
inifile.read('../../config/config.ini', 'UTF-8')

pwd = inifile.get("path", "pwd")

import sys
sys.path.append(pwd)
import MiningMonitor as mm


import datetime
now = datetime.datetime.now()

eth_monitor = mm.MiningMonitor(_currency="eth")
ltc_monitor = mm.MiningMonitor(_currency="ltc")

active_ethworkers = eth_monitor.get_eth_currentacitiveworkers()
active_ltcworkers = ltc_monitor.get_ltc_currentacitiveworkers()
print("ethminerのworker数は {0} です".format(active_ethworkers))
print("ltcminerのworker数は {0} です".format(active_ltcworkers))
# eth_monitor.post2slack(_text=f"ethminerのworker数は {active_ethworkers} です")
# ltc_monitor.post2slack(_text=f"ltcminerのworker数は {active_ltcworkers} です")
eth_monitor.post2slack(_text="ethminerのworker数は {0} です".format(active_ethworkers))
ltc_monitor.post2slack(_text="ltcminerのworker数は {0} です".format(active_ltcworkers))
