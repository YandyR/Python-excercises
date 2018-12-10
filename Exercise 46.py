try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Alberto',
    'url': 'localhost:8080/lab?',
    'download_url': 'localhost:8080/lab?',
    'author_email': 'albertomunoz114@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}
setup(**config)

