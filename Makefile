DOCS_DIR=doc
MSG=Deploy API Documentation

format:
	yapf -r -p app/*

doc:
	apidoc -i app/ $DOCS_DIR
	ghp-import -n -p -m $MSG $DOCS_DIR