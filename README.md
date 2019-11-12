# Meteoroid Client

## Overview
Meteoroid Client is a command-line client for Meteoroid that  
integrating Function as a Service(FaaS) capabilities in FIWARE.

## Requirements
Python 3.8+
cliff  2.16.0+
pbr    5.4.3+


## Usage

### Start virtualenv and Install 

```
virtualenv -p python3.8 xxxx
source xxx/bin/active
pip install .
```
### Example of use　
```
$ meteoroid result show 22
+---------------+------------------+
| Field         | Value            |
+---------------+------------------+
| id            | 22               |
| response      | test_response    |
| logs          | test_logs        |
| FiwareService | None             |
| functionId    | test_function_id |
+---------------+------------------+
```
