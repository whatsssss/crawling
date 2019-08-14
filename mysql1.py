import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345678' ,db = 'test',charset='utf8mb4')

def create_table():
    try:
        with conn.cursor() as cursor:
            sql = '''
                CREATE TABLE cre_tab2 (
                    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    email varchar(255) NOT NULL,
                    password varchar(255) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

def insert_table(a,b):
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO cre_tab2 (email, password) VALUES (%s, %s)'
            cursor.execute(sql, (a, b))
        conn.commit()
        print(cursor.lastrowid)
        # 1 (last insert id)
    finally:
        conn.close()


def select_table():
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM users WHERE email = %s'
            cursor.execute(sql, ('test@test.com',))
            result = cursor.fetchone()
            print(result)
            # (1, 'test@test.com', 'my-passwd')
    finally:
        conn.close()

def main():

    Label_list = [('가랏zzzz'),('pick')]
    print(Label_list)

    # for i in Label_list:
    #     print(i)



    # insert_table(Label_list[0][0],Label_list[0][1])




if __name__ == "__main__":
    main()
