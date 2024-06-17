install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

lint:
	poetry run pre-commit run --all-files

run-server:
	poetry run python -m cooking_core.manage runserver 0:8007

.PHONY: createsuperuser
createsuperuser:
	poetry run python -m cooking_core.manage createsuperuser

.PHONY: install
install:
	poetry install

.PHONY: makemigrations
makemigrations:
	poetry run python -m cooking_core.manage makemigrations

.PHONY: dry-run
dry-run:
	poetry run python -m cooking_core.manage makemigrations dry-run

.PHONY: migrate
migrate:
	poetry run python -m cooking_core.manage migrate

.PHONY: update
update: install migrate install-pre-commit ;


.PHONY: lint install-pre-commit

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml up --force-recreate db


.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no
