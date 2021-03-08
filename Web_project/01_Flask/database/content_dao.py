from pymysql import cursors
from database import connector

# create table content_table(
#     content_idx int auto_increment,
#     content_subject varchar(500) not null,
#     content_date date not null,
#     content_writer_idx int not null,
#     content_text varchar(500) not null,
#     content_file varchar(500),
#     content_board_idx int not null,
#     constraint content_pk primary key(content_idx),
#     constraint content_fk1 foreign key(content_writer_idx)
#     references user_table(user_idx),
#     constraint content_fk2 foreign key(content_board_idx)
#     references board_table(board_idx)
# );

# 게시글 정보 저장 (Create)
def insertContentData(content_subject, content_writer_idx,
                        content_text, content_file, content_board_idx):
    # 쿼리문 작성   
    sql = '''
        insert into content_table
        (content_subject, content_date, content_writer_idx,
        content_text, content_file, content_board_idx)
        values
        (%s, sysdate(), %s, %s, %s, %s)
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 저장될 값 설정
    data = (content_subject, content_writer_idx,
            content_text, content_file, content_board_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터베이스 접속종료
    conn.close()
# --------------------------------------------------------

# 모든 글 정보를 가져오는 함수 (READ)
def selectContentDataAll():
    # 쿼리문 작성
    sql = '''
        select * from content_table
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정


    # 쿼리문 실행
    cursor.execute(sql)
    result = cursor.fetchall()

    # 데이터베이스 접속종료
    conn.close()

    return result

# -------------------------------------------
# 모든 글 정보를 가져오는 함수 (READ)
def selectContentDataOne(content_idx):
    # 쿼리문 작성
    sql = '''
        select * from content_table
        where content_idx = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정
    data = (content_idx)

    # 쿼리문 실행
    cursor.execute(sql,data)
    result = cursor.fetchone()

    # 데이터베이스 접속종료
    conn.close()

    return result
# -------------------------------------------

# 게시글 정보를 수정하는 함수
# 처음에는 들어가는 값을 다 지정해준후 수정되지 않는 값은 삭제해나가면서 진행
def updateContentData(content_subject, content_writer_idx, content_text, 
                        content_file, content_board_idx, content_idx):
    # 쿼리문 작성
    sql = '''
        update content_table
        set content_subject = %s, content_writer_idx = %s,
            content_text = %s, content_file = %s,
            content_board_idx = %s
        where content_idx = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정
    data = (content_subject, content_writer_idx, content_text, 
            content_file, content_board_idx, content_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터베이스 접속 종료
    conn.close()

# 게시글 하나를 삭제하는 함수
def deleteContentData(content_idx):
    # 쿼리문 작성
    sql = '''
        delete from content_table
        where content_idx = %s
    '''

    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()

    # %s에 지정될 값 설정
    data = (content_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()

    # 데이터베이스 접속종료
    conn.close()