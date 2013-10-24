svcmgt
======

Manage global services

run setup.sh to install required packages

#Add new files to the project:
git add www

git commit -m "new project"<br>

git push -u origin master<br>




#How to setup git
sudo apt-get install -y git-core

git config --global user.name "Julian Garcia-Sotoca"

git config --global user.email "juliansotoca@gmail.com"

git init

git remote add origin git@github.com:juliansotoca/svcmgt.git


#create and copy ssh key:
ssh-keygen -t rsa

more /home/vagrant/.ssh/id_rsa.pub

#test connectivity

ssh -T git@github.com


#clone repo
$ git clone https://github.com/juliansotoca/svcmgt.git
