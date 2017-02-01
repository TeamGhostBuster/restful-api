doc:
	apidoc -i app/api/ doc/
	git subtree push --prefix doc origin gh-pages