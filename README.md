# MyCITool

## Introduction
MyCITool is just an initial implementation of CI python code including steps to clone an application from git repository, build a Docker image and start containers.

## Requirements 

* Python3
* Docker

## Install dependancies
Clone the repo and run the following command:

`pip install -r requirements.txt`

## Usage

Run the `MyCITool.py` script and provide the required parameters.
Run `python3 mycitool.py -h` for more details. 

## Limitation

This version was designed to work with a single repository: https://github.com/guyyosan/python-cherry-container

## Improvements

* Include logging
* Improve exception handling
* Add more functionalities