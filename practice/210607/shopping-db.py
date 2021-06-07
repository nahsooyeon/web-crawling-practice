import pymysql
import simplejson as json
import datetime

#MySQL Connection#데이터베이스 선택 연결

conn = pymysql.connect(host='localhost', user='root', password='password', db='python_app1', charset='utf8')

#pymysql 버전 확인
print('pymysql.version:',pymysql.__version__)

#cursor 연결
c = conn.cursor()

# 데이터베이스 생성
c.execute('CREATE DATABASE IF NOT EXISTS naver_db')
#데이터베이스 선택
conn.select_db('naver_db')


# 커서 반환
# c.close()
#
# #접속 해제
# conn.close()
#
# #트랜잭션 시작
# conn.begin()
#
# #커밋
# conn.commit()
#
# #롤백
# conn.rollback()
#
#날짜 생성
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime',nowDatetime)


#테이블 생성(데이터 타입)

c.execute("CREATE TABLE IF NOT EXISTS shopping(product longtext NOT NULL, \
                                               price bigint(20) NOT NULL, \
                                               url VARCHAR(2000) NOT NULL, \
                                               review bigint(20) NOT NULL, \
                                               zzim bigint(20) NOT NULL, \
                                               regdate varchar(256) NOT NULL)" \
                                               )

try:
    with conn.cursor() as c:
        with open('/Users/devpomme/Desktop/네이버쇼핑매크로.json', 'r') as infile:
            r = json.load(infile)
            productData = []
            for product in r:
                p = (product['상품명'], product['가격'], product['URL'], product['리뷰'], product['찜'], nowDatetime )
                productData.append(p)
            c.executemany("INSERT INTO shopping(product, price, url, review, zzim, regdate) VALUES (%s, %s, %s, %s, %s, %s)", productData)
    conn.commit()
finally:
    conn.close()
