
pipeline {
    agent any

    stages { 
        stage('build') {
            steps {
                sh 'git clone https://github.com/Maneleki/Selenium_projekt.git'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest tests/test.py'
            }
        }
    }
}
