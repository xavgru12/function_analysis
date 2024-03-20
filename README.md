# Perequisites to run this Python script

## install and setup Postgresql

install:
```
sudo apt install postgresql
```
enter postgresql:
```
sudo -u postgres psql template1
```
enter new password:
```
ALTER USER postgres with encrypted password 'postgres';
```

## install required Python packages using Poetry <br>

Poetry ensures all the Python packages are set to a specific version. Therefore the behaviour of the Python script is deterministic and equal to everyone who may run it. <br> 
install Poetry:
```
pip install poetry
```
setup poetry in your project root:
```
poetry init
```
let Poetry handle everything with: <br> 
```
poetry install
```
