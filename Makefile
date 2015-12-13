.PHONY: all clean coverage test verbose

all: clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage:
	nosetests code/utils/tests data/tests/ --with-coverage --cover-package=code/utils/functions,data/data_hashes.py

test:
	nosetests code/utils/tests data/tests/

verbose:
	nosetests data/tests code/utils/tests -v
