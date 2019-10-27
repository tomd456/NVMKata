#!/bin/bash

# Source Function Code for executing each stage of CI.
source packageUtils.sh

#Begin by basic sanity test against Python Code, will fail if any code mistakes.
echo "INFO: Executing Inital Lint Tests against App"
pythonLint kata_app/__init__.py

#Return Status from Pylint, for Logic, proceed, only if succesful, to Unit Testing.
compileLintStatus=$?
if [ $compileLintStatus -ne 0 ]; then
     echo "ERROR: Inital Lint Results Have failed, will not proceed to Execute Unit Tests"
     exit 1
else 
     echo "INFO: Inital Lint Results Have Succeeded, will now proceed to Execute Unit Tests"
     pythonUnitTest unittests.py
fi 

#Return Status from Unit Testing, proceed to packaging App, only if status is succesfull.
unitTestStatus=$?
if [ $unitTestStatus -ne 0 ]; then
     echo "ERROR: Unit Tests Have failed, will not proceed to Package App"
     exit 1
else 
     echo "INFO: Unit Tests Have Suceeded, will proceed to Package App"
     pythonPackage "setup.py sdist bdist_wheel" 
fi 

echo "INFO: CI Build has completed, Artifacts have been succesfully, Built, Tested & Packaged."

