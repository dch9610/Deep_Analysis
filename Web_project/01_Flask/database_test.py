# 데이터베이스 접속 테스트 내가 만든 폴더와 파일명
from database import connector
from database import user_dao
from database import board_dao

conn = connector.get_connection()
print(conn)
# conn.close()

# 사용자 정보 저장 테스트 (CREATE)
# user_dao.insertUserData('홍길동','abcd','1234')
# user_dao.insertUserData('김길동','aaaa','1234')
# user_dao.insertUserData('최길동','bbbb','1234')
# print('저장완료')

# 모든 사용자 정보 읽기 테스트 (READ)
# result = user_dao.selectUserDataAll()
# print(result)

# 한명의 사용자 정보 읽기 테스트 (READ)
# result_one = user_dao.selectUserDataOne(1)
# print(result_one)

# 한명의 회원 정보 수정 (UPDATE)
# user_dao.updataUserData(1,9999)

# 사용자 한명의 정보를 삭제하는 테스트 (DELETE)
# user_dao.deleteUserData(1)

# 한명의 사용자 정보 읽기 테스트 (READ)
# result_one = user_dao.selectUserDataOne(1)
# print(result_one)


# -------------------------------------------
# 게시판 이름 정보 저장 (CREATE)
# board_dao.insertBoardData('자유게시판')
# board_dao.insertBoardData('유머게시판')
# board_dao.insertBoardData('정치게시판')
# board_dao.insertBoardData('스포츠게시판')
# print('저장완료')

# 모든 게시판 이름 정보 출력 (READ)
# result_all = board_dao.selectBoardAll()
# print(result_all)

# 하나의 게시판 이름 정보 출력 (READ)
# result_one = board_dao.selectBoardOne(2)
# print(result_one)

