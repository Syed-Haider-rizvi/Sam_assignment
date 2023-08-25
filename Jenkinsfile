pipeline {
        environment {
        registry= "akashtawade/sparkdemo1"
        registryCredential= 'akash1493'
    }
    agent any
    stages {
        stage('Checkout') {
        steps {
		
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'Lavanya-Prabhakar', url: 'https://github.com/Lavanya-Prabhakar/Spark_Assignment_Practice.git']]])
			
            }
        }
        stage('Build') {
               steps {
                    { 
						git credentialsId: 'Lavanya-Prabhakar', url: 'https://github.com/Lavanya-Prabhakar/Spark_Assignment_Practice.git'
						   script {
									RUN docker build .
								 }
                    }
				}
            }
         stage('Test') {
            steps {
                echo 'Job has been test'
            }
        }
        stage('QA Deploy') {
            steps {
                echo 'Job has been deployed'
            }
        }
         stage('Prod Deploy') {
            steps {
                echo 'Production Deployment done'
            }
        }
    }
}





