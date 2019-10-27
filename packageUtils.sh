#!/bin/bash

pythonLint (){
	pylint $1
}

pythonUnitTest (){
	python3 $1

}

pythonPackage (){
	python3 $1
}
