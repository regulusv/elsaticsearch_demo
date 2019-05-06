#!/usr/bin/env bash

curl -X POST localhost:9200/school_demo/_doc/1 -H 'Content-Type: application/json' \
     -d '
{
    "name": "San Mateo High School",
    "city": "San Mateo",
    "state": "California",
    "country": "US",
    "code": "a41vwe4",
    "school_type": ["high_school"],
    "latitude": 37.544632,
    "longitude": -122.290188,
    "number_of_users": 20
  }'
curl -X POST localhost:9200/school_demo/_doc/2 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "San Mateo Middle School",
    "city": "San Mateo",
    "state": "California",
    "country": "US",
    "code": "502f23kj",
    "school_type": ["middle_school"],
    "latitude": 37.563245,
    "longitude": -122.249657,
    "number_of_users": 320
  }'
curl -X POST localhost:9200/school_demo/_doc/3 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "San Mateo Elementary School",
    "city": "San Mateo",
    "state": "California",
    "country": "US",
    "code": "u01jao23",
    "school_type": ["elementary_school"],
    "latitude": 37.543778,
    "longitude": -122.307988,
    "number_of_users": 49
  }'
curl -X POST localhost:9200/school_demo/_doc/4 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "San Diego High School",
    "city": "San Diego",
    "state": "California",
    "country": "US",
    "code": "gjqp245",
    "school_type": ["high_school"],
    "latitude": 32.832585,
    "longitude": -117.160717,
    "number_of_users": 533
  }'
curl -X POST localhost:9200/school_demo/_doc/5 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "San Francisco Middle School",
    "city": "San Francisco",
    "state": "California",
    "country": "US",
    "code": "4ja03j",
    "school_type": ["middle_school"],
    "latitude": 37.746773,
    "longitude": -122.427137,
    "number_of_users": 82
  }'
curl -X POST localhost:9200/school_demo/_doc/6 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "Fries High School",
    "city": "Portland",
    "state": "Oregon",
    "country": "US",
    "code": "5j1jla",
    "school_type": ["high_school"],
    "latitude": 45.478980,
    "longitude": -122.617322,
    "number_of_users": 86
  }'
curl -X POST localhost:9200/school_demo/_doc/7 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "Hamburger Elementary School",
    "city": "Fresno",
    "state": "California",
    "country": "US",
    "code": "5j1l04",
    "school_type": ["elementary_school"],
    "latitude": 36.778856,
    "longitude": -119.790636,
    "number_of_users": 36
  }'
curl -X POST localhost:9200/school_demo/_doc/8 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "Hogwarts Witchcraft and Wizardry",
    "city": "Taumuning",
    "state": "Guam",
    "country": "US",
    "code": "gnb0f84",
    "school_type": ["high_school", "middle_school", "elementary_school"],
    "latitude": 13.505329,
    "longitude": 144.799088,
    "number_of_users": 44
  }'
curl -X POST localhost:9200/school_demo/_doc/9 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "Polk School",
    "city": "Portland",
    "state": "Oregon",
    "country": "US",
    "code": "jale151",
    "school_type": ["middle_school", "elementary_school"],
    "latitude": 45.518589,
    "longitude": -122.676156,
    "number_of_users": 2
  }'
curl -X POST localhost:9200/school_demo/_doc/10 -H 'Content-Type: application/json' \
     -d '
  {
    "name": "Bayside School",
    "city": "Kansas City",
    "state": "Missouri",
    "country": "US",
    "code": "vmo4jaks",
    "school_type": ["high_school", "elementary_school"],
    "latitude": 39.087773,
    "longitude": -94.587777,
    "number_of_users": 59
  }'