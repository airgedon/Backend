FROM ubuntu:20.04

RUN apt-get update && apt-get install -y tzdata && apt install -y python3.8 python3-pip

RUN apt install python3-dev libpq-dev nginx -y

RUN pip install django gunicorn psycopg2

ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV /env

ENV PATH /env/bin:$PATH

ADD . /home/ubuntu/actions-runner/_work/Backend/Backend

WORKDIR /home/ubuntu/actions-runner/_work/Backend/Backend

COPY . .


RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "devsearch.wsgi"]
