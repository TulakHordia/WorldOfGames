from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route('/')
def score_server():
    SCORE = utils.SCORES_FILE_NAME
    ERROR = utils.BAD_RETURN_CODE
    render_template('error.html', ERROR=ERROR)
    render_template('score.html', SCORE=SCORE)


if __name__ == '__main__':
    app.run(debug=True)
