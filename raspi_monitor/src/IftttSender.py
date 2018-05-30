import urllib.request, urllib.parse
import configparser
import json

class IftttSender(object):
    def __init__(self, api_key=None):
        #inifile = configparser.ConfigParser()
        #inifile.read("../config/ifttt_config.ini")
        self.api_key = api_key
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context

# dictをurllib.parseでrequestのdataとすることができる

    def post(self, event_name=None, where_to_place="M1", message="hoge", *args):
        url = "https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(event_name, self.api_key)
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}
        data = {"value1": where_to_place, "value2": message, "value3": args}
        data = urllib.parse.urlencode(data).encode("utf-8")
        
         #URLErrorが発生した場合、1度だけretryする
        try: 
            req = urllib.request.Request(url=url, headers=headers) 
            res = urllib.request.urlopen(req, data=data)
        
        except URLError:
            print("Error Occured...  try one more time")
            req = urllib.request.Request(url=url, headers=headers) 
            res = urllib.request.urlopen(req, data=data)
            
        print(res)

        #data = json.loads(res.read())
        #print(data)

if __name__ == "__main__":
    data = {
      "value1": 30,
      "value2": 35,
      "value3": 40,
    }
    event_name = "add_temperature"
    message = "hello from akira"
    
    inifile = configparser.ConfigParser()
    inifile.read("../config/ifttt_config.ini")
    ifttt = IftttSender(api_key=inifile.get("webhook", "api_key"))
    ifttt.post(event_name=event_name, where_to_place="M1", message=message)


