# Start minikube
    minikube start

# install strimzi operator
    helm repo add strimzi http://strimzi.io/charts/ 
    helm install my-kafka-operator strimzi/strimzi-kafka-operator 


# cluster definition 
    kubectl apply -f https://farberg.de/talks/big-data/03-Kafka-Operator-Helm/kafka-cluster-def.yaml 

# watch the cluster
    watch kubecl get all '

# start skaffold if everything is up and running 
    skaffold dev 

# Optional 

run the run.sh file it does everything for you


