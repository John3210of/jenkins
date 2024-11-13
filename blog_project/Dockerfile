FROM python:3.11-alpine
RUN apk update && apk add --no-cache \
    mariadb-client \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    mariadb-dev \
    pkgconfig
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
