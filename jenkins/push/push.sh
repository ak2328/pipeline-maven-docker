#!/bin/bash

echo "********************"
echo "** Pushing image ***"
echo "********************"

IMAGE="maven-project"

echo "** Logging in ***"
docker login -u amit2328 -p $PASS
echo "*** Tagging image ***"
docker tag $IMAGE:$BUILD_TAG amit2328/$IMAGE:$BUILD_TAG
echo "*** Pushing image ***"
docker push amit2328/$IMAGE:$BUILD_TAG
