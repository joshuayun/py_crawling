import json
import requests


str_headers = {"Content-Type": "text/html",
"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.21022; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
"Cache-Control": "no-cache",
"Cache-Control":"no-store"
}


targetPage ="http://m.11st.co.kr/MW/html/mainTabData/mobileWeb_HOME.json"
req = requests.post(targetPage, headers=str_headers)
html = req.text
html_json = json.loads(html)
jsonDataList = html_json["data"]

for jsonData in jsonDataList:
    blockList = jsonData['blockList']
    for block in blockList:
        typeNm = block['type']
        if(typeNm == "ContentsScroll_KeywordRanking"):
            list = block['list']
            listOne = list[0]
            items = listOne['items']
            for item in items:
               print("순위:{}, 키워드:{}".format(item['rank'],item['title1']))












