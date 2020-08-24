pipeline {
     
     agent any

     environment {
        PASS = credentials('registry-password') 
        IMAGE = maven-project
        TAG = 10
    }
 

     stages {
         stage('Build')
         {

             steps {
                   sh '''
                       ./jenkins/build/mvn.sh mvn -B -DskipTests clean package 
                       ./jenkins/build/build.sh
                       '''
                       
                       // cd .\jenkins\build\ | docker-compose -f docker-compose-build.yml build --no-cache
                       
                 
                              }

                              post {
                success {
                   archiveArtifacts artifacts: 'java-app/target/*.jar', fingerprint: true
                }
            }
         }

         stage('Test')
         {

             steps {

                 sh './jenkins/test/mvn.sh mvn test'

             }

            post {
                always {
                    junit 'java-app/target/surefire-reports/*.xml'
                }
            }


             }

         stage('Push')
         {

             steps {

                 sh './jenkins/push/push.sh'

             }


             }


         stage('Deploy')
         {
             steps {

                 echo './jenkins/deploy/deploy.sh'
             }
         }

        
         }
     }
