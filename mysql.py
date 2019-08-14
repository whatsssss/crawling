from bs4 import BeautifulSoup
import requests
import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345678' ,db = 'test',charset='utf8mb4')

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

def parse_html_a(html):

    webtoon_list = list()
    soup = BeautifulSoup(html, 'html.parser')
    webtoon_area = soup.find("div",
                             {"id": "cl_body_list"}
                             ).find_all("div", {"class": "ccl-class-name"})
    for webtoon_index in webtoon_area:
        info_soup = webtoon_index.find("a")

        _text = info_soup.text.split(".")
        _title = _text[0]

        webtoon_list.append(_title)

    return webtoon_list

def parse_html_b(html):

    webtoon_list = list()
    soup = BeautifulSoup(html, 'html.parser')
    webtoon_area = soup.find("div",
                             {"id": "cl_body_list"}
                             ).find_all("div", {"class": "ccl-ins-name"})
    for webtoon_index in webtoon_area:
        info_soup = webtoon_index.find("a")

        _text = info_soup.text.split(".")
        _title = _text[0]

        webtoon_list.append(_title)

    return webtoon_list


def parse_html_c(html):

    webtoon_list = list()
    soup = BeautifulSoup(html, 'html.parser')
    webtoon_area = soup.find("div",
                             {"id": "cl_body_list"}
                             ).find_all("div", {"class": "ccl-contents"})
    for webtoon_index in webtoon_area:
        info_soup = webtoon_index.find("a")

        _text = info_soup.text.split(".")
        _title = _text[0]

        webtoon_list.append(_title)

    return webtoon_list



URL = "http://www.learningmen.com/classList;jsessionid=F10DED222F09E747F1286330558624BA?ncs_code_1=20&category_class=1%2c2%2c3%2c4%2c5&category_type=ed&page=1"
html = get_html(URL)


a_1=get_html(URL)

a=parse_html_a(a_1)
b=parse_html_b(a_1)

e=parse_html_c(a_1)


print(a)
print(b)
print(e)
def create_table():
    try:
        with conn.cursor() as cursor:
            sql = '''
                CREATE TABLE cre_tab2 (
                    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    title varchar(255) NOT NULL,
                    academy varchar(255) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

def insert_table():
        try:
            with conn.cursor() as cursor:
                sql = 'INSERT INTO cre_tab2 (title, academy) VALUES (%s, %s)'
                range(0, len(a))
                for i in range(len(a)):
                    cursor.execute(sql, (a[i], b[i]))



            conn.commit()
            print(cursor.lastrowid)
            # 1 (last insert id)
        finally:
            conn.close()


# def select_table():
#     try:
#         with conn.cursor() as cursor:
#             sql = 'SELECT * FROM users WHERE email = %s'
#             cursor.execute(sql, ('test@test.com',))
#             result = cursor.fetchone()
#             print(result)
#             # (1, 'test@test.com', 'my-passwd')
#     finally:
#         conn.close()

def main():


     # create_table()
    insert_table()





if __name__ == "__main__":
    main()
