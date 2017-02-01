doc:
	apidoc -i app/api/ doc/
	@git add -f doc && git commit -m 'Deploy API Documentation'
	git subtree push --prefix dist origin gh-pages