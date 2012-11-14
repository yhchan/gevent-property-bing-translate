clean:
	find . -name "*~" -delete
	find . -name "*.pyc" -delete

lint:
	pylint translate parse
