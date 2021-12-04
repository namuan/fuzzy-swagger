# fuzzy-swagger

[![PyPI](https://img.shields.io/pypi/v/fuzzy-swagger?style=flat-square)](https://pypi.python.org/pypi/fuzzy-swagger/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fuzzy-swagger?style=flat-square)](https://pypi.python.org/pypi/fuzzy-swagger/)
[![PyPI - License](https://img.shields.io/pypi/l/fuzzy-swagger?style=flat-square)](https://pypi.python.org/pypi/fuzzy-swagger/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


---

**Documentation**: [https://namuan.github.io/fuzzy-swagger](https://namuan.github.io/fuzzy-swagger)

**Source Code**: [https://github.com/namuan/fuzzy-swagger](https://github.com/namuan/fuzzy-swagger)

**PyPI**: [https://pypi.org/project/fuzzy-swagger/](https://pypi.org/project/fuzzy-swagger/)

---

API fuzz testing generator using swagger document.

## Installation

```sh
pip install fuzzy-swagger
```

## Example Usage

```
$ fuzzy-swagger --swagger http://localhost:8080/api-docs --server http://localhost:8080
```

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.7+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```
