
.PHONY: run-server
run-server:
	poetry run python -m core.manage runserver

.PHONY: install
install:
	poetry install

.PHONY: makemigrations
makemigrations:
	poetry run python -m core.manage makemigrations

.PHONY: dry-run
dry-run:
	poetry run python -m core.manage makemigrations dry-run

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: update
update: install migrate ;