FROM python:3.10.14-slim

RUN mkdir /opt/redeyes

COPY . /opt/redeyes
WORKDIR /opt/redeyes

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

CMD ["python", "-m", "gunicorn", "redeyes.wsgi", "-b", "0.0.0.0:8000"]
