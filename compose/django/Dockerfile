FROM python:3.9.4-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
	g++ \
    vim

# fix warning
RUN pip install --upgrade pip==21.1.1

RUN mkdir /code

COPY ./requirements/ /tmp/

RUN pip --no-cache-dir install -r /tmp/local.txt
RUN apt-get clean

COPY ./compose/django/start.sh ./start.sh
RUN chmod +x ./start.sh

WORKDIR /code


# CMD tail -f /dev/null