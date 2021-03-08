# 게시판 정보 CRUD
from pymysql import cursors
from database import connector

# 게시판 이름 정보 저장 (CREATE)
def insertBoardData(board_name):
    # 쿼리문 작성
    sql='''
        insert into board_table
        (board_name)
        values (%s)
    '''
    
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값 지정
    data=(board_name)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    
    # 데이터베이스 접속종료
    conn.close()
# -------------------------------------------


# 모든 게시판 이름 정보 반환하는 함수 (READ)
def selectBoardAll():
    # 쿼리문 작성
    sql = '''
        select * from board_table 
        order by board_idx asc
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값 지정


    # 쿼리문 실행
    cursor.execute(sql)
    result = cursor.fetchall()

    # 데이터베이스 접속종료
    conn.close()

    return result
# -------------------------------------------


# 하나의 게시판 이름 데이터를 가져오는 함수
def selectBoardOne(board_idx):
    # 쿼리문 작성   
    sql = '''
        select * from board_table
        where board_idx = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입될 값 지정
    data = (board_idx)

    # 쿼리문 실행
    cursor.execute(sql,data)
    result = cursor.fetchone()

    # 데이터베이스 접속종료
    conn.close()

    return result
# -------------------------------------------

# 게시판 정보를 수정하는 함수
def updateBoardData(board_name, board_idx):
    # 쿼리문 작성
    sql = '''
        update board_table
        set board_name = %s
        where board_idx = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정
    data = (board_name, board_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터베이스 접속해제
    conn.close()
# -------------------------------------------

# 게시판 정보 삭제 (Delete)
def deleteBoardData(board_idx):
    # 쿼리문 작성
    sql='''
        delete from board_table
        where board_idx = %s
    '''

    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값 설정   
    data = (board_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터베이스 접속종료
    conn.close()
