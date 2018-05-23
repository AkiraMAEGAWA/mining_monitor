from smbus2 import SMBus, SMBusWrapper
import time
import slackweb

import configparser
inifile = configparser.ConfigParser()
inifile.read('../../config/config.ini', 'UTF-8')

i2c = SMBus(1)
address = 0x48

while True:
    try:
        block = i2c.read_i2c_block_data(address, 0x00, 2)
    except OSError as e:
        print("Oops...  change address...")

        if address == 0x48:
            address = 0x49
            print("change address to 0x49")
            continue
        elif address == 0x49:
            address = 0x4b
            print("change address to 0x4b")
            continue
        else:
            address = 0x48
            print("change address to 0x48")
            continue


    val = block[0] << 8
    val = val | block[1]
    val = val >> 3


    if (val >= 4096):
        val = val - 8192

    print("TEMPerature:" + str(val / 16.0) )
    slack = slackweb.Slack(url=inifile.get("slack", "webhook_url"))
    # slack.notify(text=str(val/16.0))
    

    attachments = []
    attachment = {"title": "raspi_temperature", "pretext": "location_1", "text": str(val/16.0)}
    attachments.append(attachment)
    slack.notify(attachments=attachments)
    time.sleep(1)
    time.sleep(599)
