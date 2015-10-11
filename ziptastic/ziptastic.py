import urllib2
import json


class Ziptastic(object):
    """Ziptastic Python Module"""

    #: This is your Ziptastic API Key that you can get from
    #: https://www.getziptastic.com/dashboard
    api_key = ''

    #: The current endpoint where Ziptastic APIs are served from.
    endpoint = 'zip.getziptastic.com'

    @staticmethod
    def build_url(endpoint, version='v3', preferred_protocol='https'):
        """Build the Ziptastic API url."""
        return preferred_protocol + '://' + endpoint + '/' + version + '/'

    @classmethod
    def get_from_postal_code(cls, postal_code, country='US'):
        """Get geo data from postal code and country code"""
        headers = {}

        #: If no api_key is set then default to Version 2 of Ziptastic API.
        if cls.api_key:
            headers.update({
                "x-key": cls.api_key
            })
            uri = cls.build_url(cls.endpoint)
        else:
            uri = cls.build_url(cls.endpoint, version='v2')

        url = uri + str(country) + '/' + str(postal_code)

        request = urllib2.Request(url, headers=headers)
        contents = urllib2.urlopen(request).read()

        #: An object is returned.
        return json.loads(contents)
