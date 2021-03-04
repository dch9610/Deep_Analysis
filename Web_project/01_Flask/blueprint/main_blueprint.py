from flask import Blueprint
from flask import render_template

# blueprint 객체 생성
main_blue = Blueprint('main', __name__)

# main을 요청하면 호출되는 함수
@main_blue.route('/main')
def main():
    # html 데이터를 랜더링한다.
    html = render_template('main/main.html')
    return html