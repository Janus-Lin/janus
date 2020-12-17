CHECK_DIRS=.

FLAKE8_CONFIG=tox.ini

TEST_DIR=tests/system_test tests/unittest

all_tests: flake8 test

flake8:
	flake8 $(CHECK_DIRS) --config=$(FLAKE8_CONFIG)

test:
	cp log/log.py log/log.py.org
	cp log/log_test.py  log/log.py
	coverage run --parallel-mode -m pytest $(TEST_DIR) -sv
	coverage combine
	coverage html --rcfile=tox.ini
	coverage report --rcfile=tox.ini
	mv log/log.py.org log/log.py

install:
	# apt-get install $(grep -vE "^\s*#" requirements/packages.txt  | tr "\n" " ")
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements/product.txt
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements/devel.txt
