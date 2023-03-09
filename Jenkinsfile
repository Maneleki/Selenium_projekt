/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('tests Python Env') {
            withPythonEnv('python3') {
                sh 'pip install pytest'
                sh 'pytest tests/test.py'
            }
    }
}
