from flask import Blueprint
from flask import render_template

# 게시판 리스트 blueprint 객체생성
board_blue = Blueprint('board',__name__)

# board_main을 요청하면 호출되는 함수
@board_blue.route('/board_main')
def board_main():
    
    # html 데이터를 랜더링한다.
    board_html = render_template('board/board_main.html')
    return board_html


# board_read를 요청하면 호출되는 함수
@board_blue.route('/board_read')
def board_read():

    # html 데이터를 랜더링한다.
    board_read_html = render_template('board/board_read.html')
    return board_read_html

# 글수정 페이지
@board_blue.route('/board_modify')
def board_modify():

    # html 데이터를 랜더링한다.
    board_modify_html = render_template('board/board_modify.html')
    return board_modify_html

# 글작성 페이지
@board_blue.route('/board_write')
def board_write():

    # html 데이터를 랜더링한다.
    board_write_html = render_template('board/board_write.html')
    return board_write_html