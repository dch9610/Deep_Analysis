from flask import Blueprint
from flask import render_template

# blueprint 객체생성
user_blue = Blueprint('user',__name__)

# user_main을 요청하면 호출되는 함수
@user_blue.route('/user_login')
def user_login():
    
    # 응답결과를 랜더링한다.
    user_html = render_template('user/user_login.html')
    return user_html

# 회원가입
@user_blue.route('/user_join')
def user_join():

    # 응답결과를 랜더링한다.
    join_html = render_template('user/user_join.html')
    return join_html

# 회원 정보 수정
@user_blue.route('/user_modify')
def user_modify():

    # 응답결과를 랜더링한다.
    modify_html = render_template('user/user_modify.html')
    return modify_html