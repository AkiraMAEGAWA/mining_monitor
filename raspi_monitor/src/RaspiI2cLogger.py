from smbus2 import SMBus, SMBusWrapper
import time
import slackweb

import configparser
inifile = configparser.ConfigParser()
inifile.read('../../config/config.ini', 'UTF-8')

class RaspiI2cLogger(object):
    def __init__(self):
        self.i2c = SMBus(1)
        self.address = 0x48
   
    def is_address_exist(self):
        try:
            block = self.i2c.read_i2c_block_data(self.address, 0x00, 2)
        except OSError as e:
            print("Oops...  change address...")

            if self.address == 0x48:
                self.address = 0x49
                print("change address to 0x49")
                return False
            elif self.address == 0x49:
                self.address = 0x4b
                print("change address to 0x4b")
                return False
            else:
                self.address = 0x48
                print("change address to 0x48")
                return False
        
        return True


    def get_temperature(self):
        if is_address_exist():
            val = block[0] << 8
            val = val | block[1]
            val = val >> 3

            if (val >= 4096):
                val = val - 8192

            print("TEMPerature:" + str(val / 16.0))
            return (val/16.0)
        else:
            print("using invalid address")           
            return "invalid"

    def logging(self):
        while True:
            print(get_temperature())
            #for notifing to slack
            #slack = slackweb.Slack(url=inifile.get("slack", "webhook_url"))
            #slack.notify(text=str(val/16.0))
            #attachments = []
            #attachment = {"title": "raspi_temperature", "pretext": "location_1", "text": str(val/16.0)}
            #attachments.append(attachment)
            #slack.notify(attachments=attachments)

            #time.sleep(1)
            #time.sleep(599)
            time.sleep(5)

if "__name__" == "__main__":
    i2c = RaspiI2cLogger()
    i2c.logging()
        
