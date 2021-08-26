FROM python:3.9.1-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  && apt-get install -y build-essential procps telnet curl unzip wget xvfb tar bzip2 libgtk-3-0 libdbus-glib-1-2 \
  && apt-get install -y python3-dev build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gcc postgresql \
  && apt-get install -y gettext 

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip3 install -r /requirements/local.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY server server
COPY setup.cfg  /server/setup.cfg
COPY .coveragerc  /server/.coveragerc
COPY pytest.ini /server/pytest.ini


WORKDIR /server

ENTRYPOINT ["/entrypoint"]