FROM python:3
RUN apt update -y
COPY app.py .
CMD python app.py