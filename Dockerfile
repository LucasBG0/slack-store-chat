FROM python:3.10.6-alpine3.16@sha256:c37301b8439432638163231fd441845fce3511dde0ec6f2e7e131b5b91e6ffea

RUN apk --update add bash nano

COPY ./requirements.txt /app/requirements.txt

RUN addgroup -g 1100 python

RUN adduser -u 1100 -G python --disabled-password -s /bin/bash python

USER python

WORKDIR /app

#python binaries
ENV PATH="/home/python/.local/bin:${PATH}"

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["python3", "app.py"]
