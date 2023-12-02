#!/usr/bin/env bash
# use this to deploy the application to minikube
kubectl config use-context minikube
kubectl apply -f k8s/manifets.yaml
