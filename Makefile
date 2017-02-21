.PHONY: all clean doc

MSG=Deploy API Documentation

build:
	@pipreqs . --force

format:
	@yapf -r -p app/*

doc:
	apidoc -i app/ doc/
	ghp-import -n -p -m $MSG doc/

clean:
	@rm -rf $DOCS_DIR dist/ build/ app.egg-info/
	@find . -name '__pycache__' -delete -exec rm -rf {} \;
