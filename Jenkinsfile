pipeline {
     
     agent any

     environment {
        PASS = credentials('registry-password')
        TAG = 10
    }
 

     stages {
         stage('Build')
         {

             steps {
                   sh '''
                       bash ./jenkins/build/mvn.sh mvn -B -DskipTests clean package 
                       bash ./jenkins/build/build.sh
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

                 sh 'bash ./jenkins/test/mvn.sh mvn test'

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

                 sh 'bash ./jenkins/push/push.sh'

             }


             }


         stage('Deploy')
         {
             steps {

                 echo 'bash ./jenkins/deploy/deploy.sh'
             }
         }

        
         }
     }
