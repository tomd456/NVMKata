# Indicates the alpine-based python Docker image will be used as the base image.
FROM python:3

ADD . /kata_app
WORKDIR /kata_app

RUN pip3 install -U pylint

CMD /kata_app/CIBuild.sh
