FROM python:3.6.8-alpine

COPY requirements.txt /requirements.txt
COPY . /

RUN apk add --no-cache  \
    python3-dev \
    libstdc++ \
    libpq \
    g++ \
    postgresql-dev
    

RUN pip install -r /requirements.txt

EXPOSE 5000
CMD python /api.py