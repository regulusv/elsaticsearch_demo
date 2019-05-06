from flask import Flask, request, json
from elasticsearch import Elasticsearch

app = Flask(__name__)

ELASTICSEARCH_PORT = 9200
es = Elasticsearch([{'host': 'elasticsearch', 'port': ELASTICSEARCH_PORT}])

indexName = "school_demo"
docType = "_doc"
parameters = ["name", "city", "state", "country", "code", "school_type", "latitude", "longitude", "number_of_users"]
query_key = 'q'

NOT_ACCEPTABLE = 406  # Request is not Acceptable
SUCCESS = 200

WILDCARD_MATCHING = False
PORT = 8000


@app.route('/index')
def hello_world():
    return 'Hello World'


@app.route('/school_demo/search')
def get_every_candidate():
    res = []
    query_dict = request.args

    if request.method != 'GET':
        # HANDLE ERROR
        response = app.response_class(
            response=json.dumps(res),
            status=NOT_ACCEPTABLE,
            mimetype='application/json'
        )
        return response

    threshold = 0.5
    found_credible = True

    for tag in parameters[:-3]:
        if not WILDCARD_MATCHING:
            tmp = es.search(index=indexName, doc_type=docType,
                            body={'query': {'match': {tag: query_dict[query_key]}}})
        else:
            tmp = es.search(index=indexName, doc_type=docType,
                            body={'query': {'regexp': {tag: "*." + query_dict[query_key] + ".*"}}})

        if len(tmp['hits']['hits']) != 0:
            with open('log.txt', 'w') as outfile:
                json.dump(tmp['hits']['hits'], outfile)

            for candidate in tmp['hits']['hits']:
                if candidate['_score'] > threshold:
                    found_credible = True
                res.append(candidate)

    def sort_by_score(e):
        return -e['_score']

    res.sort(key=sort_by_score)

    res_filtered = []
    ids = set()
    if found_credible:
        for candidate in res:
            if candidate['_score'] > threshold and candidate['_id'] not in ids:
                ids.add(candidate['_id'])
                res_filtered.append(candidate['_source'])

    response = app.response_class(
        response=json.dumps(res_filtered),
        status=SUCCESS,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run('0.0.0.0', PORT, debug=True)
