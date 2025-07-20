pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Blaszczykowske/HelloJenkins.git'
            }
        }

        stage('Set up virtualenv') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Run Script') {
            steps {
                sh './venv/bin/python main.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pip install pytest'
                sh './venv/bin/pytest --junitxml=results.xml || true'
            }
        }
    }
}
