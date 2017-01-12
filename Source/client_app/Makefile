init:
	pip install -r requirements.txt

package:
	python setup.py sdist
	python setup.py bdist --formats=wininst

install:
	-pip uninstall sysinfo_client_app -y
	-rm -rf dist
	pip install dist/sysinfo_client_app-*.tar.gz

test:
	nosetests tests