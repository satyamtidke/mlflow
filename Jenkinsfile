def workspace;
node
{
    stage('checkout')
    {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/satyamtidke/mlflow.git']]])
        workspace = pwd()
    }
    stage('code analysis')
    {
        echo "code analysis"
    }
    stage("Build")
    {
        echo "build"
    }
    stage('delivery')
    {
        echo "delivery!!"
    }
    stage('unit testing')
    {
        echo "testing"
    }
}
