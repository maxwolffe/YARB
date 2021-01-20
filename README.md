# YARB
Yet Another Recipe Book

[![Coverage Status](https://coveralls.io/repos/github/maxwolffe/YARB/badge.svg?branch=)](https://coveralls.io/github/maxwolffe/YARB?branch=master)
![Docker Image CI](https://github.com/maxwolffe/YARB/workflows/Docker%20Image%20CI/badge.svg)

A Django app for organizing meal planning and for me to learn how to productionize a Docker based application.

# Getting started

## Starting the application locally
1. Bring up the local db and webapp  
   `docker-compose up`
2. Execute migrations against the local db  
  `docker-compose run web sh -c "python manage.py makemigrations && python manage.py migrate"`
