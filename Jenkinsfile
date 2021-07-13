pipeline {
    agent any

    options {
        timeout(time: 1, unit: 'HOURS')   // timeout on whole pipeline job
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
    }
}
