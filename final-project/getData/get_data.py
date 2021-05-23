import urllib.request, requests
from pprint import pprint
import json

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=db9a0fbc483652a8365d7dd0cbbed704&targetDt=20200220'
res = requests.get(url)
text = res.text

d = json.loads(text)

movieList = []



for b in d['boxOfficeResult']['dailyBoxOfficeList']:
    print(b['movieNm'])
