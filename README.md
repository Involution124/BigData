# BigData
Distributed Big Data computing platform, parallelized machine learning. 

# Installation
1) Setup the model training deployment

```kubectl create -f trainer ```

Wait for it to finish, if you proceed early the rest of the system will be idle until this is complete

2) Setup the Zookeeper and Kafka nodes

```kubectle create -f zookeeper.yaml; kubectl create -f kafka.yaml```

3) Initialize the ML processing nodes 

```kubectl create -f processor.yaml```

4) Initialize the ML preprocessing nodes

```kubectl create -f preprocessor.yaml```

