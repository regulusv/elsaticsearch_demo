# A RESTful API Service to Query ElasticSearch

## About
The API will give result on query, the related results are sorted.

port for ElasticSearch is 9200
port for flask as web server is 8000

## How to run the application
Install docker and docker-compose. Build the docker image.
$ docker-compose up
then the web server is running in port 8000, read the following for using API


## Populate database
On the host system, go to root folder of the project
$ chmod u+x setup.sh
$ bash setup.sh

## To view the data in database
$ curl -H 'Content-Type: application/json' -X GET http://localhost:9200/school_demo/_search?pretty


### GET /school_demo
Query school name or something related:

$ curl -i -H "Accept: application/json" http://localhost:8000/school_demo/search?q=Polk%20School

### Test
$ python basic_api_tests.py -v
it will show:

tests done
...
----------------------------------------------------------------------
Ran 3 tests in 88.108s

OK

Process finished with exit code 0

