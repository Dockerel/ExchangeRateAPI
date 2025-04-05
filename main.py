import json, requests, pytz
import datetime as dt

with open("data/data.json", "r") as f:
    json_data = json.load(f)

url = "https://m.search.naver.com/p/csearch/content/qapirender.nhn?key=calculator&pkid=141&q=%ED%99%98%EC%9C%A8&where=m&u1=keb&u6=standardUnit&u7=0&u3=USD&u4=KRW&u8=down&u2=1"

response = requests.get(url)
todayCurrency = (
    response.json().get("country")[1].get("subValue").split()[0].replace(",", "")
)

kst = pytz.timezone("Asia/Seoul")
current_time_kst = dt.datetime.now(kst)
todayDate = str(current_time_kst).split()[0]

json_data[todayDate] = todayCurrency
del json_data[list(json_data.keys())[0]]

with open("data/data.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)
