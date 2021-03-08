# 데이터베이스 접속 테스트 내가 만든 폴더와 파일명
from database import connector
from database import user_dao
from database import board_dao
from database import content_dao

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

# 게시판 정보를 수정하는 테스트
# board_dao.updateBoardData('변경된 게시판',8)

# 게시판 삭제 (DELETE)
# board_dao.deleteBoardData(4)

# 모든 게시판 이름 정보 출력 (READ)
# result_all = board_dao.selectBoardAll()
# print(result_all)

# -------------------------------------------
# 게시글 정보를 저장하는 테스트 (CREATE)
# 외래키의 값은 참조하는 테이블의 값과 동일하게 해야함
# content_dao.insertContentData('테스트제목',2,'테스트내용','aaa.jpg',1)

# 게시글 모든 정보 불러오기 (READ)
# content_result_all = content_dao.selectContentDataAll()
# print(content_result_all)

# 하나의 게시판 이름 정보 출력 (READ)
# content_result_one = content_dao.selectContentDataOne(3)
# print(content_result_one)

# 게시글을 수정하는 함수 (UPDATE)
# content_dao.updateContentData('수정된제목',2,'수정된내용','bbb.jpg',1,3)

# 게시글을 삭제하는 함수 (DELETE)
content_dao.deleteContentData(3)


# 게시글 모든 정보 불러오기 (READ)
content_result_all = content_dao.selectContentDataAll()
print(content_result_all)