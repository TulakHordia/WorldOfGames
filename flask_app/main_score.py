from flask import Flask, render_template
import utils
import os

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        if not os.path.exists(utils.SCORES_FILE_NAME):
            print(f"File not found: {utils.SCORES_FILE_NAME}")
            error = utils.BAD_RETURN_CODE
            return render_template('error.html', ERROR=error)

        with open(utils.SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
            return render_template('score.html', SCORE=score)
    except FileNotFoundError:
        error = utils.BAD_RETURN_CODE
        return render_template('error.html', ERROR=error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        error = utils.BAD_RETURN_CODE
        return render_template('error.html', ERROR=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

