FROM python:3.12

RUN apt-get update;

RUN apt-get -y install locales && \
    locale-gen ru_RU.UTF-8 && \
    echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen

ENV LANG='ru_RU.UTF-8' \
    LANGUAGE='ru_RU.UTF-8' \
    LC_ALL='ru_RU.UTF-8'

RUN ln -fs /usr/share/zoneinfo/Erope/Moscow /etc/localtime

WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "app.py"]