minikube start --driver=docker --kubernetes-version=1.23.5 --memory=8g —cpus=4 --profile mlops
minikube status -p mlops
minikube dashboard -p mlops


# minikube start --driver=docker \
#   --kubernetes-version=v1.23.5  \
#   --extra-config=apiserver.service-account-signing-key-file=/var/lib/minikube/certs/sa.key \
#   --extra-config=apiserver.service-account-issuer=kubernetes.default.svc