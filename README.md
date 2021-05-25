# evreka_bins

git pull https://github.com/asliii/evreka_bins.git
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r req.txt
sudo -u postgres psql
create database logdb;
create user loguser with password '123456';
grant all privileges on database logdb to loguser;

