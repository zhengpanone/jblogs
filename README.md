```shell
cd jblogs
pipenv --python /usr/local/bin/python3
pipenv shell
pipenv install -r requirements.txt

pipenv requirements > requirements.txt
pipenv requirements --dev > dev-requirements.txt

```
