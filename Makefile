default: schoolsearch.py
	python3 -c 'import schoolsearch; schoolsearch.main()'

test: test.py schoolsearch.py
	python3 test.py 2> test.out
	cat test.out
