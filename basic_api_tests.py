"""

How to run Python test:
1. Change HOST or PORT variables if need be.
2. python basic_api_tests.py -v

"""
import unittest
import requests
import json


class TestSearchAPI(unittest.TestCase):
    HOST = "http://localhost"
    PORT = "8000"

    def test_exact_match(self):
        response = requests.get("{}:{}/school_demo/search?q={}".format(self.HOST, self.PORT, "Polk School"))
        results = response.json()
        with open('test_log.txt', 'w') as outfile:
            json.dump(results, outfile)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["code"], "jale151")

        response = requests.get("{}:{}/school_demo/search?q={}".format(self.HOST, self.PORT, "Portland"))
        results = response.json()
        with open('test_log.txt', 'a') as outfile:
            json.dump(results, outfile)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["code"], "jale151")
        self.assertEqual(results[1]["code"], "5j1jla")

    def test_part_match(self):
        response = requests.get("{}:{}/school_demo/search?q={}".format(self.HOST, self.PORT, "Polk"))
        results = response.json()
        with open('test_log.txt', 'a') as outfile:
            json.dump(results, outfile)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["code"], "jale151")

        response = requests.get("{}:{}/school_demo/search?q={}".format(self.HOST, self.PORT, "Kansas"))
        results = response.json()
        with open('test_log.txt', 'a') as outfile:
            json.dump(results, outfile)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["code"], "vmo4jaks")

        response = requests.get("{}:{}/school_demo/search?q={}".format(self.HOST, self.PORT, "San Mateo"))
        results = response.json()
        with open('test_log.txt', 'a') as outfile:
            json.dump(results, outfile)
        self.assertEqual(len(results), 4)
        self.assertEqual(results[0]["code"], "502f23kj")
        self.assertEqual(results[1]["code"], "a41vwe4")
        self.assertEqual(results[2]["code"], "4ja03j")
        self.assertEqual(results[3]["code"], "u01jao23")

    def test_no_results(self):
        response = requests.get("{}:{}/school_demo/search?q={}".format(self.HOST, self.PORT, "steve"))
        results = response.json()
        self.assertEqual(len(results), 0)

    print("tests done")


if __name__ == '__main__':
    unittest.main()
