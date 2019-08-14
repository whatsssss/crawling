#!/usr/bin/env python

# builtin module
from datetime import datetime

# pip install module
import requests
from bs4 import BeautifulSoup
# user defined module

URL_TPL = "http://www.learningmen.com/classList?category_class=1,2,3,4,5&category_type=ed&ncs_code_1=20&tb=%EC%A0%95%EB%B3%B4%ED%86%B5%EC%8B%A0"


def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


def parse_html(html):
    """
   입력받은 마음의 소리 웹툰 페이지 html에서 마음의소리의 회차, 제목 url을 추출하여
   tuple로 만들고, 리스트에 갯수대로 저장하여 반환한다
   :param html: string
   :return: 마음의 소리 정보가 담긴 리스트
   """
    webtoon_list = list()
    soup = BeautifulSoup(html, 'html.parser')
    webtoon_area = soup.find("div",
                             {"id": "cl_body_list"}
                             ).find_all("div", {"class": "ccl-class-name"})
    for webtoon_index in webtoon_area:
        info_soup = webtoon_index.find("a")
        _url = info_soup["href"]
        _text = info_soup.text.split(".")
        _title = ""
        _num = _text[0]
        if len(_text) > 1:
            _title = _text[1]

        webtoon_list.append((_num, '','',))
    return webtoon_list

a=get_html(URL_TPL)
b=parse_html(a)
print(b)
