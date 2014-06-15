REST-Web-Service
================

Setup (Ubuntu)
---------------
apt-get update
apt-get install git
apt-get install python-pip
pip install pecan
pip install nose
git clone https://github.com/aratim/REST-Web-Service.git


Build the web service 
----------------------
cd REST-Web-Service/
python setup.py develop


Start the web service
----------------------
pecan serve config.py


Access the web service
-----------------------
On a terminal:
    curl http://<Server IP>:9000/fibo/<number>

On a web browser:
    http://<Server IP>:9000/fibo/<number>


Run the unit tests
-------------------
./run_tests.sh
