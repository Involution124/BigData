FROM tensorflow/tensorflow:latest-py3
LABEL maintianer="Tyler Cole"

ENV DEBIAN_FRONTEND noninteractive

ADD Keras-CoDeepNEAT /Keras-CoDeepNEAT

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y graphviz libgraphviz-dev

RUN pip3 install kafka-python
RUN pip3 install keras
RUN pip3 install networkx
RUN pip3 install pydot
RUN pip3 install graphviz
RUN pip3 install pygraphviz
RUN pip3 install sklearn
RUN pip3 install matplotlib


#RUN git clone https://github.com/sbcblab/Keras-CoDeepNEAT.git;

CMD ["python3", "-v"]
CMD ["python3",  "/Keras-CoDeepNEAT/example_scripts/run_cifar10.py"]
