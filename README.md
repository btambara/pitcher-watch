# pitcher-watch

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar).

## [pip-tools](https://pypi.org/project/pip-tools/)

``` bash
// Setup Dev Environment
pip-sync setup/requirements.txt setup/development/requirements.txt
```

## [pre-commit](https://pre-commit.com/)

``` bash
// Fixes all issues
bash scripts/pre-commit-fix.sh
```

## [SQLAlchemy](https://www.sqlalchemy.org/)

``` bash
// Manual migrations run
alembic revision -m "Create player table"
```

## Run [pytest](https://docs.pytest.org/en/8.0.x/) locally

``` bash
// Run test locally
bash scripts/run-pytest.sh
```
