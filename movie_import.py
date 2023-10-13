from db_conn import *
import pandas as pd
import numpy as np  # numpy 라이브러리 추가
import re

file_name = 'top_movies.csv'
df = pd.read_csv(file_name)

# 데이터프레임 열 이름 수정
df.columns = ['id', 'movie_name', 'release_year', 'watch_time', 'movie_rating', 'metascore', 'gross', 'votes', 'description']

# 데이터 형식 변환
df['watch_time'] = df['watch_time'].astype(int)
df['movie_rating'] = df['movie_rating'].astype(float)

# 'metascore' 열에서 NaN값을 처리
df['metascore'] = df['metascore'].replace([np.nan, np.inf, -np.inf], 0).astype(int)

df['gross'] = df['gross'].str.replace('[^\d,]', '', regex=True)  # 숫자와 쉼표(,) 이외의 문자 제거
df['gross'] = df['gross'].str.replace(',', '').astype(float)  # 쉼표(,) 제거하고 부동 소수점으로 변환
df['votes'] = df['votes'].str.replace(',', '').astype(int)  # 쉼표(,) 제거하고 정수로 변환
df['gross'] = df['gross'].fillna(0)
#'II 2018'와 같은 부적절한 값이 'release_year' 열에 있어서 발생한 오류 
#정규 표현식 (\d+)을 사용하여 숫자를 추출하여 해결
df['release_year'] = df['release_year'].str.extract('(\d+)').astype(int)


insert_sql = """INSERT INTO top_movie (id, movie_name, release_year,
                    watch_time, movie_rating, metascore, gross, votes, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

conn, cur = open_db('db2023')

truncate_sql = """TRUNCATE TABLE top_movie;"""
cur.execute(truncate_sql)
conn.commit()

for index, r in df.iterrows():
    t = (r['id'], r['movie_name'], r['release_year'], r['watch_time'],
         r['movie_rating'], r['metascore'], r['gross'], r['votes'], r['description'])
    try:
        cur.execute(insert_sql, t)
    except Exception as e:
        print(t)
        print(e)
        break

conn.commit()
close_db(conn, cur)
