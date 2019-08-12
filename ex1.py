import requests
from bs4 import BeautifulSoup

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

URL = "https://comic.naver.com/webtoon/weekdayList.nhn?week=tue"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')


l = soup.find_all("a")
print(len(l))
# webtoon_area = soup.find("span",{"class": "ccl-class-type class-type-st online"}).find_all("div", {"class":"ccl-ins-name"})
#
# print(webtoon_area)