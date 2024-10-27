# prerequisites to run this Python script

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
## lint and format using ruff
Ruff is included as Python package with poetry in this project. <br> 
lint:
```
poetry run ruff check
```
format:
```
poetry run ruff format 
```
Use --diff option to show what would be formatted:
```
poetry run ruff format --diff
```

## run the Python script
```
poetry run python -m src.function_analysis
```

## Input
Inside /data, there are three CSV files for training functions, ideal functions and test values.

## Output
The script will generate four HTML files which can be opened and viewed in any web browser. Each HTML file represents one training function, the matcning ideal function including matching test values.
