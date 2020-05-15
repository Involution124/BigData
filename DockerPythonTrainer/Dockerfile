FROM tensorflow/tensorflow:latest-py3
LABEL maintianer="Tyler Cole"

ENV DEBIAN_FRONTEND noninteractive

ADD Keras-CoDeepNEAT /Keras-CoDeepNEAT
ADD run_mnist.py /run_mnist.py

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y graphviz libgraphviz-dev

RUN pip3 install kafka-python
RUN pip3 install keras
RUN pip3 install networkx
RUN pip3 install pydot
RUN pip3 install graphviz
RUN pip3 install pygraphviz
RUN pip3 install sklearn
RUN pip3 install matplotlib



ENTRYPOINT ["python3",  "/run_mnist.py"]
