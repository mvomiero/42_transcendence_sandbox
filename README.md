## Virtual environments in python
* create a venv called "venv"
```bash
python3 -m venv --without-pip venv
```
* activate the venv
```bash
source venv/bin/activate
```
* get pip in the venv
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```


### add the django location to PATH
```bash
export PATH="/home/mvomiero/.local/bin:$PATH"
```
* to check if django is installed
```bash
python3 -m django --version
```

* to start a new project
```bash
django-admin startproject mysite
```

* to run the project:
* first change in the website folder, then run the servers
```bash
python3 manage.py runserver
```
* to start the polls app
```bash
python3 manage.py startapp polls
```
