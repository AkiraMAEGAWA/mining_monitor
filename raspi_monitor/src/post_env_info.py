import IftttSender
import RaspiI2cLogger
import configparser
import datetime

import sys
args = sys.argv

inifile = configparser.ConfigParser()
inifile.read("../config/ifttt_config.ini")
ifttt = IftttSender.IftttSender(api_key=inifile.get("webhook", "api_key"))

i2c = RaspiI2cLogger.RaspiI2cLogger()

now = datetime.datetime.now()
event_name = "add_temperature"
if len(args) <= 1:
    message = str(i2c.get_temperature())
    message += "\n hello from raspi with ifrttt v2 " + str(now.day) + "/" + str(now.hour) + "/" + str(now.minute)
else:
    message = str(args[1:])

for column in [chr(i) for i in range(65,90)]:
    ifttt.post(event_name=event_name, where_to_place=column + str(1), message=message)