import os

print("****************************************")
print("*****Testing code**********")
print("****************************************")

var = 'mvn test'

os.system('docker run --rm  -v  C:/Users/dell/Desktop/jenkins/pipeline/java-app:/app -v /root/.m2/:/root/.m2/ -w /app maven:3-alpine {}'.format(var))
