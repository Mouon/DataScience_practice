import mysql.connector


def search_movies():
    # MySQL 데이터베이스에 연결
    cnx = mysql.connector.connect(user='root', 
                                  password='mhj881610!', 
                                  host='localhost', 
                                  database='movie_db')
    cursor = cnx.cursor()

    # 검색 조건 입력 받기
    title = input("영화 제목을 입력하세요 (또는 엔터를 눌러 건너뛰기): ")
    year = input("제작연도를 입력하세요 (또는 엔터를 눌러 건너뛰기): ")
    country = input("제작국가를 입력하세요 (또는 엔터를 눌러 건너뛰기): ")
    genre = input("장르를 입력하세요 (또는 엔터를 눌러 건너뛰기): ")
    director = input("감독을 입력하세요 (또는 엔터를 눌러 건너뛰기): ")

    # 영화 검색 쿼리 생성
    search_query = """
    SELECT m.title, m.year, c.name AS country, g.genre, d.name AS director
    FROM Movies AS m
    LEFT JOIN MovieCountry AS mc ON m.id = mc.movie_id
    LEFT JOIN Countries AS c ON mc.country_id = c.id
    LEFT JOIN Genres AS g ON m.id = g.movie_id
    LEFT JOIN MovieDirector AS md ON m.id = md.movie_id
    LEFT JOIN Directors AS d ON md.director_id = d.id
    WHERE 1=1
    """

    # 검색 조건에 따라 쿼리에 조건 추가
    if title:
        search_query += "AND m.title LIKE '%{}%' ".format(title)
    if year:
        search_query += "AND m.year = {} ".format(year)
    if country:
        search_query += "AND c.name LIKE '%{}%' ".format(country)
    if genre:
        search_query += "AND g.genre LIKE '%{}%' ".format(genre)
    if director:
        search_query += "AND d.name LIKE '%{}%' ".format(director)

    # 영화 검색 실행
    cursor.execute(search_query)
    movies = cursor.fetchall()

    # 검색 결과 출력
    if movies:
        print("검색 결과:")
        for movie in movies:
            print("제목:", movie[0])
            print("제작연도:", movie[1])
            print("제작국가:", movie[2])
            print("장르:", movie[3])
            print("감독:", movie[4])
            print("---------------")
    else:
        print("검색 결과가 없습니다.")

    cursor.close()
    cnx.close()


# 영화 검색 실행
search_movies()
