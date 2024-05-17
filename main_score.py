from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(utils.SCORES_FILE_NAME, 'r') as file:
            score = file.read()
    except FileNotFoundError:
        error = utils.BAD_RETURN_CODE
        return render_template('error.html', ERROR=error)

    return render_template('score.html', SCORE=score)


if __name__ == '__main__':
    app.run(debug=True)
