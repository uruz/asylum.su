import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
NAME = 'site_asylum'
with open(os.path.join(here, 'README.md')) as readme:
    README = readme.read()

requires = [
    'django==1.7',
    'gunicorn',
    'psycopg2',
    'pytz',
]

setup(name=NAME,
      version='0.0',
      description='site_asylum',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite=NAME,
      install_requires=requires,
)
