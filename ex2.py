import requests
from bs4 import BeautifulSoup

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html


URL = "http://www.learningmen.com/classList?category_class=1,2,3,4,5&category_type=ed&ncs_code_1=20&tb=%EC%A0%95%EB%B3%B4%ED%86%B5%EC%8B%A0"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')


webtoon_area = soup.find("div",{"class": "ccl-class-name"})
print(webtoon_area)