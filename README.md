# kata_app Python Package

This is an example python Package, provided to demonstrate both the singular _Build, Test, Package_ CI Processes, and a combined staged based pipeline. 

Please see instructions below for executing the singular stages **Locally**, on your System, in addition to processing the full pipeline process through a **Docker** Image.

## Execute Steps Locally

### Pre-Requsites:

*  'pylint' - This code-checker must first be installed on your local system before proceeding, in order for the first stage to complete. - See instructions:
   
    * https://www.pylint.org/#install

### Run Lint Testing against the Python Code (Step 1 / Build)

1. Within the root package directory execute the below command against the main constructor method python script.

    * 'pylint kata_app\__init__.py'

2. A report will be returned, detailing any possible issues discovered from the lint test, with a final result rating of the code within the script.

### Run Unit Testing against the Python Code (Step 2 / Unit Testing)

1. Proceed to complete the Unit Tests provided within the package, using the command below:

    * 'python3 unittests.py'

2. Each arithmatic module endpoint within the main construct will be tested to ensure the expected value is returned, using the unit tests within the python script.
If an unexpected value is returned, i.e. their is an issue within the script, the Unit Tests will return a failure, allowing for diagnosis of the method in question.

### Package the Python artifacts. (Step 3 / Package Artifacts)

1. After testing is completed, package the artfiacts, using standard Python methodologies (see: setup.py), by executing the command below, still in the root project directory.

    * 'python3 setup.py sdist bdist_wheel'

2. This will now package the main artifacts/ scripts, within the kata_app directory, based on details stored within setup.py. A tar.gz archive will be provided within sub-dir /dist, 'kata_app-0.0.1.tar.gz'.

### Cleanup (Optional)

1. In order to remove any cache build/ post package artifacts, run the below Python script, from the base Package directory:

    * 'python3 cleanup.py'

2. The script will now proceed to remove all cache files used for Linting, in addition to any packages generated.    


## Run Full CI Pipeline Using Docker

### Pre-Requsites:

*  Docker is already installed, and setup locally on your Machine.

### Build Docker image, from Dockerfile

1. From main project directory, execute below command:

    * docker build . -t kata_app:latest

2. Docker will proceed to pull the base image, if it does'nt already exist, add required pre-req's, and generate the Docker image, to your system.

### Run Docker Container, executing CIBuild Script.

1. Run the below command, to startup the Docker container, and execute the CIBuild script.

    * docker run --rm -it kata_app:latest

2. Monitor output from the command, to check how the CI Process completes. 
    * Each stage is dependent on the previous succeeding; i.e. for the Unit Tests to succeed, the Lint Tests must pass, and the same for the packaging of the Python Artifacts, the Unit Tests must pass. 
    * Following the completing of the Pipeline script, the container will exit, as it's no longer required. 
    * If any fixes are to be completed, the Docker image can be rebuilt, and the container re-executed to re-attempt the CI process.