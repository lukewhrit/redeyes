FROM python:3.10.14-alpine3.19

RUN mkdir /opt/redeyes

COPY . /opt/redeyes
WORKDIR /opt/redeyes

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "redeyes.wsgi", "-b", "0.0.0.0:8000"]
