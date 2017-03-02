FROM exiasr/alpine-flask:pytest
MAINTAINER Michael Lin <michaellin@ualberta.ca>

ADD . /home/app

ENV APP_DIR /home/app

WORKDIR /home/app

