import requests
from bs4 import BeautifulSoup
import datetime
import timeInfo
import urllib.parse



def cal_time(param_ymdt):
    one_hour_later_ymdt = param_ymdt + datetime.timedelta(hours=1)
    return one_hour_later_ymdt


#print(realKwd_date[0].text, realKwd_time[0].text)

#kwdDate = realKwd_date[0].text
#kwdYear = kwdDate[:4]
#kwdMonth = kwdDate[5:7]
#kwdDay = kwdDate[8:10]
#convert_date = datetime.datetime.strptime(kwdYear+"-"+kwdMonth+"-"+kwdDay, "%Y-%m-%d").date()

#현재날짜 가져오기
now_ymdt = datetime.datetime.today()
now_minute = now_ymdt.strftime("%m")

#58분일때는 1시간 뒤로 계산함
if(now_minute == "58"):
     now_ymdt = cal_time(now_ymdt)
#날짜 YYYYMMDD
now_date = now_ymdt.strftime("%Y%m%d")
#시간 HH
now_hour = now_ymdt.strftime("%H")



str_headers = {"Content-Type": "text/html",
"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.21022; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
"Cache-Control": "no-cache",
"Cache-Control":"no-store"
}

targetPage ="http://datalab.naver.com/keyword/realtimeList.naver"
req = requests.get(targetPage, headers=str_headers)
html = req.text
soup = BeautifulSoup(html,'html.parser')
realKwd_date = soup.select('#content > div > div.section_serch_area > div > div.date_indo > a.date_box._date_trigger > span.date_txt._title_ymd')
realKwd_time = soup.select('#content > div > div.section_serch_area > div > div.time_indo > a.time_box._time_trigger > span.time_txt._title_hms')
realKwd_ranges = soup.select('#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a ')

#INSERT 변수로 보낼 dictionary
addList ={}

for realKwd in realKwd_ranges :
    #print("순위:{}, 키워드:{}".format(realKwd.find('em').text,realKwd.find('span').text))
    rank = realKwd.find('em').text
    kwd = realKwd.find('span').text
    encode_kwd = urllib.parse.quote(kwd, encoding='UTF-8')

    addList['media_idx'] = 4 # 네이버는 4
    addList['rpt_ymd'] = now_date
    addList['tm'] = now_hour
    addList['link_url'] = "https://search.naver.com/search.naver?where=nexearch&query="+encode_kwd+"&sm=top_lve&ie=utf8"
    addList['keyword'] = kwd
    addList['ranking'] = rank

    #INSERT comm_time info
    result = timeInfo.add_comm_time_info(addList)




