import os

print("****************************************")
print("*****Building jar**********")
print("****************************************")

var = 'mvn -B -DskipTests clean package'
WORKSPACE='C:/Users/dell/Desktop/jenkins/jenkins_home/workspace/pipeline-docker-maven'

os.system('docker run --rm  -v  {}/java-app:/app -v /root/.m2/:/root/.m2/ -w /app maven:3-alpine {}'.format(WORKSPACE,var))
