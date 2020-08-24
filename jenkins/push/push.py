import os
import sys


print("********************")

print("** Pushing image ***")

print("********************")

IMAGE="maven-project"
b = 10
Pass = 'amit@28198'

print("** Logging in ***")
os.system('docker login -u amit2328 -p {}'.format(Pass))
print("*** Tagging image ***")
os.system('docker tag {}:{} amit2328/{}:{}'.format(IMAGE,b,IMAGE,b))
print("*** Pushing image ***")
os.system('docker push amit2328/{}:{}'.format(IMAGE,b))
