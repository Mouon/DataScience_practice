import pandas as pd
import mysql.connector
import pymysql

# 1. 엑셀 파일 읽기
df = pd.read_excel('/Users/munhyeonjrn/\\movies.xls',  converters={'장르': str})

# 2. MySQL 데이터베이스에 연결
cnx = mysql.connector.connect(user='root', 
                              password='mhj881610!', 
                              host='localhost', 
                              database='movie_db')
cursor = cnx.cursor()

# 3. 각 테이블 생성
create_movies_table_query = """

CREATE TABLE Movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    title_en VARCHAR(255),
    year INT,
    type VARCHAR(255),
    status VARCHAR(255)
);
"""
create_directors_table_query = """
CREATE TABLE Directors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
"""
create_movie_director_table_query = """
CREATE TABLE MovieDirector (
    movie_id INT,
    director_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(id),
    FOREIGN KEY (director_id) REFERENCES Directors(id)
);
"""
create_genres_table_query = """
CREATE TABLE Genres (
    movie_id INT,
    genre VARCHAR(255),
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);
"""
create_countries_table_query = """
CREATE TABLE Countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
"""
create_movie_country_table_query = """
CREATE TABLE MovieCountry (
    movie_id INT,
    country_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(id),
    FOREIGN KEY (country_id) REFERENCES Countries(id)
);
"""
cursor.execute(create_movies_table_query)
cursor.execute(create_directors_table_query)
cursor.execute(create_movie_director_table_query)
cursor.execute(create_genres_table_query)
cursor.execute(create_countries_table_query)
cursor.execute(create_movie_country_table_query)

# 4. 데이터 삽입
for i, row in df.iterrows():
    # 필드에 'nan' 값이 있는지 확인
    movie_name = row['영화명'] if pd.notna(row['영화명']) else 'Unknown'
    movie_name_eng = row['영화명(영문)'] if pd.notna(row['영화명(영문)']) else 'Unknown'
    production_year = row['제작연도'] if pd.notna(row['제작연도']) else None
    movie_type = row['유형'] if pd.notna(row['유형']) else 'Unknown'
    production_status = row['제작상태'] if pd.notna(row['제작상태']) else 'Unknown'
    genres = row['장르']
    # 영화 삽입
    insert_movie_query = """
    INSERT INTO Movies (title, title_en, year, type, status)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_movie_query, (movie_name, movie_name_eng, production_year, 
                                        movie_type, production_status))
    movie_id = cursor.lastrowid
    # 감독이 누락되었는지 확인
    director = row['감독']
    if pd.isna(director):
        director = 'Unknown'
    # 감독 삽입 (이름이 같은 감독이 이미 있는지 확인)
    select_director_query = """
    SELECT id FROM Directors WHERE name = %s
    """
    cursor.execute(select_director_query, (director,))
    result = cursor.fetchone()
    if result:
        director_id = result[0]
    else:
        insert_director_query = """
        INSERT INTO Directors (name)
        VALUES (%s)
        """
        cursor.execute(insert_director_query, (director,))
        director_id = cursor.lastrowid
    # 영화-감독 관계 삽입
    insert_movie_director_query = """
    INSERT INTO MovieDirector (movie_id, director_id)
    VALUES (%s, %s)
    """
    cursor.execute(insert_movie_director_query, (movie_id, director_id))
    # 장르 삽입
    if pd.notna(genres):  # 장르 데이터가 있는 경우에만 실행
        genres_list = genres.split(',')  # 쉼표로 장르 분리하여 리스트로 저장
        for genre in genres_list:
            insert_genre_query = """
            INSERT INTO Genres (movie_id, genre)
            VALUES (%s, %s)
            """
            cursor.execute(insert_genre_query, (movie_id, genre.strip()))
    # 제작국가 삽입
    production_countries = row['제작국가']
    if pd.notna(production_countries):  # 제작국가 데이터가 있는 경우에만 실행
        countries_list = production_countries.split(',')  # 쉼표로 국가 분리하여 리스트로 저장
        for country in countries_list:
            country = country.strip()
            # 국가 삽입 (이름이 같은 국가가 이미 있는지 확인)
            select_country_query = """
            SELECT id FROM Countries WHERE name = %s
            """
            cursor.execute(select_country_query, (country,))
            result = cursor.fetchone()
            if result:
                country_id = result[0]
            else:
                insert_country_query = """
                INSERT INTO Countries (name)
                VALUES (%s)
                """
                cursor.execute(insert_country_query, (country,))
                country_id = cursor.lastrowid
            # 영화-국가 관계 삽입
            insert_movie_country_query = """
            INSERT INTO MovieCountry (movie_id, country_id)
            VALUES (%s, %s)
            """
            cursor.execute(insert_movie_country_query, (movie_id, country_id))

cnx.commit()
cursor.close()
cnx.close()


