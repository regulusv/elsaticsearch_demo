FROM python:alpine3.6
ADD . /code
WORKDIR /code
EXPOSE 8000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod 644 app.py
CMD python app.py
