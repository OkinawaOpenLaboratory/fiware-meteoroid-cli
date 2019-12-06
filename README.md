# Meteoroid CLI

## Overview
Meteoroid CLI is a command-line-interface for Meteoroid that
integrating Function as a Service(FaaS) capabilities in FIWARE.

## Requirements
Python 3.8+
cliff  2.16.0+
pbr    5.4.3+


## Usage

### Install meteoroid cli

```
pip install meteoroid-cli
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

## Commands

```
Commands:
  function create  Create a function
  function delete  Delete a function
  function list  Show function list
  function show  Show a function
  function update  Update a function

  endpoint create  Create endpoint
  endpoint delete  Delete endpoint
  endpoint list  Show endpoint list
  endpoint show  Show a endpoint

  subscription create  Create subscription
  subscription delete  Delete subscription
  subscription list  Show subscription list
  subscription show  Show a subscription

  result list    Show result list
  result show    Show a result
```

### How to use

[Meteoroid README](https://github.com/OkinawaOpenLaboratory/fiware-meteoroid/blob/master/README.md)
