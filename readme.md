Steps to run code quality.

- Flake:
    docker-compose run --rm django flake8 server

- Black:
    docker-compose run --rm django black --check --exclude=migrations server
    docker-compose run --rm django black --diff --exclude=migrations server
    docker-compose run --rm django black --exclude=migrations server

- Isort:
    docker-compose run --rm django isort server --check-only
    docker-compose run --rm django isort server --diff
    docker-compose run --rm django isort server

- Reverifying:
    docker-compose run --rm django flake8 server
    docker-compose run --rm django black --check --exclude=migrations server
    docker-compose run --rm django isort server --check-only