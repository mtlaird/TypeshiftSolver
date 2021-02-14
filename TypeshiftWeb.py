from bottle import route, run, post, request
from TypeshiftSolver import TypeshiftBoard


def new_puzzle_link():
    return "Solve a <a href=/puzzle>new puzzle</a>.<br>\n"


@route('/')
def index():
    return new_puzzle_link()


@route('/puzzle')
def new_puzzle():
    ret_html = 'Enter new puzzle here: <br>\n<form action="/solve" method="post" autocomplete="off">\n'

    base_input = '<input type="text" name="{name}" minlength="0" maxlength="1" size="1">'
    for row in range(8):
        for col in range(8):
            element_name = "row{row}col{col}".format(row=row, col=col)
            ret_html += base_input.format(name=element_name)
        ret_html += "<br>\n"

    ret_html += "<input type=submit></form>\n(This may take a minute...)"

    return ret_html


@post('/solve')
def solve_puzzle():
    board = TypeshiftBoard()

    for col in range(8):
        coltext = ""
        for row in range(8):
            element_name = "row{row}col{col}".format(row=row, col=col)
            element_value = request.forms.get(element_name)
            if element_value != "" and element_value is not None:
                coltext += element_value
        if coltext != "":
            board.add_column(coltext)

    board.solve()

    return "Board: <br>\n" + board.board_html() + "Valid words: <br>\n" + board.valid_words_html() + \
           "<br>\n" + new_puzzle_link()


run(host="localhost", port=5234)
