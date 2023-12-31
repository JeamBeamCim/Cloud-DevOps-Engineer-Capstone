#!/usr/bin/env bash

dockerpath=gokhantrnd/capstone_project
TAG=capstoneproject

kubectl run $TAG --image=$dockerpath --generator=run-pod/v1

kubectl get pods

kubectl port-forward pod/$TAG 8001:80
