.PHONY: all clean doc test

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

test:
	docker-compose -f docker-compose.test.yml build
	docker-compose -f docker-compose.test.yml up -d
	@sleep 10
	docker exec -it flaskapp-test /wait-for-it.sh localhost:80 -- pytest