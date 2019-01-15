test: test.py schoolsearch.py
	python test.py > test.out
	cat test.out
default: schoolsearch.py 
	python -c 'import schoolsearch; schoolsearch.main()'
