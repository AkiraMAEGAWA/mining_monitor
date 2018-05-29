import IftttSender
import configparser
import datetime

import sys
args = sys.argv

now = datetime.datetime.now()

event_name = "add_temperature"
if len(args) <= 1:
    message = "hello from raspi with ifrttt v2 " + str(now.day) + "/" + str(now.hour) + "/" + str(now.minute)
else:
    message = str(args[1:])

inifile = configparser.ConfigParser()
inifile.read("../config/ifttt_config.ini")
ifttt = IftttSender.IftttSender(api_key=inifile.get("webhook", "api_key"))
ifttt.post(event_name=event_name, where_to_place="M1", message=message)

