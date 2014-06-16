REST-Web-Service
================

This project provides RESTful web services. Currently I only provide a web service for generating fibonacci series.
The input should be a positive number and upper boundary on the input is 10000.

Steps to setup the system on Ubuntu server
-------------------------------------------
Create a basic Ubuntu 12.04 cloud server with 2 GB RAM.

Login to the server and run the following commands:

apt-get update

apt-get install git

apt-get install python-pip

pip install pecan

pip install nose

pip install mock

git clone https://github.com/aratim/REST-Web-Service.git


Steps to build the web service 
------------------------------
cd REST-Web-Service/

python setup.py develop


Start the web service
----------------------
pecan serve config.py


Access the web service
-----------------------
On a terminal:
    curl http://<Server IP>:9000/fibonacci?num=<number>

On a web browser:
    http://<Server IP>:9000/fibonacci?num=<number>
    

Example:
    From a terminal on the cloud server:
        curl http://localhost:9000/fibonacci?num=5 generates the output as follows:
        
            {"status": 200, "body": {"Fibonacci Series": [0, 1, 1, 2, 3]}}    
 

Run the unit tests
-------------------
./run_tests.sh
