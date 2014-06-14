#!/bin/bash

echo -e "\nRunning tests for Fibonacci Controller"
nosetests restwebservice.tests.api.controllers.v1.test_fibonacci


echo -e "\nRunning tests for Fibonacci Handler"
nosetests restwebservice.tests.api.handlers.test_fibonacci_handler
