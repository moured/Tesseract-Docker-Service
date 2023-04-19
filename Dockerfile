FROM python:3
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
RUN apt update && apt install tesseract-ocr -y && apt install tesseract-ocr-all -y
COPY . .
CMD python /app/app.py