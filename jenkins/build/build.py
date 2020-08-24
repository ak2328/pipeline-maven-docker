import os

#Copy new jar to the build location

os.system('copy -f C:/Users/dell/Desktop/jenkins/pipeline/java-app/target/*.jar /jenkins/build')

print("****************************************")
print("*****Building image**********")
print("****************************************")

os.system('cd C:/Users/dell/Desktop/jenkins/pipeline/jenkins/build/ | docker-compose -f docker-compose-build.yml build --no-cache')