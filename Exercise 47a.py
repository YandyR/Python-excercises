try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Alberto',
    'url': 'localhost:8080/lab?',
    'download_url': 'localhost:8080/lab?',
    'author_email': 'albertomunoz114@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}
setup(**config)

