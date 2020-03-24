setup:
	pre-commit install
	pre-commit install --hook-type commit-msg
	pre-commit install --hook-type pre-push