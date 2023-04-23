# Readme
## Project title
Python Common Lib
## Introduction - the project's aim
Aim of the project is to prepare set of common libraries for python projects
## Technologies
Project is created with:
* Python3.10
* Pytest
* Tox

## Hardware
Following hardware setup is used for the project:
* n/a

## Prerequisities
To run this project following prerequisites have to be fulfilled:
* Python3 has to be installed (3.9.2 - current default RaspbianOS version, 3.10.x, 3.11.x)
* Tox has to be installed
* Pytest has to be installed

## Install (Instalation from source code)
To run this project, make following instructions:
* Create folder for code in user folder
```
$ mkdir Git && cd $_
```
* Download git repository 
```
$ git clone https://github.com/0p553cd3v/PyCommon
```
* Go to repo dir
```
$ cd PyCommon
```
* (Optional) Run tests and code checkers
```
$ python3 tools/run.py
```
* If want to install from repo then:
- Build package
```
$ python3 build/build.py
```
- Install package 
```
$ python3 tools/install.py
```
* Import necessary functions using
```
>> import py_common
```
or 
```
>> from py_common.module import module_file_name
```

## Install (Instalation from PyPI)
TODO

## Notes
It is worth to install pyenv for handling of multiple python interpreters for tox. Link to instruction:
https://codeburst.io/how-to-install-and-manage-multiple-python-versions-in-wsl2-1131c4e50a58



