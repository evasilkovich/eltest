import unittest
from unittest.mock import patch
from controllers import hello


class TestStringMethods(unittest.TestCase):

    @patch('controllers.hello.put_object')
    def test_hello(self, MockPutObject):
        response = hello.handler([],[])
        self.assertEqual(response["body"], 'helloworld')


if __name__ == '__main__':
    unittest.main()
