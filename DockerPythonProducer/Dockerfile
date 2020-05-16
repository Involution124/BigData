FROM tensorflow/tensorflow:latest-py3
LABEL maintianer="Tyler Cole"

RUN pip3 install keras
RUN pip3 install kafka-python
ADD app.py /app.py
ENTRYPOINT ["python3", "app.py"]
