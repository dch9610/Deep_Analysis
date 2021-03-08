from types import resolve_bases
from flask import Blueprint
from flask import render_template
from flask import request # 정보추출 라이브러리

# db저장 라이브러리 호출
from database import user_dao

# blueprint 객체생성
user_blue = Blueprint('user',__name__)

# ----------------------------------------
# user_main을 요청하면 호출되는 함수
@user_blue.route('/user_login', methods=['get'])
def user_login():
    # 파라미터 데이터를 추출한다.
    login_fail = request.args.get('login_fail')

    # 응답결과를 랜더링한다.
    user_html = render_template('user/user_login.html', login_fail = login_fail)
    return user_html

# ----------------------------------------
# 회원가입
@user_blue.route('/user_join')
def user_join():

    # 응답결과를 랜더링한다.
    join_html = render_template('user/user_join.html')
    return join_html

# ----------------------------------------
# 회원 정보 수정
@user_blue.route('/user_modify')
def user_modify():

    # 응답결과를 랜더링한다.
    modify_html = render_template('user/user_modify.html')
    return modify_html

# ----------------------------------------
# 회원가입처리
@user_blue.route('/user_join_pro', methods=['post'])
def user_join_pro():
    # 브라우저가 전달한 데이터를 추출한다.
    # print(request.form)
    user_name = request.form.get('user_name')
    user_id   = request.form.get('user_id')
    user_pw   = request.form.get('user_pw')

    # print(user_name)
    # print(user_id)
    # print(user_pw)

    # 데이터 베이스에 저장한다.
    user_dao.insertUserData(user_name, user_id, user_pw)


    return '''
        <script>
            alert('가입이 완료되었습니다.')
            location.href = 'user_login'
        </script>
    '''

# ----------------------------------------
# 아이디 중복확인
@user_blue.route('/check_join_id')
def check_join_id():
    # 브라우저가 보낸 아이디를 추출한다.
    new_id = request.args.get('new_id')

    # 중복확인
    result = user_dao.checkInputUserId(new_id)

    return f'{result}'

# ----------------------------------------
# 로그인 처리
@user_blue.route('/user_login_pro', methods=['post'])
def user_login_pro():
    # 브라우저가 전달한 데이터를 추출한다.
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    # print(user_id)
    # print(user_pw)

    # 사용자 존재여부를 확인
    result = user_dao.check_login_user(user_id, user_pw)
    # print(result)

    # 로그인 실패
    if result == None:
        return '''
            <script>
                alert('로그인에 실패하였습니다.')
                location.href = 'user_login?login_fail=true'
            </script>
        '''
    # 로그인 성공   
    else:
        return '''
            <script>
                alert('로그인에 성공하였습니다.')
                location.href = 'main'
            </script>
        '''