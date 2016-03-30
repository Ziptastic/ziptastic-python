# Official Ziptastic Python Library
Official python library for GetZiptastic.com

[![Documentation Status](https://readthedocs.org/projects/ziptastic-python/badge/?version=latest)](http://ziptastic-python.readthedocs.org/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/Ziptastic/ziptastic-python.svg?branch=master)](https://travis-ci.org/Ziptastic/ziptastic-python)
[![Coverage Status](https://coveralls.io/repos/Ziptastic/ziptastic-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/Ziptastic/ziptastic-python?branch=master)

## Installation
    pip install ziptastic-python (coming soon)


## Testing
`$ nosetests`

With coverage

`$ nosetests --with-coverage --cover-package=ziptastic`


## Usage
### Forward geocoding
```python
from ziptastic import Ziptastic

# Set your API key. (Available at https://www.getziptastic.com/dashboard)
api = Ziptastic('<your api key>')
result = api.get_from_postal_code('48867')
```

### Reverse geocoding
```python
from ziptastic import Ziptastic

# Set API key.
api = Ziptastic('<your api key>')
result = api.get_from_coordinates('42.9934', '-84.1595')
```
