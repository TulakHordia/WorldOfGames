FROM python:3.9

WORKDIR /flask_app

ENV FLASK_APP=main_score.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY flask_app/ .

RUN pip install -r requirements.txt

EXPOSE 5000
EXPOSE 8777

CMD python main_score.py