# 사용자 정보 CRUD 파일
from database import connector

# 사용자 정보 저장 (Create)
def insertUserData(user_name, user_id, user_pw):
    # 쿼리문
    sql ='''
            insert into user_table
            (user_name, user_id, user_pw)
            values (%s, %s, %s)
        '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # 아무 기호가 없을때는 튜플형식
    # %s 부분에 대입될 값을 튜플로 생성한다.
    # 쿼리문의 %s 순서에 맞춰준다.
    data = user_name, user_id, user_pw

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속을 끊어준다.
    conn.close()

# 모든 회원 정보를 반환하는 함수 (Read)
def selectUserDataAll():
    # 쿼리문
    sql = '''
        select * from user_table
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값 지정 (없음)

    # 쿼리 실행
    cursor.execute(sql)
    result = cursor.fetchall()

    # 데이터베이스 접속 해제
    conn.close()

    return result


# 회원 한명의 데이터를 가져오는 함수
def selectUserDataOne(user_idx):
    # 쿼리문 작성
    sql = '''
        select * from user_table
        where user_idx = %s

    '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입될 값 지정
    data = (user_idx)

    # 쿼리문 실행
    cursor.execute(sql,data) # 작성한 sql문에 %s 부분에 data가 들어감
    result = cursor.fetchone()

    # 데이터베이스 접속해제
    conn.close()

    return result

# 특정 회원의 데이터를 수정하는 함수
def updataUserData(user_idx, user_pw):
    # 쿼리문 작성
    sql = '''
        update user_table
        set user_pw = %s
        where user_idx = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값 설정
    data = (user_pw, user_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit() # 변경된 값 반영

    # 데이터베이스 접속종료
    conn.close()


# 회원 정보 삭제 (Delete)
def deleteUserData(user_idx):
    # 쿼리문 작성
    sql ='''
        delete from user_table
        where user_idx = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값 설정
    data = (user_idx)

    # 쿼리문 실행
    cursor.execute(sql,data)
    conn.commit()

    # 데이터베이스 접속 종료
    conn.close()