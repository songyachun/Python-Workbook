try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Skeleton',
    'author': 'Sonya Song',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'songyachun@yeat.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Skeleton'
}

setup(**config)
