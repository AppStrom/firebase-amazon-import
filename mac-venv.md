## Python3 Virtualenv Setup and Preparing requirements.txt

##### Requirements

- Python 3
- Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

##### Installation

To install virtualenv via pip run:

```bash
$ pip3 install virtualenv
```

##### Usage

Creation of virtualenv:

```bash
$ virtualenv -p python3 <desired-path>
```

Activate the virtualenv:

```bash
$ source <desired-path>/bin/activate
```

Deactivate the virtualenv:

```bash
$ deactivate
```

[About Virtualenv](https://virtualenv.pypa.io/en/stable/)
{"mode":"full","isActive":false}

Prepare requirements.txt:

```bash
$ pip3 freeze > requirements.txt
```

Upgrade pip3:

```bash
pip3 install --upgrade pip
```
