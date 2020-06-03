#!/bin/bashf

minikube start
helm repo add strimzi http://strimzi.io/charts/ 
helm install my-kafka-operator strimzi/strimzi-kafka-operator
kubectl apply -f https://farberg.de/talks/big-data/03-Kafka-Operator-Helm/kafka-cluster-def.yaml
skaffold dev
