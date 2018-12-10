# obj

This module provides a wrapper for dict and list items that exposes dict entries as it's attributes.

### Installation

    $ pipenv install -e git+https://github.com/rusintez/obj.git#egg=obj
    # $ pip install git+ssh://git@github.com/rusintez/obj.git@master

### Usage 
```py
# import
from obj import to_obj

# initialize
object = to_obj({ 'foo': 'bar' })
array = to_obj([{ 'baz': 'qux' }])

# provides accessors
object.foo

# provides support for nested properties
array[0].baz

# in the iterator
item.baz for item in array
``` 

### Prerequisites

- git
- python >=3.4
- pipenv

### Development

    $ git clone git@github.com:rusintez/obj.git
    $ cd obj
    $ pipenv install
    $ pipenv run clean
    $ pipenv run format
    $ pipenv run lint
    $ pipenv run test
    $ pipenv run coverage
    $ pipenv run coverageReport
    $ open htmlcov/index.html

### Author

Vladimir Popov <rusintez@gmail.com>

### License

MIT