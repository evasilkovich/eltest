import unittest
import os
import requests


class TestStringMethods(unittest.TestCase):

    def test_hello(self):
        url = os.environ.get('API_GATEWAY_URL')
        print(url)
        url1 = url+'/hello'
        print(url1)

        r = requests.get(url1)
        print(r.status_code)
        print(r.text)

        self.assertEqual(r.text, 'helloworld')


if __name__ == '__main__':
    unittest.main()
