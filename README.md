# World of Games: The Epic Journey

Welcome to the World of Games: The Epic Journey! This Python program offers you an exciting collection of three games to enjoy. Embark on this epic journey filled with fun and challenges!

## Features

- **Memory Game:** Test your memory skills as you recall a sequence of numbers that appear for a brief moment.
  
- **Guess Game:** Put your guessing abilities to the test as you try to predict a number chosen by the computer.
  
- **Currency Roulette:** Take a gamble and try to guess the value of a random amount of USD in ILS (Israeli Shekels).

## Flask Integration

The project currently has Flask integration working. To run the application, execute `main_score.py` and visit [http://127.0.0.1:5050](http://127.0.0.1:5050) in your browser.

## Jenkins Pipeline

The project is integrated with Jenkins using a Jenkinsfile. The pipeline script automates the following tasks:

- Pulls the GitHub repository.
- Builds the Docker image and pushes it.
- Launches the Docker containers.
- Installs Selenium and Webdriver Manager.
- Executes tests using `tests/e2e.py` to ensure the score is between 1 and 1000.
- Fails the pipeline if the test conditions are not met.

The tests are performed on port 8777.
