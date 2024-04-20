# pitcher-watch

![pre-commit Action](https://github.com/btambara/pitcher-watch/actions/workflows/pre-commit.yml/badge.svg)
![pytest Action](https://github.com/btambara/pitcher-watch/actions/workflows/pytest.yml/badge.svg)
![vitest Action](https://github.com/btambara/pitcher-watch/actions/workflows/vitest.yml/badge.svg)

## Tech Stack

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![Vuetify](https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=AEDDFF)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)

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
