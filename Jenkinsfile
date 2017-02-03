pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 setup.py install --user --prefix='
            }
        }
        stage('Deploy') {
            steps {
                sh 'forever start -c python3 run.py'
            }
        }
    }
}
