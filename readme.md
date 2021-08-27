Steps to run code quality.

- Flake:
    docker-compose run --rm django flake8 .

- Black:
    docker-compose run --rm django black --check --exclude=migrations .
    docker-compose run --rm django black --diff --exclude=migrations .
    docker-compose run --rm django black --exclude=migrations .

- Isort:
    docker-compose run --rm django isort . --check-only
    docker-compose run --rm django isort . --diff
    docker-compose run --rm django isort .

- Reverifying:
    docker-compose run --rm django flake8 .
    docker-compose run --rm django black --check --exclude=migrations .
    docker-compose run --rm django isort . --check-only

- Running Pytest
    docker-compose run --rm django pytest