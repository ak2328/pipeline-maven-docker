#!/bin/bash

echo "***************************"
echo "** Building jar ***********"
echo "***************************"

WORKSPACE=/home/jenkins_home/workspace/pipeline-docker-maven

docker run --rm  -v  /home/jenkins_home/workspace/Pipeline-maven-docker/java-app:/app -v /root/.m2/:/root/.m2/ -w /app maven:3-alpine "$@"
