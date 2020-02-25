FROM ubuntu:18.04
LABEL maintianer="Arnav Bhutani"

ENV DEBIAN_FRONTEND noninteractive


ARG ADDITIONAL_PACKAGES="python3.6 python3-pip libopencv-dev wget"

RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y gnupg2 ca-certificates \
            git build-essential $ADDITIONAL_PACKAGES \
      && rm -rf /var/lib/apt/lists/*

COPY ./configure.sh /tmp/

ARG SOURCE_BRANCH="master"
ARG SOURCE_COMMIT="d51d89053afc4b7f50a30ace7b2fcf1b2ddd7598"
ENV SOURCE_BRANCH $SOURCE_BRANCH
ENV SOURCE_COMMIT $SOURCE_COMMIT

ARG CONFIG

RUN git clone https://github.com/AlexeyAB/darknet.git && cd darknet \
      && git checkout $SOURCE_BRANCH \
      && git reset --hard $SOURCE_COMMIT \
      && /tmp/configure.sh cpu-cv && make \
      && cp darknet /usr/local/bin \
      && cp -r cfg / \
      && cp -r data / \
      && cd .. && rm -rf darknet

RUN git clone https://github.com/Involution124/BigData.git && cd BigData/DockerPythonConsumer \
      && cp app.py / \
      && cd ../.. && rm -rf BigData

RUN pip3 install kafka-python
RUN wget https://pjreddie.com/media/files/yolov3.weights

COPY app.py /tmp/

CMD ["python3", "app.py"]
