"""
Python project skeleton
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MyProj',
    'author': 'moodoki',
    'url': 'random.com',
    'packages': ['name'],
    'install_requires': ['nose'],
    'name': 'randomproj'
}

setup(**config)
