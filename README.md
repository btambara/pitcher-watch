# pitcher-watch

This web application focuses on MLB pitchers and aims to display useful statistical information and highlights.

![pre-commit Action](https://github.com/btambara/pitcher-watch/actions/workflows/pre-commit.yml/badge.svg)
![pytest Action](https://github.com/btambara/pitcher-watch/actions/workflows/pytest.yml/badge.svg)
![vitest Action](https://github.com/btambara/pitcher-watch/actions/workflows/vitest.yml/badge.svg)

## Tech Stack

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![Vuetify](https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=AEDDFF)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)

## Development Environment

First, rename `.env copy` to `.env`.

Run:

``` bash
openssl rand -base64 48
```

Next, copy and paste the openssl return value in `SECRET_KEY` in `.env`

Finally, fill out the keys with the proper values.

### Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar).

### [pip-tools](https://pypi.org/project/pip-tools/) - Setup Dev Environment

``` bash
pip-sync setup/requirements.txt setup/development/requirements.txt
```

### [pre-commit](https://pre-commit.com/) - Fixes all formating/lint issues

``` bash
bash scripts/pre-commit-fix.sh
```

### [SQLAlchemy](https://www.sqlalchemy.org/) - Manual migrations run

``` bash
alembic revision -m "Create player table"
```

### [pytest](https://docs.pytest.org/en/8.0.x/) - Run test locally

``` bash
bash scripts/run-pytest.sh
```

## Copyright Notice

This package and its author are not affiliated with MLB or any MLB team. Use of MLB data is subject to the notice posted at <http://gdx.mlb.com/components/copyright.txt>.
