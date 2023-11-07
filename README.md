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