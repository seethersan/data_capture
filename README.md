# DATACAPTURE

## DataCapture Class

DataCapture class has two attributes, the list of numbers and a dict for stats. It uses numpy for stats calculation and comes with tests written with unittest library.

Before using greater, less and between methods is needed to execute **build_stats**. If this functions are executed before **build_stats** it will raise a custom exception called UninitializedStats

This class only accepts numbers from 0 to 1000.

## Install the project

First create a virtualenv

```
virtualenv .env
source .env/bin/activate
```

## Install dependencies

```
pip install -r requirements.txt
```

## Run tests

```
python test_data_capture.py
```
