
pipeline {
    agent any
    stages { 
        stage('Tools initiated') {
            steps {
                sh 'npm -v'
                sh 'git --version'
            }
        }
        stage('Check code') {
            steps {
                git branch: 'main', url: 'https://github.com/Maneleki/Selenium_projekt.git'
            }
        }
        stage('build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest tests/test_sydsvenskan.py'
            }
        }
    }
}
