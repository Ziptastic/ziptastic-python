import unittest
from mock import patch, Mock
import requests_mock
from nose.tools import eq_
from json import loads

from ziptastic import Ziptastic

compare_v3_json = """[{"city": "Owosso", "country": "US",
    "county": "Shiawassee", "state": "Michigan", "state_short": "MI",
    "postal_code": "48867"}]"""

compare_v2_json = """{"city": "Owosso", "country": "US",
    "county": "Shiawassee", "state": "Michigan", "state_short": "MI",
    "postal_code": "48867"}"""


class TestZiptasticLib(unittest.TestCase):
    @requests_mock.mock()
    def test_get_from_v3_postal_code(self, m):
        url = 'https://zip.getziptastic.com/v3/US/48867'
        m.get(url, text=compare_v3_json)
        postal_code = '48867'
        Ziptastic.api_key = 'abc123'
        ziptastic = Ziptastic('abc123')
        result = ziptastic.get_from_postal_code(postal_code)

        req = m.request_history[0]
        eq_(url, req.url)
        eq_(loads(compare_v3_json), result)

    @requests_mock.mock()
    def test_get_from_v2_postal_code(self, m):
        url = 'https://zip.getziptastic.com/v2/US/48867'
        m.get(url, text=compare_v2_json)
        postal_code = '48867'
        ziptastic = Ziptastic('')
        result = ziptastic.get_from_postal_code(postal_code)

        req = m.request_history[0]
        eq_(url, req.url)
        eq_(loads(compare_v2_json), result)

    def test_build_url(self):
        version = 'v42'
        endpoint = 'test.endpoint'
        correct_url = 'https://test.endpoint/v42'
        self.assertEquals(correct_url, Ziptastic.build_url(endpoint,
                                                           version=version))
