```shell
cd jblogs
pipenv --python /usr/local/bin/python3
pipenv shell
pipenv install -r requirements.txt

pipenv requirements > requirements.txt
pipenv requirements --dev > dev-requirements.txt


brew install --cask mactex
make clean latexpdf

```

需要安装MacTeX

```shell
brew install --cask mactex

make clean latexpdf
```

Sphinx 自动构建

```shell
sphinx-autobuild source build/html
```