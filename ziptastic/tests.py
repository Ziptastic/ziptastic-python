import unittest
from mock import patch, Mock

from ziptastic import Ziptastic

compare_v3_json = ["""[{"city": "Owosso", "country": "US",
    "county": "Shiawassee", "state": "Michigan", "state_short": "MI",
    "postal_code": "48867"}]"""]

compare_v2_json = ["""{"city": "Owosso", "country": "US",
    "county": "Shiawassee", "state": "Michigan", "state_short": "MI",
    "postal_code": "48867"}"""]


class TestZiptasticLib(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('urllib2.urlopen')
        self.urllib_mock = self.patcher.start()

        self.urllib2_v3_mock = Mock()
        self.urllib2_v3_mock.read.side_effect = compare_v3_json
        self.urllib_mock.return_value = self.urllib2_v3_mock

    def setUpV3(self):
        self.urllib_mock.stop()
        self.urllib_mock = self.patcher.start()
        self.urllib2_v2_mock = Mock()
        self.urllib2_v2_mock.read.side_effect = compare_v2_json
        self.urllib_mock.return_value = self.urllib2_v2_mock

    def tearDown(self):
        self.urllib_mock.stop()

    def test_get_from_v3_postal_code(self):
        postal_code = '48867'
        Ziptastic.api_key = 'abc123'
        result = Ziptastic.get_from_postal_code(postal_code)

        self.assertIn('postal_code', result[0])
        self.assertEqual('https://zip.getziptastic.com/v3/US/48867',
                         self.urllib_mock.call_args[0][0].get_full_url())

    def test_get_from_v2_postal_code(self):
        self.setUpV3()

        postal_code = '48867'
        result = Ziptastic.get_from_postal_code(postal_code)

        self.assertIn('postal_code', result)
        self.assertEqual('https://zip.getziptastic.com/v2/US/48867',
                         self.urllib_mock.call_args[0][0].get_full_url())

    def test_build_url(self):
        version = 'v42'
        endpoint = 'test.endpoint'
        correct_url = 'https://test.endpoint/v42/'
        self.assertEquals(correct_url, Ziptastic.build_url(endpoint,
                                                           version=version))

    def test_object_is_returned(self):
        result = Ziptastic.get_from_postal_code('48867')
        self.assertTrue(type(result), 'object')


if __name__ == '__main__':
    unittest.main()
