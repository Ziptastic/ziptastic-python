Official Ziptastic Python Library
=================================


Python library for `GetZiptastic.com <https://www.getziptastic.com>`_
---------------------------------------------------------------------

.. image:: https://readthedocs.org/projects/ziptastic-python/badge/?version=latest
   :target: http://ziptastic-python.readthedocs.org/en/latest/?badge=latest

.. image:: https://codecov.io/gh/ziptastic/ziptastic-python/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ziptastic/ziptastic-python/branch/master

.. image:: https://travis-ci.org/Ziptastic/ziptastic-python.svg?branch=master
   :target: https://travis-ci.org/Ziptastic/ziptastic-python

.. image:: https://circleci.com/gh/Ziptastic/ziptastic-python.png
   :target: https://circleci.com/gh/Ziptastic/ziptastic-python

Installation
------------

    >>> pip install ziptastic-python


Running tests
-------------

    $ nosetests

Running tests with coverage
---------------------------

    $ nosetests --with-coverage --cover-package=ziptastic


Usage
=====

Forward geocoding
-----------------

    >>> from ziptastic import Ziptastic
    >>> api = Ziptastic('<your api key>')
    >>> result = api.get_from_postal_code('48867')


Reverse geocoding
-----------------

    >>> from ziptastic import Ziptastic
    >>> api = Ziptastic('<your api key>')
    >>> result = api.get_from_coordinates('42.9934', '-84.1595')
