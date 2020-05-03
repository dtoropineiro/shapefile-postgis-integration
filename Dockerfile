ARG IMAGE_VERSION=python
ARG IMAGE_TAG=3.7
FROM $IMAGE_VERSION:$IMAGE_TAG

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        libgdal.dev \
        postgis \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]