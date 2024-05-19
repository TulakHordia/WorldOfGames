from app import start_play, welcome
from main_score import app, score_server
from werkzeug.serving import run_simple
import threading
import time


def run_flask():
    run_simple('127.0.0.1', 5000, app, use_reloader=False, use_debugger=True)


if __name__ == '__main__':
    # Place flask into another thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    # Wait a sec to start the game
    time.sleep(1)
    # Run WoG 1-2
    welcome()
    start_play()


