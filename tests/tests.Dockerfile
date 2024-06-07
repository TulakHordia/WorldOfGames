# tests/tests.Dockerfile

FROM python:3.9

# Set up environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install Firefox
RUN apt-get update && \
    apt-get install -y \
    firefox-esr \
    --no-install-recommends

# Install Geckodriver
RUN apt-get install -y wget
RUN wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
    && rm /tmp/geckodriver.tar.gz

# Set up xvfb to run headless Firefox
RUN apt-get install -y xvfb

# Set the working directory
WORKDIR /tests

# Copy the test scripts into the container
COPY tests/ .

# Install the required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set the display port for xvfb
ENV DISPLAY=:99

# Use xvfb-run to start the script
CMD ["xvfb-run", "-s", "-screen 0 1920x1080x24", "python", "e2e.py"]
