from bs4 import BeautifulSoup
import requests
import pymysql

URL_TPL = "http://www.learningmen.com/classList?category_class=1,2,3,4,5&category_type=ed&ncs_code_1=20&tb=%EC%A0%95%EB%B3%B4%ED%86%B5%EC%8B%A0"

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


def parse_html(html):

    webtoon_list = list()
    soup = BeautifulSoup(html, 'html.parser')
    webtoon_area = soup.find("div",
                             {"id": "cl_body_list"}
                             ).find_all("div", {"class": "ccl-class-name"})
    for webtoon_index in webtoon_area:
        info_soup = webtoon_index.find("a")

        _text = info_soup.text.split(".")
        _title = _text[0]

        webtoon_list.append([_title])

    return webtoon_list

def main():

    Label_list = []

    a = get_html(URL_TPL)
    b = parse_html(a)
    print(b)

    html = parse_html(URL_TPL)
        soup = BeautifulSoup(html, 'html.parser')

        for i in s:
            n = 0
            element_list = list()
            conn = pymysql.connect(
                host   = "localhost",
                user   = "root",
                passwd = "1234",
                db     = "malware",
                charset= "utf8"
            )
            curs = conn.cursor() # 객체 생성
            for x in i.find_all(name='td'):
                print (Label_list[n],":", x.string)
                n = (n+1)%len(Label_list)
                element_list.append(x.string)
                if len(element_list) == 7:
                    sql = """insert into hash(Data, Domain, IP, CC, ASN, Autom_system_name, Virus_Total_MD5) 
                    values(%s, %s, %s, %s, %s, %s, %s)"""
                    curs.execute(sql, (element_list[0],element_list[1],element_list[2],
                                       element_list[3],element_list[4],element_list[5],
                                       element_list[6]))
                    element_list.clear()
                    conn.commit()
            conn.close()
            print ("=============================")
        #print (soup)
        # L = soup.find_all(name='a')
        # for i in L:
        #     #print (i.attrs['href'])
        #     if "https" in i.attrs['href']:
        #         print (i.string)
if __name__ == "__main__":
    main()

