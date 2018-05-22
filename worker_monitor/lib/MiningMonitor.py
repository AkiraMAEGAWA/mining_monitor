class MiningMonitor(object):
    """
    マイニングプールの監視クラスです。
    
    プール名に応じて、インスタンス時に_currency = "eth" or "ltc" or..  
    を指定してください。
    
    """


    def __init__(self, _currency="eth"):
        import slackweb
        import json
        import urllib.request
        from datetime import datetime
       
        # bitfly' のapiはsslの証明書を要求してくるが、その回避用
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context


        self.slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
        # 参考ページ  https://ja.stackoverflow.com/questions/27922/python3%E3%81%A7web%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0%E3%81%97%E3%81%9F%E3%81%84%E3%81%AE%E3%81%A7%E3%81%99%E3%81%8C%E5%AD%98%E5%9C%A8%E3%81%99%E3%82%8Burl%E3%81%8C%E9%96%8B%E3%81%91%E3%81%BE%E3%81%9B%E3%82%93
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}

        if _currency == "eth":
            self.eth_url = 'https://api.ethermine.org/miner/"515CE20480D546BcbD3cd2c9f7e180e374DAE44a"/dashboard'
            self.request = urllib.request.Request(url=self.eth_url, headers=self.headers)
            self.res = urllib.request.urlopen(self.request)
            self.eth_data = json.loads(self.res.read().decode('utf-8'))

        elif _currency == "ltc":
            self.ltc_url = 'https://www.litecoinpool.org/api?api_key=84aea38648cf63ad05aa7175a166edf4'
            self.request = urllib.request.Request(url=self.ltc_url, headers=self.headers)
            self.res = urllib.request.urlopen(self.request)
            self.ltc_data = json.loads(self.res.read().decode('utf-8'))

        	
        


    # 各currencyごとのworker数をgetします    
    def get_eth_currentacitiveworkers(self):
        return (self.eth_data["data"]["currentStatistics"]["activeWorkers"])


    def get_ltc_currentacitiveworkers(self):
        num_worker = 0
        for _worker in self.ltc_data["workers"]:
            #ハッシュのハッシュの処理が少し面倒でした
            if self.ltc_data["workers"][_worker]["connected"]:
                num_worker += 1

        return num_worker 



    def get_red_workers(self, _deadline=1200):
        """
        DEADLINE秒(default:3600秒)以上プールに認識されていないworker(lost_worker)を
        取得します。
        
        params:
          _deadline: いい感じの閾値にしてください

        const: 
          DEADLINE

        return: 
          _lost_worker: lostしたworker番号のlist
            or 
          ["nothing"]: ないことを意味する文字列 " nothing " を含んだリスト

        """
        DEADLINE = _deadline  # 3600 sec
        workers = self.eth_data["data"]["workers"]
        #json dataはdataがstatisticsを子に持ち、statisticsは降順に新しいデータとなる 
        latest_stats_time = self.eth_data["data"]["statistics"][-1]["time"]
        red_workers = []

        for worker in workers:
            # print(latest_stats_time - worker["lastSeen"])
            if latest_stats_time - worker["lastSeen"] > DEADLINE:
                print(worker["worker"])
                red_workers.append(worker["worker"])
        

        return red_workers if len(red_workers) > 0 else [" nothing "]


    def post2slack(self, _text):
        """
        slackに任意の文字列をポストできます

        params: 
            _text  ポストする文字列
        """
        self.slack.notify(text=_text)



if __name__ == "__main__":

    eth_monitor = MiningMonitor(_currency="eth")
    ltc_monitor = MiningMonitor(_currency="ltc")

    active_ethworkers = eth_monitor.get_eth_currentacitiveworkers()
    active_ltcworkers = ltc_monitor.get_ltc_currentacitiveworkers()
    print(f"ethminerのworker数は {active_ethworkers} です")
    print(f"ltcminerのworker数は {active_ltcworkers} です")
    eth_monitor.post2slack(_text=f"ethminerのworker数は {active_ethworkers} です")
    ltc_monitor.post2slack(_text=f"ltcminerのworker数は {active_ltcworkers} です")

    red_ethworkers = eth_monitor.get_red_workers()
    print(red_ethworkers)
    for i in red_ethworkers:
        eth_monitor.post2slack(_text=f"red worker: {i}\n")