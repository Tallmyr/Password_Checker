# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['password_checker']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'password-checker',
    'version': '1.0',
    'description': 'Checks passwords against Have I Been Pwned Database',
    'long_description': 'Checks passwords against Have I Been Pawned Database\n\nThis can be downloaded and run using main.py for command-line version.\nAlternatively, this can also be installed using the whl in releases.\n',
    'author': 'Simon Tallmyr',
    'author_email': 'simon@tallmyr.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Tallmyr/Password-Checker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

