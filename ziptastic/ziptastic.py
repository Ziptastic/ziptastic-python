import requests


class ZiptasticAPIKeyRequiredException(Exception):
    pass


class Ziptastic(object):
    """Ziptastic Python Module"""

    #: The current endpoint where Ziptastic APIs are served from.
    endpoint = 'zip.getziptastic.com'

    def __init__(self, api_key):
        """
        Initialize Ziptastic API

        :param: This is your Ziptastic API Key that you can get from
            https://www.getziptastic.com/dashboard
        """
        self.api_key = api_key

    @staticmethod
    def build_url(endpoint, version='v3', preferred_protocol='https'):
        """Build the Ziptastic API url."""
        return preferred_protocol + '://' + endpoint + '/' + version

    def get_from_postal_code(self, postal_code, country='US'):
        """Get geo data from postal code and country code"""
        headers = {}

        #: If no api_key is set then default to Version 2 of Ziptastic API.
        if self.api_key:
            headers.update({
                "x-key": self.api_key
            })
            uri = self.build_url(self.endpoint)
        else:
            uri = self.build_url(self.endpoint, version='v2')

        url = "{uri}/{country}/{postal_code}".format(uri=uri, country=country,
                                                     postal_code=postal_code)

        r = requests.get(url, headers=headers)

        return r.json()

    def get_from_coordinates(self, latitude, longitude):
        """Get geo data from coordinates"""

        headers = {}

        #: If no api_key is set then default to Version 2 of Ziptastic API.
        if self.api_key:
            headers.update({
                "x-key": self.api_key
            })
            uri = self.build_url(self.endpoint)
        else:
            raise ZiptasticAPIKeyRequiredException

        url = "{uri}/{latitude}/{longitude}".format(uri=uri, latitude=latitude,
                                                    longitude=longitude)

        r = requests.get(url, headers=headers)

        return r.json()
