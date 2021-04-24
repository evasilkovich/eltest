import os
import unittest
import requests

class TestStringMethods(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def test_api(self):
        print('test_api')
        url = os.environ.get('API_GATEWAY_URL')
        print(url)
        url1 = url+'/hello'
        print(url1)

        # try:
            # headers = {"Content-Type": "application/json"}
        r = requests.get(url1)
        print(r.status_code)
        print(r.text)
        self.assertEqual(r.text, 'helloworld')

        # except Exception as err:
        #         print(f'Error occurred: {err}')


if __name__ == '__main__':
    unittest.main()