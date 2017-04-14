FROM python:3.6-slim

RUN apt-get update && apt-get install -yq --no-install-recommends \
  build-essential python3-dev libmysqlclient-dev

COPY requirements.txt /var/app/
WORKDIR /var/app/
RUN pip install -r requirements.txt

COPY . /var/app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
