# For Hand-ons
## 1st Project Delpoyment on Kubernetes using Jenkins

![Flow Chart Architecture -1 drawio](https://user-images.githubusercontent.com/121743268/215323459-dbb6a8a3-f317-413a-ad24-e19e4514b5c1.png)

I am succeed commit the codes to GitHub and using weebhook with Jenkins.

And I tried to add nodes by SSHagent to send files from Jenkins server to those nodes.
But it is not complete because after building config, Jenkins show error "Permission denied (publickey)".

**Jenkins Scipt below:**
```
node {
    stage('Git checkout'){
        git 'https://github.com/snowpaper/JumpBox_HomeTest.git'
    }
    stage('sending docker file to Ansible server over ssh'){
        sshagent(['ansible-demo']) {
            sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.31.193'
            sh 'scp /var/lib/jenkins/workspace/Pipeline-Demo/* ubuntu@172.31.31.193:/home/ubuntu'
        }
    }
    stage('sending docker file to WebApp server over ssh'){
        sshagent(['webapp-demo']) {
            sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.22.64'
            sh 'scp /var/lib/jenkins/workspace/Pipeline-Demo/* ubuntu@172.31.22.64:/home/ubuntu'
        }
    }
}
```

## 2nd Project
### Deployment Web Application on Kubernetes



