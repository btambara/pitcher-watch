#!bin/bash

rm -rf test.db

pytest --cov-report term-missing --cov=api api/src
