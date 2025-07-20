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
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\pip install --upgrade pip'
                bat '.\\venv\\Scripts\\pip install -r requirements.txt || exit /b 0'
            }
        }

        stage('Run Script') {
            steps {
                bat '.\\venv\\Scripts\\python main.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\pip install pytest'
                bat '.\\venv\\Scripts\\pytest --junitxml=results.xml || exit /b 0'
            }
        }
    }
}
