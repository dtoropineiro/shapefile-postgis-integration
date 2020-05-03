ARG IMAGE_VERSION=kartoza/postgis
ARG IMAGE_TAG=12.1
FROM $IMAGE_VERSION:$IMAGE_TAG

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libgdal.dev \
    postgis

EXPOSE 5432