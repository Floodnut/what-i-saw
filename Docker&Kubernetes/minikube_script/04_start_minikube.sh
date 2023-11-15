minikube start --driver=docker --kubernetes-version=1.23.3 --memory=8g —cpus=4 --profile mlops
minikube status
minikube dashboard -p mlops