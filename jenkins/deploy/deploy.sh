#!/bin/bash


echo maven-project > /tmp/.auth
echo $BUILD_TAG >> /tmp/.auth
echo $PASS >> /tmp/.auth

scp -i /opt/prod /tmp/.auth  prod@13.232.219.144:/tmp/.auth
scp -i /opt/prod ./jenkins/deploy/publish  prod@13.232.219.144:/tmp/publish
ssh -i /opt/prod  prod@13.232.219.144 "/tmp/publish"
