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


if len(args) == 2:
    sleep_time = args[1]
    is_horizen = False

elif len(args) == 3:
    sleep_time = args[1]
    is_horizen = args[2]

else:
    sleep_time = 60
    is_horizen = False

#spreadsheetに横並べor縦並べ
if is_horizen:
    for column in [chr(i) for i in range(65,90)]:

        now = datetime.datetime.now()
        event_name = "add_temperature"
 
        message = str(i2c.get_temperature())
        # message += "\n hello from raspi with ifrttt v2 " + str(now.day) + "/" + str(now.hour) + "/" + str(now.minute)

        ifttt.post(event_name=event_name, where_to_place=column + str(1), message=message)
        time.sleep(sleep_time)
        
else:  #vertical
    for row in range(3, 103):
      
        now = datetime.datetime.now()
        event_name = "add_temperature"
   
        message = str(i2c.get_temperature())
       #message += "\n hello from raspi with ifrttt v2 " + str(now.day) + "/" + str(now.hour) + "/" + str(now.minute)
     
       ifttt.post(event_name=event_name, where_to_place= "H" + str(row), message=message)
       time.sleep(sleep_time)
