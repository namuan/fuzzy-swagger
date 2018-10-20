# Fuzzy-Swagger

[![Maintainability](https://api.codeclimate.com/v1/badges/90e749fdf9cda775a2f4/maintainability)](https://codeclimate.com/github/namuan/fuzzy-swagger/maintainability)

[![CircleCI](https://circleci.com/gh/namuan/fuzzy-swagger.svg?style=svg)](https://circleci.com/gh/namuan/fuzzy-swagger)

API fuzz testing generator using swagger document.

## Motivation


## Installation

```shell
$ pip install fuzzy-swagger
```

## Example Usage

```
$ fuzzy-swagger --swagger http://localhost:8080/api-docs --server http://localhost:8080
```

## Running locally

```
$ python local_main.py --swagger http://localhost:8080/api-docs --server http://localhost:8080
```

## Verbose debugging

To turn on verbose output for debugging, set the `--verbose` argument.

## Publishing Updates to PyPi

For the maintainer, increment the version number in fuzzy_swagger.py and run the following:

```shell
docker build -f ./Dockerfile.buildenv -t namuan/fuzzy-swagger:build .
docker run --rm -it --entrypoint python namuan/fuzzy-swagger:build setup.py publish
```

Enter the username and password for pypi.org repo when prompted
