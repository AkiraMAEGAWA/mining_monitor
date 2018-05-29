import urllib.request, urllib.parse
import configparser
import json

class IftttSender(object):
    def __init__(self):
        inifile = configparser.ConfigParser()
        inifile.read("../config/ifttt_config.ini")
        
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context

# dictをurllib.parseでrequestのdataとすることができる

    def post(event_name=None, api_key=None, where_to_place="M1", message=None, other=None):
        url = "https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(event_name, api_key)
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}
        data = {"value1": where_to_place, "value2": message, "value3": other}
        data = urllib.parse.urlencode(data).encode("utf-8")
        req =urllib.request.Request(url=url, headers=headers) 
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
    api_key = inifile.get("webhook", "api_key")
    event_name = "add_temperature"
    message = "hello world" + input()
    post(event_name=event_name, api_key=api_key, message=message)


