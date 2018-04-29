import urllib.request, urllib.parse, urllib.error
import json
import ssl
import datetime
from bs4 import BeautifulSoup

#SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Set the date range
now_time = datetime.datetime.now()
daysrange = -7
yes_time = now_time + datetime.timedelta(days=daysrange)
start_date = yes_time.strftime('%Y-%m-%d')
end_date = now_time.strftime('%Y-%m-%d')

api_key = "9724cf3522db47c2882c6e2c7c701601"
keyword = "finance"
url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy=popularity&apiKey={}".format(keyword,start_date,end_date,api_key)
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)
#print(json.dumps(info, indent=4))

index = 1
for article in info["articles"]:
    url = article["url"]
    #print(index,article["publishedAt"][:10],article["title"],article["description"])
    index +=1
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)
        print("**********")
    except:
        print("**********")
    print(article["publishedAt"][:10],article["title"])
    
